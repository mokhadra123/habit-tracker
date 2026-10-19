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

/** The rules judged day by day. */
export type DayRule = Exclude<ScheduleRule, { repeat: 'n_per_week' }>;
/** The rule judged week by week (FR-1.4: it has no expected days). */
export type WeekRule = Extract<ScheduleRule, { repeat: 'n_per_week' }>;

/** Both ends inclusive. */
export type WeekRange = { start: CalendarDate; end: CalendarDate };

export type LogStatus = 'done' | 'partial' | 'skipped';

/**
 * One habit_logs row as the domain sees it — what validateLog checks, the
 * streak counts and consistency weighs. `value` is NULL for boolean habits
 * and for skipped.
 */
export type DayLog = { date: CalendarDate; status: LogStatus; value: number | null };

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

export type ConsistencySettings = {
  // users.week_start: n_per_week is judged in whole weeks.
  weekStart: number;
  // habits.target_value: weighs a partial log (5 of 8 counts 0.625). NULL for boolean.
  targetValue: number | null;
  // 'rolling': the last 30 days, or the last 4 complete weeks for n_per_week (FR-2.3).
  // 'lifetime': everything since startDate, for the re-entry view (FR-2.7).
  window: 'rolling' | 'lifetime';
};
