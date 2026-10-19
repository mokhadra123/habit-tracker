// A calendar date with no time and no time zone, e.g. '2026-01-15'.
export type CalendarDate = string;

export type ScheduleRule = {
  startDate: CalendarDate;
} & (
  | { repeat: 'daily' }
  | { repeat: 'weekly'; weekdays: number[] }
  | { repeat: 'every_n_days'; intervalDays: number }
  | { repeat: 'n_per_week'; timesPerWeek: number }
);

/**
 * What a schedule expects, in the unit the schedule actually uses.
 *
 * `n_per_week` deliberately has no per-day answer (FR-1.4: it must not care
 * WHICH days), so a boolean would have to lie. The unit depends only on the
 * rule, never on the date being asked about.
 */
export type Expectation = { unit: 'day'; expected: boolean } | { unit: 'week'; target: number };

/** Both ends inclusive. */
export type WeekRange = { start: CalendarDate; end: CalendarDate };

export type LogStatus = 'done' | 'partial' | 'skipped';
export type DayLog = { date: CalendarDate; status: LogStatus };

export type StreakSettings = {
  weekStart: number;
  allowedMissesPerWeek: number; // habits.allowed_misses_per_week
};

export type Streak = { unit: 'day' | 'week'; count: number };

// `duration` arrives in v1.1 (the API rejects it until then); its log rules match numeric.
export type HabitType = 'boolean' | 'numeric' | 'duration';

/** The habit fields a log is checked against. */
export type HabitForLog = {
  habitType: HabitType;
  // NULL for boolean; > 0 for numeric and duration (ck_habits_measure).
  targetValue: number | null;
  startDate: CalendarDate;
};

export type LogInput = { date: CalendarDate; status: LogStatus; value: number | null };

/** Why a log was refused. Codes, not messages: the API and the web choose the words. */
export type LogRejection =
  | 'future_date'
  | 'outside_edit_window'
  | 'before_start'
  | 'partial_on_boolean'
  | 'value_not_allowed'
  | 'value_required'
  | 'done_below_target'
  | 'partial_reaches_target';

export type LogValidation = { ok: true } | { ok: false; reason: LogRejection };
