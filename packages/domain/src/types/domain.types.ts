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
