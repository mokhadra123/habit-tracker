-- =====================================================================
--  SEED DATA — habit tracker
--  Generated companion to docs/data-modeling.dbml (that file is the schema
--  source of truth; DBML has no seed syntax, so the rows live here).
--
--  Every row satisfies the CHECK rules documented in the DBML §CHECKS block.
--  Explicit ids are used so the fixtures are stable across reseeds; if the
--  columns become identity/serial, reset the sequences after loading (see
--  the bottom of this file).
-- =====================================================================

BEGIN;

-- 6 users spanning every timezone/DST shape, one OAuth user (no password,
-- david) and one deactivated account (frank, deleted_at set).
-- alice uses week_start=6 (Sat) and day_boundary_hour=4 to exercise FR-1.4/FR-6.5.
INSERT INTO "users" ("id", "username", "email", "password", "role", "timezone", "week_start", "day_boundary_hour", "daily_reminder_budget", "quiet_hours_start", "quiet_hours_end", "is_account_verified", "verification_token", "verification_token_expires_at", "reset_password_token", "reset_password_token_expires_at", "password_changed_at", "profile_image", "created_at", "updated_at", "deleted_at") VALUES
  (1, 'alice', 'alice@example.com', '$2b$10$hashedpasswordplaceholder0001', 'admin', 'Africa/Cairo', 6, 4, 3, '22:00', '07:00', true, NULL, NULL, NULL, NULL, NULL, 'https://i.pravatar.cc/150?img=1', '2026-01-05 09:00:00+02', '2026-01-05 09:00:00+02', NULL),
  (2, 'bob', 'bob@example.com', '$2b$10$hashedpasswordplaceholder0002', 'user', 'Europe/London', 1, 0, 3, NULL, NULL, true, NULL, NULL, 'rst_4b1e7a9c3f', '2026-02-02 12:15:00+00', '2026-01-20 08:00:00+00', 'https://i.pravatar.cc/150?img=2', '2026-01-12 14:30:00+00', '2026-02-02 11:15:00+00', NULL),
  (3, 'candice', 'candice@example.com', '$2b$10$hashedpasswordplaceholder0003', 'user', 'America/New_York', 0, 0, 2, NULL, NULL, false, 'ver_9f3a1c7d2b', '2026-03-01 10:00:00-05', NULL, NULL, NULL, NULL, '2026-02-28 18:45:00-05', '2026-02-28 18:45:00-05', NULL),
  (4, 'david', 'david@example.com', NULL, 'user', 'Asia/Tokyo', 1, 0, 1, '23:00', '06:30', true, NULL, NULL, NULL, NULL, NULL, NULL, '2026-03-10 08:20:00+09', '2026-03-10 08:20:00+09', NULL),
  (5, 'emma', 'emma@example.com', '$2b$10$hashedpasswordplaceholder0005', 'user', 'Australia/Sydney', 1, 0, 3, NULL, NULL, false, 'ver_5c8e4a1f6d', '2026-04-15 12:00:00+10', NULL, NULL, NULL, 'https://i.pravatar.cc/150?img=5', '2026-04-14 21:05:00+10', '2026-04-14 21:05:00+10', NULL),
  (6, 'frank', 'frank@example.com', '$2b$10$hashedpasswordplaceholder0006', 'user', 'Europe/Berlin', 1, 0, 3, NULL, NULL, true, NULL, NULL, NULL, NULL, NULL, NULL, '2026-05-02 16:40:00+02', '2026-06-18 09:12:00+02', '2026-06-18 09:12:00+02');

INSERT INTO "groups" ("id", "group_name", "icon", "owner_id", "invite_code", "max_members", "leaderboard_enabled", "created_at", "updated_at", "deleted_at") VALUES
  (1, 'The Five of Us', '🔥', 1, 'inv_7Ka92mQz4Xr1', 12, false, '2026-05-01 09:00:00+02', '2026-05-01 09:00:00+02', NULL);

INSERT INTO "group_members" ("id", "group_id", "user_id", "role", "joined_at") VALUES
  (1, 1, 1, 'owner', '2026-05-01 09:00:00+02'),
  (2, 1, 2, 'member', '2026-05-01 10:12:00+02'),
  (3, 1, 3, 'member', '2026-05-02 15:40:00+02'),
  (4, 1, 4, 'member', '2026-05-03 08:05:00+02'),
  (5, 1, 5, 'member', '2026-05-04 19:22:00+02');

INSERT INTO "habit_templates" ("id", "template_name", "icon", "color", "description", "habit_type", "target_value", "target_unit", "direction", "repeat_habit", "weekdays", "times_per_week", "interval_days", "created_by_user_id", "group_id", "created_at", "updated_at") VALUES
  (1, 'Drink 8 glasses', '💧', '#3BA3E8', 'Hydration basics', 'numeric', 8, 'glasses', 'building', 'daily', NULL, NULL, NULL, NULL, NULL, '2026-05-01 09:00:00+02', '2026-05-01 09:00:00+02'),
  (2, 'Gym 3x a week', '🏋️', '#E8743B', 'Any three days', 'boolean', NULL, NULL, 'building', 'n_per_week', NULL, 3, NULL, 1, 1, '2026-05-01 09:05:00+02', '2026-05-01 09:05:00+02');

-- Covers every habit_type, every repeat_habit, both visibilities, both
-- directions, one paused habit and one shared group definition (FR-3.8).
INSERT INTO "habits" ("id", "habit_name", "icon", "color", "description", "lifecycle", "direction", "visibility", "repeat_habit", "weekdays", "times_per_week", "interval_days", "start_date", "habit_type", "target_value", "target_unit", "allowed_misses_per_week", "user_id", "group_id", "is_shared_definition", "category_id", "created_from_template_id", "created_at", "updated_at", "deleted_at") VALUES
  (1, 'Drink water', '💧', '#3BA3E8', 'Eight glasses across the day', 'active', 'building', 'group', 'daily', NULL, NULL, NULL, '2026-05-01', 'numeric', 8, 'glasses', 1, 1, 1, false, NULL, NULL, '2026-05-01 09:10:00+02', '2026-05-01 09:10:00+02', NULL),
  (2, 'Gym', '🏋️', '#E8743B', 'Strength session', 'active', 'building', 'group', 'n_per_week', NULL, 3, NULL, '2026-05-01', 'boolean', NULL, NULL, 1, 1, 1, false, NULL, NULL, '2026-05-01 09:12:00+02', '2026-05-01 09:12:00+02', NULL),
  (3, 'Read', '📚', '#7A5AF8', 'Thirty minutes before bed', 'active', 'building', 'private', 'daily', NULL, NULL, NULL, '2026-05-02', 'duration', 30, 'minutes', 2, 2, 1, false, NULL, NULL, '2026-05-02 21:00:00+01', '2026-05-02 21:00:00+01', NULL),
  (4, 'No smoking', '🚭', '#2FB67C', 'Abstain, every single day', 'active', 'breaking', 'group', 'daily', NULL, NULL, NULL, '2026-05-01', 'boolean', NULL, NULL, 0, 3, 1, false, NULL, NULL, '2026-05-01 12:00:00-04', '2026-05-01 12:00:00-04', NULL),
  (5, 'Deep clean', '🧹', '#F2B705', 'Rotate rooms', 'active', 'building', 'private', 'every_n_days', NULL, NULL, 3, '2026-05-01', 'boolean', NULL, NULL, 1, 4, NULL, false, NULL, NULL, '2026-05-01 08:30:00+09', '2026-05-01 08:30:00+09', NULL),
  (6, 'Stretch', '🧘', '#E85D9B', 'Mon/Wed/Fri only', 'paused', 'building', 'group', 'weekly', '{1,3,5}'::smallint[], NULL, NULL, '2026-05-01', 'duration', 15, 'minutes', 1, 5, 1, false, NULL, NULL, '2026-05-01 07:00:00+10', '2026-06-01 07:00:00+10', NULL),
  (7, 'Group steps', '👟', '#00A6A6', 'We all walk 8k', 'active', 'building', 'group', 'daily', NULL, NULL, NULL, '2026-05-10', 'numeric', 8000, 'steps', 1, 1, 1, true, NULL, NULL, '2026-05-10 09:00:00+02', '2026-05-10 09:00:00+02', NULL);

-- Habit 6 is paused open-ended; its lifecycle column is the cache of this row.
INSERT INTO "habit_pauses" ("id", "habit_id", "start_date", "end_date", "reason", "created_at") VALUES
  (1, 6, '2026-06-01', NULL, 'Shoulder injury', '2026-06-01 07:00:00+10');

-- Alice's water habit (id 1), 2026-05-01..07:
--   done, done, partial(5/8), skipped, done, <NO ROW = miss>, done
-- The skip leaves 6 expected days; credit is 4 + 5/8 = 4.625 -> 77.1%.
-- 2026-05-06 is deliberately absent: a miss is DERIVED, never stored.
-- Log 9 belongs to a PRIVATE habit and must never reach the group feed.
-- Log 10 is backfilled: log_date 05-04 but created_at 05-06 (FR-2.2).
-- Logs 11/12 are two users logging the same shared habit row (FR-3.8).
INSERT INTO "habit_logs" ("id", "habit_id", "user_id", "log_date", "status", "value", "note", "photo_url", "created_at", "updated_at") VALUES
  (1, 1, 1, '2026-05-01', 'done', 8, NULL, NULL, '2026-05-01 21:40:00+02', '2026-05-01 21:40:00+02'),
  (2, 1, 1, '2026-05-02', 'done', 8, NULL, NULL, '2026-05-02 22:05:00+02', '2026-05-02 22:05:00+02'),
  (3, 1, 1, '2026-05-03', 'partial', 5, 'Long day out', NULL, '2026-05-03 23:30:00+02', '2026-05-03 23:30:00+02'),
  (4, 1, 1, '2026-05-04', 'skipped', NULL, 'Food poisoning', NULL, '2026-05-04 11:00:00+02', '2026-05-04 11:00:00+02'),
  (5, 1, 1, '2026-05-05', 'done', 8, NULL, NULL, '2026-05-05 20:15:00+02', '2026-05-05 20:15:00+02'),
  (6, 1, 1, '2026-05-07', 'done', 8, NULL, NULL, '2026-05-07 19:50:00+02', '2026-05-07 19:50:00+02'),
  (7, 2, 1, '2026-05-02', 'done', NULL, NULL, NULL, '2026-05-02 18:00:00+02', '2026-05-02 18:00:00+02'),
  (8, 2, 1, '2026-05-05', 'done', NULL, NULL, 'https://cdn.example.com/p/9f2a.jpg', '2026-05-05 18:30:00+02', '2026-05-05 18:30:00+02'),
  (9, 3, 2, '2026-05-03', 'partial', 18, 'Fell asleep', NULL, '2026-05-03 23:10:00+01', '2026-05-03 23:10:00+01'),
  (10, 4, 3, '2026-05-04', 'done', NULL, 'Backfilled', NULL, '2026-05-06 09:00:00-04', '2026-05-06 09:00:00-04'),
  (11, 7, 1, '2026-05-10', 'done', 8420, NULL, NULL, '2026-05-10 21:00:00+02', '2026-05-10 21:00:00+02'),
  (12, 7, 2, '2026-05-10', 'partial', 6100, NULL, NULL, '2026-05-10 22:15:00+01', '2026-05-10 22:15:00+01');

-- Only on logs of habits with visibility='group'. Nothing reacts to log 9
-- (private habit) — that would be the privacy leak described in the model.
INSERT INTO "reactions" ("id", "habit_log_id", "user_id", "kind", "created_at") VALUES
  (1, 1, 2, 'fire', '2026-05-01 22:00:00+01'),
  (2, 1, 3, 'clap', '2026-05-02 01:10:00-04'),
  (3, 3, 2, 'heart', '2026-05-04 08:00:00+01'),
  (4, 8, 4, 'muscle', '2026-05-05 20:00:00+09'),
  (5, 11, 3, 'star', '2026-05-11 07:30:00-04');

-- Reminder 2 has consecutive_ignores=4 and last_decayed_at set: FR-4.4 fired.
INSERT INTO "reminders" ("id", "habit_id", "user_id", "remind_at", "is_enabled", "consecutive_ignores", "last_sent_at", "last_decayed_at", "created_at", "updated_at") VALUES
  (1, 1, 1, '09:00', true, 0, '2026-05-07 09:00:00+02', NULL, '2026-05-01 09:15:00+02', '2026-05-07 09:00:00+02'),
  (2, 2, 1, '17:30', true, 4, '2026-05-07 17:30:00+02', '2026-05-07 17:30:00+02', '2026-05-01 09:16:00+02', '2026-05-07 17:30:00+02'),
  (3, 3, 2, '21:30', false, 0, NULL, NULL, '2026-05-02 21:05:00+01', '2026-05-02 21:05:00+01');

INSERT INTO "nudges" ("id", "group_id", "from_user_id", "to_user_id", "created_at") VALUES
  (1, 1, 1, 5, '2026-06-10 10:00:00+02');

INSERT INTO "weekly_reviews" ("id", "user_id", "week_start_date", "what_worked", "what_did_not_work", "one_adjustment", "created_at", "updated_at") VALUES
  (1, 1, '2026-05-04', 'Water is automatic now', 'Gym slipped on the weekend', 'Move gym to mornings', '2026-05-10 20:00:00+02', '2026-05-10 20:00:00+02');

-- --------------------------------------------------------------------
-- If the primary keys are identity/serial columns, realign the sequences
-- so the next application INSERT does not collide with these fixtures:
-- --------------------------------------------------------------------
SELECT setval(pg_get_serial_sequence('users','id'), COALESCE((SELECT MAX(id) FROM "users"), 1), true);
SELECT setval(pg_get_serial_sequence('groups','id'), COALESCE((SELECT MAX(id) FROM "groups"), 1), true);
SELECT setval(pg_get_serial_sequence('group_members','id'), COALESCE((SELECT MAX(id) FROM "group_members"), 1), true);
SELECT setval(pg_get_serial_sequence('habit_templates','id'), COALESCE((SELECT MAX(id) FROM "habit_templates"), 1), true);
SELECT setval(pg_get_serial_sequence('habits','id'), COALESCE((SELECT MAX(id) FROM "habits"), 1), true);
SELECT setval(pg_get_serial_sequence('habit_pauses','id'), COALESCE((SELECT MAX(id) FROM "habit_pauses"), 1), true);
SELECT setval(pg_get_serial_sequence('habit_logs','id'), COALESCE((SELECT MAX(id) FROM "habit_logs"), 1), true);
SELECT setval(pg_get_serial_sequence('reactions','id'), COALESCE((SELECT MAX(id) FROM "reactions"), 1), true);
SELECT setval(pg_get_serial_sequence('reminders','id'), COALESCE((SELECT MAX(id) FROM "reminders"), 1), true);
SELECT setval(pg_get_serial_sequence('nudges','id'), COALESCE((SELECT MAX(id) FROM "nudges"), 1), true);
SELECT setval(pg_get_serial_sequence('weekly_reviews','id'), COALESCE((SELECT MAX(id) FROM "weekly_reviews"), 1), true);

COMMIT;
