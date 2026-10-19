import {
  type CalendarDate,
  type HabitForLog,
  type LogInput,
  type LogValidation,
} from '../types/domain.types';
import { addDays, toCalendarDate, toUtcDate } from './calendarDate';

/** FR-2.2: today plus the 6 days before it. */
const EDIT_WINDOW_DAYS = 7;

/**
 * May this log be written for this habit? Covers what Postgres can't check:
 * a CHECK sees only its own row (never habits.target_value), and its
 * current_date runs in the server's time zone, not the user's.
 *
 * A rejection is the USER's mistake, so it comes back as a code for the API
 * (422) and the web (wording) to translate. A malformed date is OUR bug —
 * the request schema should have stopped it — so that still throws.
 *
 * `today` must come from resolveLogDate on the server, never from the
 * request: a client that picks its own "today" can dodge the future rule.
 *
 * Logging on a day the schedule didn't expect is allowed on purpose: it shows
 * in the heatmap and simply doesn't count toward the streak (principle 2).
 *
 * @throws RangeError on a malformed date, or a numeric habit with no target.
 *
 * @example
 * validateLog(
 *   { habitType: 'numeric', targetValue: 8, startDate: '2026-10-01' },
 *   { date: '2026-10-19', status: 'done', value: 5 },
 *   '2026-10-19',
 * );
 * → { ok: false, reason: 'done_below_target' }   (5 of 8 is partial)
 */
export function validateLog(habit: HabitForLog, log: LogInput, today: CalendarDate): LogValidation {
  // Validated first, so the string comparisons below can trust the format.
  toUtcDate(log.date, 'log.date');
  toUtcDate(habit.startDate, 'habit.startDate');
  const firstEditable = toCalendarDate(addDays(toUtcDate(today, 'today'), -(EDIT_WINDOW_DAYS - 1)));

  // --- the date ---
  if (log.date > today) {
    return { ok: false, reason: 'future_date' };
  }
  if (log.date < firstEditable) {
    return { ok: false, reason: 'outside_edit_window' };
  }
  if (log.date < habit.startDate) {
    return { ok: false, reason: 'before_start' };
  }

  // --- the status/value matrix (data-modeling.dbml, habit_logs Note) ---
  if (log.status === 'skipped') {
    return log.value === null ? { ok: true } : { ok: false, reason: 'value_not_allowed' };
  }

  if (habit.habitType === 'boolean') {
    // Binary habits have no middle, and `done` already carries the answer.
    if (log.status === 'partial') {
      return { ok: false, reason: 'partial_on_boolean' };
    }
    return log.value === null ? { ok: true } : { ok: false, reason: 'value_not_allowed' };
  }

  // numeric and duration: done and partial both carry the amount.
  // `!(value > 0)` rather than `value <= 0`: it also catches NaN.
  if (log.value === null || !(log.value > 0)) {
    return { ok: false, reason: 'value_required' };
  }

  const target = habit.targetValue;
  if (target === null || !(target > 0)) {
    // ck_habits_measure guarantees a target, so reaching here is a bug.
    throw new RangeError(
      `habit.targetValue must be > 0 for a ${habit.habitType} habit, received ${String(target)}`,
    );
  }

  if (log.status === 'done') {
    return log.value >= target ? { ok: true } : { ok: false, reason: 'done_below_target' };
  }
  return log.value < target ? { ok: true } : { ok: false, reason: 'partial_reaches_target' };
}
