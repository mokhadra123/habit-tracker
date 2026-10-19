import type { CalendarDate } from '../types/domain.types';

export const CALENDAR_DATE = /^\d{4}-\d{2}-\d{2}$/;

/**
 * Parse 'YYYY-MM-DD' into UTC midnight. UTC only: it has no DST, so every day
 * is exactly 24 hours and date arithmetic can't drift.
 */
export function toUtcDate(value: CalendarDate, label: string): Date {
  if (!CALENDAR_DATE.test(value)) {
    throw new RangeError(`${label} must look like YYYY-MM-DD, received "${value}"`);
  }
  const year = Number(value.slice(0, 4));
  const month = Number(value.slice(5, 7));
  const day = Number(value.slice(8, 10));
  const utc = new Date(Date.UTC(year, month - 1, day));

  // Date.UTC silently rolls impossible dates over (Feb 30 -> Mar 2), so the
  // only reliable check is formatting it back and comparing.
  if (toCalendarDate(utc) !== value) {
    throw new RangeError(`${label} is not a real calendar date: "${value}"`);
  }
  return utc;
}

export function toCalendarDate(utc: Date): CalendarDate {
  return utc.toISOString().slice(0, 10);
}
/** Calendar arithmetic, never hours: Date.UTC rolls months and years over. */
export function addDays(utc: Date, days: number): Date {
  return new Date(Date.UTC(utc.getUTCFullYear(), utc.getUTCMonth(), utc.getUTCDate() + days));
}
