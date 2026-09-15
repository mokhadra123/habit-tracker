-- CreateEnum
CREATE TYPE "user_role" AS ENUM ('user', 'admin');

-- CreateEnum
CREATE TYPE "group_member_role" AS ENUM ('owner', 'member');

-- CreateEnum
CREATE TYPE "habit_repeat" AS ENUM ('daily', 'weekly', 'n_per_week', 'every_n_days');

-- CreateEnum
CREATE TYPE "habit_lifecycle" AS ENUM ('active', 'paused', 'archived');

-- CreateEnum
CREATE TYPE "habit_type" AS ENUM ('boolean', 'numeric', 'duration');

-- CreateEnum
CREATE TYPE "habit_direction" AS ENUM ('building', 'breaking');

-- CreateEnum
CREATE TYPE "habit_visibility" AS ENUM ('private', 'group');

-- CreateEnum
CREATE TYPE "habit_log_status" AS ENUM ('done', 'partial', 'skipped');

-- CreateEnum
CREATE TYPE "reaction_kind" AS ENUM ('fire', 'muscle', 'clap', 'heart', 'star');

-- CreateTable
CREATE TABLE "users" (
    "id" UUID NOT NULL,
    "username" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "password" TEXT,
    "role" "user_role" NOT NULL DEFAULT 'user',
    "timezone" TEXT NOT NULL,
    "week_start" SMALLINT NOT NULL DEFAULT 1,
    "day_boundary_hour" SMALLINT NOT NULL DEFAULT 0,
    "is_account_verified" BOOLEAN NOT NULL DEFAULT false,
    "verification_token" TEXT,
    "verification_token_expires_at" TIMESTAMPTZ,
    "reset_password_token" TEXT,
    "reset_password_token_expires_at" TIMESTAMPTZ,
    "password_changed_at" TIMESTAMPTZ,
    "profile_image" TEXT,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" TIMESTAMPTZ,

    CONSTRAINT "users_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "groups" (
    "id" UUID NOT NULL,
    "group_name" TEXT NOT NULL,
    "icon" TEXT,
    "owner_id" UUID NOT NULL,
    "invite_code" TEXT NOT NULL,
    "max_members" SMALLINT NOT NULL DEFAULT 12,
    "leaderboard_enabled" BOOLEAN NOT NULL DEFAULT false,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" TIMESTAMPTZ,

    CONSTRAINT "groups_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "group_members" (
    "id" UUID NOT NULL,
    "group_id" UUID NOT NULL,
    "user_id" UUID NOT NULL,
    "role" "group_member_role" NOT NULL DEFAULT 'member',
    "joined_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "group_members_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "habits" (
    "id" UUID NOT NULL,
    "habit_name" TEXT NOT NULL,
    "icon" TEXT,
    "color" TEXT,
    "description" TEXT,
    "lifecycle" "habit_lifecycle" NOT NULL DEFAULT 'active',
    "direction" "habit_direction" NOT NULL DEFAULT 'building',
    "visibility" "habit_visibility" NOT NULL DEFAULT 'private',
    "repeat_habit" "habit_repeat" NOT NULL DEFAULT 'daily',
    "weekdays" SMALLINT[],
    "times_per_week" SMALLINT,
    "interval_days" SMALLINT,
    "start_date" DATE NOT NULL,
    "habit_type" "habit_type" NOT NULL DEFAULT 'boolean',
    "target_value" DECIMAL(65,30),
    "target_unit" TEXT,
    "allowed_misses_per_week" SMALLINT NOT NULL DEFAULT 1,
    "user_id" UUID NOT NULL,
    "group_id" UUID,
    "category_id" UUID,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" TIMESTAMPTZ,

    CONSTRAINT "habits_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "habit_logs" (
    "id" UUID NOT NULL,
    "habit_id" UUID NOT NULL,
    "user_id" UUID NOT NULL,
    "log_date" DATE NOT NULL,
    "status" "habit_log_status" NOT NULL,
    "value" DECIMAL(65,30),
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "habit_logs_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "reactions" (
    "id" UUID NOT NULL,
    "habit_log_id" UUID NOT NULL,
    "user_id" UUID NOT NULL,
    "kind" "reaction_kind" NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "reactions_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "users_username_key" ON "users"("username");

-- CreateIndex
CREATE UNIQUE INDEX "users_email_key" ON "users"("email");

-- CreateIndex
CREATE INDEX "users_deleted_at_idx" ON "users"("deleted_at");

-- CreateIndex
CREATE UNIQUE INDEX "groups_invite_code_key" ON "groups"("invite_code");

-- CreateIndex
CREATE INDEX "groups_owner_id_idx" ON "groups"("owner_id");

-- CreateIndex
CREATE INDEX "group_members_user_id_idx" ON "group_members"("user_id");

-- CreateIndex
CREATE UNIQUE INDEX "group_members_group_id_user_id_key" ON "group_members"("group_id", "user_id");

-- CreateIndex
CREATE INDEX "habits_user_id_idx" ON "habits"("user_id");

-- CreateIndex
CREATE INDEX "habits_group_id_idx" ON "habits"("group_id");

-- CreateIndex
CREATE INDEX "habits_category_id_idx" ON "habits"("category_id");

-- CreateIndex
CREATE INDEX "habits_group_id_visibility_idx" ON "habits"("group_id", "visibility");

-- CreateIndex
CREATE INDEX "habit_logs_user_id_log_date_idx" ON "habit_logs"("user_id", "log_date");

-- CreateIndex
CREATE INDEX "habit_logs_log_date_idx" ON "habit_logs"("log_date");

-- CreateIndex
CREATE UNIQUE INDEX "habit_logs_habit_id_user_id_log_date_key" ON "habit_logs"("habit_id", "user_id", "log_date");

-- CreateIndex
CREATE INDEX "reactions_habit_log_id_idx" ON "reactions"("habit_log_id");

-- CreateIndex
CREATE UNIQUE INDEX "reactions_habit_log_id_user_id_key" ON "reactions"("habit_log_id", "user_id");

-- AddForeignKey
ALTER TABLE "groups" ADD CONSTRAINT "groups_owner_id_fkey" FOREIGN KEY ("owner_id") REFERENCES "users"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "group_members" ADD CONSTRAINT "group_members_group_id_fkey" FOREIGN KEY ("group_id") REFERENCES "groups"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "group_members" ADD CONSTRAINT "group_members_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "habits" ADD CONSTRAINT "habits_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "habits" ADD CONSTRAINT "habits_group_id_fkey" FOREIGN KEY ("group_id") REFERENCES "groups"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "habits" ADD CONSTRAINT "habits_category_id_fkey" FOREIGN KEY ("category_id") REFERENCES "habit_categories"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "habit_logs" ADD CONSTRAINT "habit_logs_habit_id_fkey" FOREIGN KEY ("habit_id") REFERENCES "habits"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "habit_logs" ADD CONSTRAINT "habit_logs_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "reactions" ADD CONSTRAINT "reactions_habit_log_id_fkey" FOREIGN KEY ("habit_log_id") REFERENCES "habit_logs"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "reactions" ADD CONSTRAINT "reactions_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE;
