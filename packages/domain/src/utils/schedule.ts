import {
  type CalendarDate,
  type Expectation,
  type ScheduleRule,
  type WeekRange,
} from '../types/domain.types';
import { toUtcDate, toCalendarDate, addDays } from './calendarDate';

const MS_PER_DAY = 86_400_000;

function assertWeekday(value: number, label: string): void {
  if (!Number.isInteger(value) || value < 0 || value > 6) {
    throw new RangeError(`${label} must be an integer 0-6 (0=Sunday), received ${String(value)}`);
  }
}

/**
 * Was this habit's rule expecting something on this day?
 *
 * Knows nothing about logs or about the habit's lifecycle: a paused or
 * archived habit is the caller's business. This answers about the RULE only,
 * which is what keeps the answer stable — editing a past log can never change
 * which days were expected.
 *
 * @throws RangeError on a malformed date or an out-of-range rule.
 *
 * @example
 * isExpectedOn({ repeat: 'every_n_days', intervalDays: 3, startDate: '2026-01-01' }, '2026-01-08');
 * → { unit: 'day', expected: false }   (7 days in, 7 % 3 !== 0)
 */
export function isExpectedOn(rule: ScheduleRule, date: CalendarDate): Expectation {
  const day = toUtcDate(date, 'date');
  const start = toUtcDate(rule.startDate, 'rule.startDate');
  const started = day.getTime() >= start.getTime();

  switch (rule.repeat) {
    case 'daily':
      return { unit: 'day', expected: started };

    case 'weekly': {
      if (rule.weekdays.length === 0) {
        throw new RangeError('rule.weekdays must contain at least one weekday');
      }
      for (const weekday of rule.weekdays) {
        assertWeekday(weekday, 'rule.weekdays');
      }
      return { unit: 'day', expected: started && rule.weekdays.includes(day.getUTCDay()) };
    }

    case 'every_n_days': {
      if (!Number.isInteger(rule.intervalDays) || rule.intervalDays < 2) {
        throw new RangeError(
          `rule.intervalDays must be an integer >= 2, received ${String(rule.intervalDays)}`,
        );
      }
      // Anchored to startDate, NOT to the last completion: a verdict about the
      // past must not change when an old log is edited.
      const elapsed = (day.getTime() - start.getTime()) / MS_PER_DAY;
      return { unit: 'day', expected: started && elapsed % rule.intervalDays === 0 };
    }

    case 'n_per_week': {
      if (!Number.isInteger(rule.timesPerWeek) || rule.timesPerWeek < 1 || rule.timesPerWeek > 7) {
        throw new RangeError(
          `rule.timesPerWeek must be an integer 1-7, received ${String(rule.timesPerWeek)}`,
        );
      }
      // The week is the unit, so the target is the same on every day of it.
      // Whether a partial first week still owes the full target is a product
      // decision, and it belongs to the caller that counts logs.
      return { unit: 'week', target: started ? rule.timesPerWeek : 0 };
    }

    default: {
      // Compile-time exhaustiveness: adding a fifth repeat mode breaks the
      // build here instead of silently returning nothing at runtime.
      const unhandled: never = rule;
      throw new RangeError(`Unknown repeat mode: ${JSON.stringify(unhandled)}`);
    }
  }
}

/**
 * The calendar week containing `date`, using the user's own first day of the
 * week (users.week_start). Both ends inclusive.
 *
 * This boundary is where the n_per_week quota and the allowed-misses window
 * reset (FR-1.4 / FR-2.4), so a wrong boundary makes every streak wrong for
 * anyone whose week doesn't start on Monday.
 *
 * @example
 * weekRangeFor('2026-01-15', 6); // week starting Saturday
 */
export function weekRangeFor(date: CalendarDate, weekStart: number): WeekRange {
  assertWeekday(weekStart, 'weekStart');
  const day = toUtcDate(date, 'date');

  const offset = (day.getUTCDay() - weekStart + 7) % 7;
  const start = addDays(day, -offset);

  return { start: toCalendarDate(start), end: toCalendarDate(addDays(start, 6)) };
}
