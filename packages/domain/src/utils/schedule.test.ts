import { describe, expect, it } from 'vitest';
import { isExpectedOn, weekRangeFor } from './schedule';

// 2026-01-12 is a Monday.
const start = '2026-01-12';

describe('isExpectedOn', () => {
  it('daily: every day from startDate on', () => {
    const rule = { repeat: 'daily' as const, startDate: start };
    expect(isExpectedOn(rule, '2026-01-11')).toEqual({ unit: 'day', expected: false });
    expect(isExpectedOn(rule, start)).toEqual({ unit: 'day', expected: true });
  });

  it('weekly: only the chosen weekdays (0=Sunday)', () => {
    const rule = { repeat: 'weekly' as const, weekdays: [1, 4], startDate: start };
    expect(isExpectedOn(rule, '2026-01-12')).toEqual({ unit: 'day', expected: true }); // Mon
    expect(isExpectedOn(rule, '2026-01-13')).toEqual({ unit: 'day', expected: false }); // Tue
    expect(isExpectedOn(rule, '2026-01-15')).toEqual({ unit: 'day', expected: true }); // Thu
  });

  it('every_n_days: counted from startDate', () => {
    const rule = { repeat: 'every_n_days' as const, intervalDays: 3, startDate: '2026-01-01' };
    expect(isExpectedOn(rule, '2026-01-07')).toEqual({ unit: 'day', expected: true });
    expect(isExpectedOn(rule, '2026-01-08')).toEqual({ unit: 'day', expected: false });
  });

  it('n_per_week: a weekly target, never a per-day answer (FR-1.4)', () => {
    const rule = { repeat: 'n_per_week' as const, timesPerWeek: 3, startDate: start };
    expect(isExpectedOn(rule, '2026-01-14')).toEqual({ unit: 'week', target: 3 });
    expect(isExpectedOn(rule, '2026-01-11')).toEqual({ unit: 'week', target: 0 });
  });

  it('throws on a malformed rule or date', () => {
    expect(() => isExpectedOn({ repeat: 'weekly', weekdays: [], startDate: start }, start)).toThrow(
      RangeError,
    );
    expect(() =>
      isExpectedOn({ repeat: 'weekly', weekdays: [7], startDate: start }, start),
    ).toThrow(RangeError);
    expect(() =>
      isExpectedOn({ repeat: 'every_n_days', intervalDays: 1, startDate: start }, start),
    ).toThrow(RangeError);
    expect(() =>
      isExpectedOn({ repeat: 'n_per_week', timesPerWeek: 8, startDate: start }, start),
    ).toThrow(RangeError);
    expect(() => isExpectedOn({ repeat: 'daily', startDate: start }, '2026-02-30')).toThrow(
      RangeError,
    );
  });
});

describe('weekRangeFor', () => {
  it('uses the user’s own first day of the week', () => {
    // Thursday 2026-01-15
    expect(weekRangeFor('2026-01-15', 6)).toEqual({ start: '2026-01-10', end: '2026-01-16' }); // Sat
    expect(weekRangeFor('2026-01-15', 1)).toEqual({ start: '2026-01-12', end: '2026-01-18' }); // Mon
    expect(weekRangeFor('2026-01-15', 4)).toEqual({ start: '2026-01-15', end: '2026-01-21' }); // Thu
  });

  it('crosses a year boundary', () => {
    expect(weekRangeFor('2026-01-01', 6)).toEqual({ start: '2025-12-27', end: '2026-01-02' });
  });

  it('throws on an out-of-range weekStart', () => {
    expect(() => weekRangeFor('2026-01-15', 7)).toThrow(RangeError);
  });
});
