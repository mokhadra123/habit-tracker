import { describe, expect, it } from 'vitest';
import { resolveLogDate } from './resolveLogDate';

describe('resolveLogDate', () => {
  it('uses the user’s calendar day, not the UTC one', () => {
    // 00:30 in Cairo (UTC+2 in January) is still 22:30 the day before in UTC.
    expect(resolveLogDate(new Date('2026-01-15T22:30:00Z'), 'Africa/Cairo')).toBe('2026-01-16');
    expect(resolveLogDate(new Date('2026-01-15T22:30:00Z'), 'UTC')).toBe('2026-01-15');
  });

  it('credits the hours before dayBoundaryHour to yesterday (FR-6.5)', () => {
    // 03:00 Cairo with a 04:00 boundary is still "last night".
    expect(resolveLogDate(new Date('2026-01-16T01:00:00Z'), 'Africa/Cairo', 4)).toBe('2026-01-15');
    // 04:00 Cairo is the new day.
    expect(resolveLogDate(new Date('2026-01-16T02:00:00Z'), 'Africa/Cairo', 4)).toBe('2026-01-16');
  });

  it('rolls back across a month and a year', () => {
    expect(resolveLogDate(new Date('2026-01-01T01:00:00Z'), 'UTC', 4)).toBe('2025-12-31');
  });

  it('throws on input that can only be a bug', () => {
    expect(() => resolveLogDate(new Date('nope'), 'UTC')).toThrow(RangeError);
    expect(() => resolveLogDate(new Date(), 'Mars/Olympus')).toThrow(RangeError);
    expect(() => resolveLogDate(new Date(), 'UTC', 24)).toThrow(RangeError);
  });
});
