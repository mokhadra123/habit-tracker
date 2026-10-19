import {
  type CalendarDate,
  type ConsistencySettings,
  type DayLog,
  type DayRule,
  type ScheduleRule,
  type WeekRule,
} from '../types/domain.types';
import { addDays, toCalendarDate, toUtcDate } from './calendarDate';
import { isExpectedOn, weekRangeFor } from './schedule';

/** FR-2.3: the rolling window, in days. */
const ROLLING_DAYS = 30;
/** n_per_week has no expected days, so its rolling window is whole weeks. */
const ROLLING_WEEKS = 4;

type Tally = { numerator: number; denominator: number };

/**
 * The headline metric (FR-2.3): how much of what the schedule asked for was
 * done, as a ratio 0..1. Unlike the streak it degrades gently: one miss in a
 * month moves 1 to ~0.97, never to 0.
 *
 * - done            -> 1 of 1
 * - partial         -> value / targetValue of 1 (5 of 8 glasses = 0.625)
 * - skipped         -> left out of both sides (FR-2.5)
 * - no log          -> 0 of 1: the miss, derived, never stored
 * - today, no log   -> left out: the day isn't over
 *
 * Returns null when nothing has been asked for yet (a habit started today, or
 * a fully skipped window): 0% would read as failure for a habit that has had
 * no chance to fail (principle 2).
 *
 * Partials are weighed against the CURRENT targetValue, so raising the target
 * lowers old partials. Accepted: `done` stays frozen, and that is what counts.
 *
 * @throws RangeError on a malformed date or rule, or a partial with no amount.
 *
 * @example
 * // daily, the last 30 days: 28 done, 1 missed, today not logged yet
 * consistencyScore(rule, logs, '2026-10-30', { weekStart: 6, targetValue: null, window: 'rolling' });
 * → 0.9655…   (28 / 29)
 */
export function consistencyScore(
  rule: ScheduleRule,
  logs: DayLog[],
  today: CalendarDate,
  settings: ConsistencySettings,
): number | null {
  // Validated first, so the string comparisons below can trust the format.
  toUtcDate(rule.startDate, 'rule.startDate');
  toUtcDate(today, 'today');
  if (today < rule.startDate) {
    return null;
  }

  const { numerator, denominator } =
    rule.repeat === 'n_per_week'
      ? weekTally(rule, logs, today, settings)
      : dayTally(rule, logs, today, settings);

  return denominator === 0 ? null : numerator / denominator;
}

function dayTally(
  rule: DayRule,
  logs: DayLog[],
  today: CalendarDate,
  settings: ConsistencySettings,
): Tally {
  const end = toUtcDate(today, 'today');
  const habitStart = toUtcDate(rule.startDate, 'rule.startDate');
  const rollingStart = addDays(end, -(ROLLING_DAYS - 1));
  const start =
    settings.window === 'lifetime' || rollingStart.getTime() < habitStart.getTime()
      ? habitStart
      : rollingStart;
  // Built once: logs.find() inside the loop would make this O(n²).
  const logByDate = new Map(logs.map((log) => [log.date, log]));

  let numerator = 0;
  let denominator = 0;

  for (let day = start; day.getTime() <= end.getTime(); day = addDays(day, 1)) {
    const date = toCalendarDate(day);

    // Always unit 'day' for these rules; the unit check only narrows the type.
    const expectation = isExpectedOn(rule, date);
    if (expectation.unit !== 'day' || !expectation.expected) {
      continue;
    }

    const log = logByDate.get(date);
    if (log === undefined) {
      if (date !== today) {
        denominator++;
      }
    } else if (log.status !== 'skipped') {
      numerator += credit(log, settings.targetValue);
      denominator++;
    }
  }

  return { numerator, denominator };
}

/**
 * Judged in whole weeks, like the streak: each skip lowers what a week owes,
 * the current week is left out until it ends, and a first week that began
 * before startDate is left out because it was never a full week.
 */
function weekTally(
  rule: WeekRule,
  logs: DayLog[],
  today: CalendarDate,
  settings: ConsistencySettings,
): Tally {
  const { timesPerWeek } = rule;
  if (!Number.isInteger(timesPerWeek) || timesPerWeek < 1 || timesPerWeek > 7) {
    throw new RangeError(
      `rule.timesPerWeek must be an integer 1-7, received ${String(timesPerWeek)}`,
    );
  }

  const currentWeek = toUtcDate(weekRangeFor(today, settings.weekStart).start, 'currentWeek');
  const startWeek = weekRangeFor(rule.startDate, settings.weekStart).start;

  let first = toUtcDate(startWeek, 'startWeek');
  if (startWeek < rule.startDate) {
    first = addDays(first, 7);
  }
  if (settings.window === 'rolling') {
    const rollingFirst = addDays(currentWeek, -7 * ROLLING_WEEKS);
    if (rollingFirst.getTime() > first.getTime()) {
      first = rollingFirst;
    }
  }

  // GROUP BY week, in the user's own week (users.week_start), not ISO Monday.
  const byWeek = new Map<CalendarDate, { credits: number; skips: number }>();
  for (const log of logs) {
    if (log.date < rule.startDate || log.date > today) {
      continue;
    }
    const week = weekRangeFor(log.date, settings.weekStart).start;
    const bucket = byWeek.get(week) ?? { credits: 0, skips: 0 };
    if (log.status === 'skipped') {
      bucket.skips++;
    } else {
      bucket.credits += credit(log, settings.targetValue);
    }
    byWeek.set(week, bucket);
  }

  let numerator = 0;
  let denominator = 0;

  for (let day = first; day.getTime() < currentWeek.getTime(); day = addDays(day, 7)) {
    const { credits, skips } = byWeek.get(toCalendarDate(day)) ?? { credits: 0, skips: 0 };
    const owed = Math.max(0, timesPerWeek - skips);
    // Doing more than a week owes doesn't make up for another week.
    numerator += Math.min(owed, credits);
    denominator += owed;
  }

  return { numerator, denominator };
}

/** How much one done/partial log fulfils: done is whole, partial is its share. */
function credit(log: DayLog, targetValue: number | null): number {
  if (log.status === 'done') {
    return 1;
  }
  if (log.value === null || targetValue === null || !(targetValue > 0)) {
    // validateLog never lets such a partial in, so reaching here is a bug.
    throw new RangeError(
      `the partial log on ${log.date} needs a value and a target > 0 to be weighed`,
    );
  }
  return Math.min(1, log.value / targetValue);
}
