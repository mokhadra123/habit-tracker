-- CHECK constraints from docs/data-modeling.dbml (§CHECKS), MVP columns only.
-- Prisma's schema language can't express CHECKs, so this migration is
-- written by hand.
--
-- Deliberately NOT here:
--   ck_users_reminder_budget, ck_users_quiet_hours, ck_habits_shared
--       their columns arrive in v1.1.
--   ck_logs_not_future
--       uses current_date: not immutable, and evaluated in the server's time
--       zone. The service validates the date instead.
--   "a boolean habit can't be partial", "value >= target_value"
--       need columns from "habits"; a CHECK can only see its own row.
--   no duplicate weekdays
--       needs a subquery, which a CHECK can't contain. The service dedupes.
--
-- Every rule spells out IS NULL / IS NOT NULL on purpose: a CHECK whose
-- expression evaluates to NULL counts as passing.

-- users -------------------------------------------------------------------

ALTER TABLE "users"
  ADD CONSTRAINT "ck_users_week_start"
  CHECK ("week_start" >= 0 AND "week_start" <= 6);

ALTER TABLE "users"
  ADD CONSTRAINT "ck_users_day_boundary"
  CHECK ("day_boundary_hour" >= 0 AND "day_boundary_hour" <= 23);

-- groups ------------------------------------------------------------------

ALTER TABLE "groups"
  ADD CONSTRAINT "ck_groups_max_members"
  CHECK ("max_members" >= 2 AND "max_members" <= 12);

-- habits ------------------------------------------------------------------

-- Exactly one schedule shape per repeat mode. An empty weekdays array counts
-- as "no weekdays", so it doesn't matter whether a client writes NULL or '{}'.
ALTER TABLE "habits"
  ADD CONSTRAINT "ck_habits_schedule"
  CHECK (
    (
      "repeat_habit" = 'daily'
      AND ("weekdays" IS NULL OR cardinality("weekdays") = 0)
      AND "times_per_week" IS NULL
      AND "interval_days" IS NULL
    )
    OR (
      "repeat_habit" = 'weekly'
      AND "weekdays" IS NOT NULL AND cardinality("weekdays") BETWEEN 1 AND 7
      AND "times_per_week" IS NULL
      AND "interval_days" IS NULL
    )
    OR (
      "repeat_habit" = 'n_per_week'
      AND ("weekdays" IS NULL OR cardinality("weekdays") = 0)
      AND "times_per_week" IS NOT NULL AND "times_per_week" BETWEEN 1 AND 7
      AND "interval_days" IS NULL
    )
    OR (
      "repeat_habit" = 'every_n_days'
      AND ("weekdays" IS NULL OR cardinality("weekdays") = 0)
      AND "times_per_week" IS NULL
      AND "interval_days" IS NOT NULL AND "interval_days" >= 2
    )
  );

-- Weekday values are 0=Sun .. 6=Sat. How many are allowed is decided by
-- ck_habits_schedule above.
ALTER TABLE "habits"
  ADD CONSTRAINT "ck_habits_weekdays"
  CHECK (
    "weekdays" IS NULL
    OR "weekdays" <@ ARRAY[0, 1, 2, 3, 4, 5, 6]::smallint[]
  );

ALTER TABLE "habits"
  ADD CONSTRAINT "ck_habits_measure"
  CHECK (
    (
      "habit_type" = 'boolean'
      AND "target_value" IS NULL
      AND "target_unit" IS NULL
    )
    OR (
      "habit_type" IN ('numeric', 'duration')
      AND "target_value" IS NOT NULL AND "target_value" > 0
      AND "target_unit" IS NOT NULL
    )
  );

ALTER TABLE "habits"
  ADD CONSTRAINT "ck_habits_misses"
  CHECK ("allowed_misses_per_week" >= 0 AND "allowed_misses_per_week" <= 7);

-- habit_logs --------------------------------------------------------------

-- The part of the status/value matrix this row can check on its own:
--   skipped    -> no value
--   any value  -> positive (partial is > 0; done is >= target_value > 0)
ALTER TABLE "habit_logs"
  ADD CONSTRAINT "ck_logs_status_value"
  CHECK (
    ("status" <> 'skipped' OR "value" IS NULL)
    AND ("value" IS NULL OR "value" > 0)
  );
