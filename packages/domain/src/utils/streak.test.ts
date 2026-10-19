import { describe, expect, it } from 'vitest';
import { type DayLog, type LogStatus } from '../types/domain.types';
import { computeStreak } from './streak';

// Weeks start on Saturday; one miss a week is forgiven.
const settings = { weekStart: 6, allowedMissesPerWeek: 1 };
const log = (date: string, status: LogStatus): DayLog => ({ date, status, value: null });
const done = (...days: string[]) => days.map((day) => log(`2026-10-${day}`, 'done'));

describe('computeStreak: day-unit rules', () => {
  // Sat 2026-10-17 → Fri 2026-10-23 (today)
  const daily = { repeat: 'daily' as const, startDate: '2026-10-17' };

  it('forgives the first miss of a week; skipped changes nothing', () => {
    const logs = [...done('17', '18', '20', '22'), log('2026-10-21', 'skipped')];
    expect(computeStreak(daily, logs, '2026-10-23', settings)).toEqual({ unit: 'day', count: 4 });
  });

  it('resets on the second miss of the same week', () => {
    const logs = done('17', '18', '20', '22');
    expect(computeStreak(daily, logs, '2026-10-23', settings)).toEqual({ unit: 'day', count: 1 });
  });

  it('a backfill joins two streaks into one', () => {
    const rule = { repeat: 'daily' as const, startDate: '2026-10-15' };
    const logs = done('15', '16', '17', '18', '20', '21', '23'); // Mon 19 and Thu 22 missed
    expect(computeStreak(rule, logs, '2026-10-23', settings).count).toBe(1);
    expect(computeStreak(rule, [...logs, ...done('22')], '2026-10-23', settings).count).toBe(8);
  });

  it('today without a log is pending, not a miss', () => {
    const rule = { repeat: 'weekly' as const, weekdays: [1, 4], startDate: '2026-10-10' };
    const logs = done('12', '15'); // last week's Mon and Thu
    expect(computeStreak(rule, logs, '2026-10-22', settings).count).toBe(2); // Mon 19 forgiven
    expect(computeStreak(rule, logs, '2026-10-23', settings).count).toBe(0); // Thu 22 is miss #2
  });

  it('partial counts; a log on a day that was not expected does not', () => {
    const rule = { repeat: 'weekly' as const, weekdays: [1], startDate: '2026-10-17' };
    const logs = [log('2026-10-19', 'partial'), log('2026-10-20', 'done')];
    expect(computeStreak(rule, logs, '2026-10-20', settings).count).toBe(1);
  });

  it('is 0 before the habit starts', () => {
    expect(computeStreak(daily, [], '2026-10-01', settings).count).toBe(0);
  });
});

describe('computeStreak: n_per_week', () => {
  const gym = { repeat: 'n_per_week' as const, timesPerWeek: 3, startDate: '2026-10-07' }; // Wed
  const fullWeeks = { ...gym, startDate: '2026-10-10' }; // Sat

  it('counts whole weeks (the lesson example)', () => {
    const logs = [
      ...done('08'), // Oct 3–9: partial first week, can't break
      ...done('10', '12', '14'), // Oct 10–16: 3 of 3
      ...done('18', '21'), // Oct 17–23: 2 of 3, forgiven
      ...done('24', '28'), // Oct 24–30: 2 of 2 (one skip)
      log('2026-10-26', 'skipped'),
      log('2026-11-02', 'done'), // current week: pending
    ];
    expect(computeStreak(gym, logs, '2026-11-03', settings)).toEqual({ unit: 'week', count: 2 });
  });

  it('a skip lowers what the week owes', () => {
    const logs = [...done('10', '11', '12', '18'), log('2026-10-19', 'skipped')];
    expect(computeStreak(fullWeeks, logs, '2026-10-25', settings).count).toBe(1);
  });

  it('the current week is pending; it breaks once the next week starts', () => {
    const logs = done('10', '11', '12');
    expect(computeStreak(fullWeeks, logs, '2026-10-23', settings).count).toBe(1);
    expect(computeStreak(fullWeeks, logs, '2026-10-24', settings).count).toBe(0);
  });

  it('a full first week can break; a partial one cannot', () => {
    expect(computeStreak(fullWeeks, done('11'), '2026-10-17', settings).count).toBe(0);
    expect(computeStreak(gym, done('08', '10', '11', '12'), '2026-10-17', settings).count).toBe(1);
  });

  it('overachieving is +1; an all-skipped week is neutral', () => {
    const sick = ['17', '18', '19'].map((day) => log(`2026-10-${day}`, 'skipped'));
    const logs = [...done('10', '11', '12', '13', '14', '15'), ...sick];
    expect(computeStreak(fullWeeks, logs, '2026-10-24', settings).count).toBe(1);
  });

  it('counts the current week as soon as it hits the target', () => {
    expect(computeStreak(fullWeeks, done('10', '11', '12'), '2026-10-12', settings).count).toBe(1);
  });
});

describe('computeStreak: bad input', () => {
  it('throws', () => {
    const daily = { repeat: 'daily' as const, startDate: '2026-10-17' };
    const tooMany = { weekStart: 6, allowedMissesPerWeek: 8 };
    expect(() => computeStreak(daily, [], '2026-10-23', tooMany)).toThrow(RangeError);
    expect(() => computeStreak(daily, [], '2026-02-30', settings)).toThrow(RangeError);
    expect(() =>
      computeStreak(
        { repeat: 'n_per_week', timesPerWeek: 0, startDate: '2026-10-17' },
        [],
        '2026-10-23',
        settings,
      ),
    ).toThrow(RangeError);
  });
});
