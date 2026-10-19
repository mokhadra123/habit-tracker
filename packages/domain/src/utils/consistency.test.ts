import { describe, expect, it } from 'vitest';
import { type ConsistencySettings, type DayLog, type LogStatus } from '../types/domain.types';
import { consistencyScore } from './consistency';

const rolling: ConsistencySettings = { weekStart: 6, targetValue: null, window: 'rolling' };
const lifetime: ConsistencySettings = { ...rolling, window: 'lifetime' };

const log = (date: string, status: LogStatus, value: number | null = null): DayLog => ({
  date,
  status,
  value,
});
const doneOct = (...days: number[]) =>
  days.map((day) => log(`2026-10-${String(day).padStart(2, '0')}`, 'done'));
const range = (from: number, to: number) =>
  Array.from({ length: to - from + 1 }, (_, index) => from + index);

describe('consistencyScore: day-unit rules', () => {
  const daily = { repeat: 'daily' as const, startDate: '2026-09-01' };
  // Oct 1–29 done except Oct 10; today Oct 30 not logged yet.
  const month = doneOct(...range(1, 29).filter((day) => day !== 10));

  it('rolls over the last 30 days; today without a log is left out', () => {
    expect(consistencyScore(daily, month, '2026-10-30', rolling)).toBeCloseTo(28 / 29);
  });

  it('lifetime counts every day since startDate (FR-2.7)', () => {
    // All 30 days of September were missed.
    expect(consistencyScore(daily, month, '2026-10-30', lifetime)).toBeCloseTo(28 / 59);
  });

  it('weighs a partial by its share of the target', () => {
    const rule = { repeat: 'daily' as const, startDate: '2026-10-18' };
    const logs = [log('2026-10-18', 'done', 8), log('2026-10-19', 'partial', 4)];
    const settings = { ...rolling, targetValue: 8 };
    expect(consistencyScore(rule, logs, '2026-10-19', settings)).toBeCloseTo(0.75);
  });

  it('leaves skipped days out of both sides (FR-2.5)', () => {
    const rule = { repeat: 'daily' as const, startDate: '2026-10-18' };
    const logs = [log('2026-10-18', 'skipped'), log('2026-10-19', 'done')];
    expect(consistencyScore(rule, logs, '2026-10-19', rolling)).toBe(1);
  });

  it('only judges expected days', () => {
    const mondays = { repeat: 'weekly' as const, weekdays: [1], startDate: '2026-10-05' };
    // Mon 5 done, Wed 7 is not expected, Mon 12 missed, Mon 19 is today.
    expect(consistencyScore(mondays, doneOct(5, 7), '2026-10-19', rolling)).toBe(0.5);
  });

  it('is null when nothing has been asked for yet', () => {
    const fresh = { repeat: 'daily' as const, startDate: '2026-10-19' };
    expect(consistencyScore(fresh, [], '2026-10-19', rolling)).toBeNull();
    expect(consistencyScore(fresh, doneOct(19), '2026-10-19', rolling)).toBe(1);
    expect(consistencyScore(fresh, [], '2026-10-18', rolling)).toBeNull();
    const allSkipped = [log('2026-10-18', 'skipped'), log('2026-10-19', 'skipped')];
    const rule = { repeat: 'daily' as const, startDate: '2026-10-18' };
    expect(consistencyScore(rule, allSkipped, '2026-10-19', rolling)).toBeNull();
  });
});

describe('consistencyScore: n_per_week', () => {
  const gym = { repeat: 'n_per_week' as const, timesPerWeek: 3, startDate: '2026-10-07' }; // Wed
  const logs = [
    ...doneOct(8), // Oct 3–9: partial first week, left out
    ...doneOct(10, 12, 14), // Oct 10–16: 3 of 3
    ...doneOct(18, 21), // Oct 17–23: 2 of 3
    ...doneOct(24, 28), // Oct 24–30: 2 of 2 (one skip)
    log('2026-10-26', 'skipped'),
    log('2026-11-02', 'done'), // current week: left out
  ];

  it('judges complete weeks only', () => {
    expect(consistencyScore(gym, logs, '2026-11-03', rolling)).toBeCloseTo(7 / 8);
  });

  it('rolling is the last 4 complete weeks; lifetime goes back to startDate', () => {
    const early = { ...gym, startDate: '2026-09-05' }; // Sat: Sep 5–Oct 2 all missed
    // rolling: Oct 3–9 is now a full week, 1 of 3 → (1 + 3 + 2 + 2) of (3 + 3 + 3 + 2)
    expect(consistencyScore(early, logs, '2026-11-03', rolling)).toBeCloseTo(8 / 11);
    // lifetime adds 4 September weeks of 0 of 3
    expect(consistencyScore(early, logs, '2026-11-03', lifetime)).toBeCloseTo(8 / 23);
  });

  it('caps a week at what it owes; an all-skipped week owes nothing', () => {
    const rule = { ...gym, startDate: '2026-10-10' };
    const sick = [17, 18, 19].map((day) => log(`2026-10-${day}`, 'skipped'));
    const busy = [...doneOct(10, 11, 12, 13, 14), ...sick];
    expect(consistencyScore(rule, busy, '2026-10-24', rolling)).toBe(1);
  });

  it('weighs partials', () => {
    const rule = { repeat: 'n_per_week' as const, timesPerWeek: 2, startDate: '2026-10-10' };
    const amounts = [log('2026-10-11', 'done', 30), log('2026-10-13', 'partial', 15)];
    const settings = { ...rolling, targetValue: 30 };
    expect(consistencyScore(rule, amounts, '2026-10-19', settings)).toBeCloseTo(0.75);
  });

  it('is null before the first complete week ends', () => {
    expect(
      consistencyScore({ ...gym, startDate: '2026-10-14' }, [], '2026-10-19', rolling),
    ).toBeNull();
  });
});

describe('consistencyScore: bad input', () => {
  it('throws on a partial with nothing to weigh, or a malformed rule', () => {
    const daily = { repeat: 'daily' as const, startDate: '2026-10-18' };
    expect(() =>
      consistencyScore(daily, [log('2026-10-18', 'partial')], '2026-10-19', rolling),
    ).toThrow(RangeError);
    expect(() =>
      consistencyScore(
        { repeat: 'n_per_week', timesPerWeek: 0, startDate: '2026-10-01' },
        [],
        '2026-10-19',
        rolling,
      ),
    ).toThrow(RangeError);
  });
});
