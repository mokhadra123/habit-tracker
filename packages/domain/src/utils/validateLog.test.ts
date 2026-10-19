import { describe, expect, it } from 'vitest';
import { type DayLog, type HabitForLog, type LogStatus } from '../types/domain.types';
import { validateLog } from './validateLog';

const today = '2026-10-19';
const bool: HabitForLog = { habitType: 'boolean', targetValue: null, startDate: '2026-09-01' };
const glasses: HabitForLog = { habitType: 'numeric', targetValue: 8, startDate: '2026-09-01' };
const minutes: HabitForLog = { habitType: 'duration', targetValue: 30, startDate: '2026-09-01' };

const log = (status: LogStatus, value: number | null = null, date = today): DayLog => ({
  date,
  status,
  value,
});
const verdict = (habit: HabitForLog, entry: DayLog, on = today) => {
  const result = validateLog(habit, entry, on);
  return result.ok ? 'ok' : result.reason;
};

describe('validateLog: the date', () => {
  it('rejects the future', () => {
    expect(verdict(bool, log('done', null, '2026-10-20'))).toBe('future_date');
  });

  it('allows today and the 6 days before it (FR-2.2)', () => {
    expect(verdict(bool, log('done'))).toBe('ok');
    expect(verdict(bool, log('done', null, '2026-10-13'))).toBe('ok');
    expect(verdict(bool, log('done', null, '2026-10-12'))).toBe('outside_edit_window');
  });

  it('works across a month boundary', () => {
    expect(verdict(bool, log('done', null, '2026-09-30'), '2026-10-06')).toBe('ok');
  });

  it('rejects a day before the habit started', () => {
    const fresh = { ...bool, startDate: '2026-10-15' };
    expect(verdict(fresh, log('done', null, '2026-10-14'))).toBe('before_start');
    expect(verdict(fresh, log('done', null, '2026-10-15'))).toBe('ok');
  });
});

describe('validateLog: status and value', () => {
  it('boolean: no partial, no value', () => {
    expect(verdict(bool, log('partial'))).toBe('partial_on_boolean');
    expect(verdict(bool, log('done', 3))).toBe('value_not_allowed');
  });

  it('skipped never carries a value', () => {
    expect(verdict(glasses, log('skipped'))).toBe('ok');
    expect(verdict(glasses, log('skipped', 2))).toBe('value_not_allowed');
    expect(verdict(bool, log('skipped'))).toBe('ok');
  });

  it('numeric: done and partial need a positive amount', () => {
    expect(verdict(glasses, log('done'))).toBe('value_required');
    expect(verdict(glasses, log('partial', 0))).toBe('value_required');
    expect(verdict(glasses, log('done', NaN))).toBe('value_required');
  });

  it('numeric: done reaches the target, partial stays below it', () => {
    expect(verdict(glasses, log('done', 5))).toBe('done_below_target');
    expect(verdict(glasses, log('done', 8))).toBe('ok');
    expect(verdict(glasses, log('done', 10))).toBe('ok');
    expect(verdict(glasses, log('partial', 5))).toBe('ok');
    expect(verdict(glasses, log('partial', 8))).toBe('partial_reaches_target');
  });

  it('duration follows the numeric rules', () => {
    expect(verdict(minutes, log('partial', 20))).toBe('ok');
    expect(verdict(minutes, log('done', 20))).toBe('done_below_target');
  });
});

describe('validateLog: bugs throw', () => {
  it('throws on malformed dates and a numeric habit without a target', () => {
    expect(() => validateLog(bool, log('done', null, '2026-13-01'), today)).toThrow(RangeError);
    expect(() => validateLog(bool, log('done'), '19-10-2026')).toThrow(RangeError);
    expect(() => validateLog({ ...glasses, targetValue: null }, log('done', 8), today)).toThrow(
      RangeError,
    );
  });
});
