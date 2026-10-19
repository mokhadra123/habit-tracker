import {
  type CalendarDate,
  type DayLog,
  type DayRule,
  type LogStatus,
  type ScheduleRule,
  type Streak,
  type StreakSettings,
  type WeekRule,
} from '../types/domain.types';
import { addDays, toCalendarDate, toUtcDate } from './calendarDate';
import { isExpectedOn, weekRangeFor } from './schedule';

/**
 * How many expected days (or weeks, for n_per_week) in a row the habit was
 * kept, forgiving up to `allowedMissesPerWeek` misses in each week (FR-2.4).
 *
 * Derived on every read, never stored: a backfill (FR-2.2) can join two
 * streaks into one, and only a full recount gets that right.
 *
 * @throws RangeError on a malformed date or an out-of-range rule or setting.
 *
 * @example
 * // daily, 1 miss allowed, weeks start Saturday. Misses on Mon and Wed:
 * // Sat ✓ Sun ✓ Mon — Tue ✓ Wed — Thu ✓ Fri(today) ?
 * computeStreak(rule, logs, '2026-10-23', { weekStart: 6, allowedMissesPerWeek: 1 });
 * → { unit: 'day', count: 1 }   (Wed is the week's 2nd miss, so only Thu counts)
 */
export function computeStreak(
  rule: ScheduleRule,
  logs: DayLog[],
  today: CalendarDate,
  settings: StreakSettings,
): Streak {
  const { allowedMissesPerWeek } = settings;
  if (
    !Number.isInteger(allowedMissesPerWeek) ||
    allowedMissesPerWeek < 0 ||
    allowedMissesPerWeek > 7
  ) {
    throw new RangeError(
      `settings.allowedMissesPerWeek must be an integer 0-7, received ${String(allowedMissesPerWeek)}`,
    );
  }

  if (rule.repeat === 'n_per_week') {
    return weekStreak(rule, logs, today, settings);
  }
  return dayStreak(rule, logs, today, settings);
}

/**
 * Replays the history FORWARD from startDate. Walking back from today would
 * forgive the wrong miss: the allowance covers the first misses of a week,
 * and only a forward pass meets those first.
 */
function dayStreak(
  rule: DayRule,
  logs: DayLog[],
  today: CalendarDate,
  settings: StreakSettings,
): Streak {
  const start = toUtcDate(rule.startDate, 'rule.startDate');
  const end = toUtcDate(today, 'today');
  // Built once: logs.find() inside the loop would make this O(n²).
  const statusByDate = new Map<CalendarDate, LogStatus>(logs.map((log) => [log.date, log.status]));

  let count = 0;
  let missesThisWeek = 0;
  let currentWeek = '';

  for (let day = start; day.getTime() <= end.getTime(); day = addDays(day, 1)) {
    const date = toCalendarDate(day);

    // The allowance belongs to the week, not to the streak: it refills when
    // a new week starts, never because the streak broke.
    const week = weekRangeFor(date, settings.weekStart).start;
    if (week !== currentWeek) {
      currentWeek = week;
      missesThisWeek = 0;
    }

    // Always unit 'day' for these rules; the unit check only narrows the type.
    // A log on a day that wasn't expected doesn't count either way.
    const expectation = isExpectedOn(rule, date);
    if (expectation.unit !== 'day' || !expectation.expected) {
      continue;
    }

    const status = statusByDate.get(date);
    if (status === 'done' || status === 'partial') {
      // partial is effort, not failure (P6).
      count++;
    } else if (status === undefined && date !== today) {
      // No row on an expected day IS the miss — misses are never stored.
      missesThisWeek++;
      if (missesThisWeek > settings.allowedMissesPerWeek) {
        count = 0;
      }
    }
    // skipped (FR-2.5) and today without a log (the day isn't over) change nothing.
  }

  return { unit: 'day', count };
}

/**
 * n_per_week has no expected DAYS (FR-1.4), so the verdict is per week: each
 * skip lowers what the week owes, and whatever of it wasn't done is a miss.
 * Groups the logs by week once, then judges the weeks in order.
 */
function weekStreak(
  rule: WeekRule,
  logs: DayLog[],
  today: CalendarDate,
  settings: StreakSettings,
): Streak {
  const { timesPerWeek } = rule;
  if (!Number.isInteger(timesPerWeek) || timesPerWeek < 1 || timesPerWeek > 7) {
    throw new RangeError(
      `rule.timesPerWeek must be an integer 1-7, received ${String(timesPerWeek)}`,
    );
  }
  // Validated first, so the string comparisons below can trust the format:
  // 'YYYY-MM-DD' sorts exactly like the dates it names.
  toUtcDate(rule.startDate, 'rule.startDate');
  toUtcDate(today, 'today');
  if (today < rule.startDate) {
    return { unit: 'week', count: 0 };
  }

  // GROUP BY week, in the user's own week (users.week_start), not ISO Monday.
  const byWeek = new Map<CalendarDate, { completions: number; skips: number }>();
  for (const log of logs) {
    if (log.date < rule.startDate || log.date > today) {
      continue;
    }
    const week = weekRangeFor(log.date, settings.weekStart).start;
    const bucket = byWeek.get(week) ?? { completions: 0, skips: 0 };
    if (log.status === 'skipped') {
      bucket.skips++;
    } else {
      // partial is effort, not failure (P6).
      bucket.completions++;
    }
    byWeek.set(week, bucket);
  }

  const firstWeek = weekRangeFor(rule.startDate, settings.weekStart).start;
  const currentWeek = weekRangeFor(today, settings.weekStart).start;

  let count = 0;
  for (
    let day = toUtcDate(firstWeek, 'firstWeek');
    toCalendarDate(day) <= currentWeek;
    day = addDays(day, 7)
  ) {
    const week = toCalendarDate(day);
    const { completions, skips } = byWeek.get(week) ?? { completions: 0, skips: 0 };
    const owed = Math.max(0, timesPerWeek - skips);
    const misses = Math.max(0, owed - completions);

    const isOver = week !== currentWeek;
    // A week that began before startDate is the habit's first, partial week.
    const isFullWeek = week >= rule.startDate;

    // `completions > 0`: an all-skipped week owes nothing, but did nothing
    // either, so it must stay neutral like a skipped day.
    if (completions > 0 && completions >= owed) {
      count++;
    } else if (isOver && isFullWeek && misses > settings.allowedMissesPerWeek) {
      count = 0;
    }
    // Anything else changes nothing: the current week isn't over, a partial
    // first week can't be failed, and the allowance covered the rest.
  }

  return { unit: 'week', count };
}
