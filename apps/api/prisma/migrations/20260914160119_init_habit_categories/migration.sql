-- CreateTable
CREATE TABLE "habit_categories" (
    "id" UUID NOT NULL,
    "habit_category_name" TEXT NOT NULL,

    CONSTRAINT "habit_categories_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "habit_categories_habit_category_name_key" ON "habit_categories"("habit_category_name");
