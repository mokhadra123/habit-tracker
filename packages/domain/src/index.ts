export { resolveLogDate } from './utils/resolveLogDate';
export { isExpectedOn, weekRangeFor } from './utils/schedule';
export type {
  CalendarDate,
  Expectation,
  ScheduleRule,
  WeekRange,
  LogStatus,
  DayLog,
  StreakSettings,
  Streak,
  HabitType,
  HabitForLog,
  LogRejection,
  LogValidation,
  ConsistencySettings,
} from './types/domain.types';
export { computeStreak } from './utils/streak';
export { validateLog } from './utils/validateLog';
export { consistencyScore } from './utils/consistency';
