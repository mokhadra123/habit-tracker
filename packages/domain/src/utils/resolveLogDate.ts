import { type CalendarDate } from '../types/domain.types';

/**
 * Building an Intl.DateTimeFormat is expensive (it reaches into ICU), and this
 * runs on every log write. There are only a handful of distinct time zones
 * across all users, so one formatter per zone is cached for the process.
 */
const formatterCache = new Map<string, Intl.DateTimeFormat>();

function getFormatter(timeZone: string): Intl.DateTimeFormat {
  const cached = formatterCache.get(timeZone);
  if (cached) return cached;

  let formatter: Intl.DateTimeFormat;
  try {
    formatter = new Intl.DateTimeFormat('en-CA', {
      timeZone,
      year: 'numeric',
      month: '2-digit',
      day: '2-digit',
      hour: '2-digit',
      hourCycle: 'h23',
    });
  } catch {
    throw new RangeError(`resolveLogDate: unknown IANA time zone "${timeZone}"`);
  }

  formatterCache.set(timeZone, formatter);
  return formatter;
}

// The instant expressed as calendar parts in one specific time zone.
function localParts(formatter: Intl.DateTimeFormat, instant: Date) {
  const parts = formatter.formatToParts(instant);

  const read = (type: Intl.DateTimeFormatPartTypes): number => {
    const part = parts.find((p) => p.type === type);
    if (part === undefined) {
      throw new Error(`resolveLogDate: formatter produced no "${type}" part`);
    }
    return Number(part.value);
  };

  return { year: read('year'), month: read('month'), day: read('day'), hour: read('hour') };
}

export function resolveLogDate(instant: Date, timeZone: string, dayBoundaryHour = 0): CalendarDate {
  if (Number.isNaN(instant.getTime())) {
    throw new RangeError('resolveLogDate: instant is an Invalid Date');
  }

  if (!Number.isInteger(dayBoundaryHour) || dayBoundaryHour < 0 || dayBoundaryHour > 23) {
    throw new RangeError(
      `resolveLogDate: dayBoundaryHour must be an integer 0-23, received ${String(dayBoundaryHour)}`,
    );
  }

  const { year, month, day, hour } = localParts(getFormatter(timeZone), instant);

  // Before the user's day boundary, so this still belongs to yesterday.
  const dayOffset = hour < dayBoundaryHour ? -1 : 0;

  const resolved = new Date(Date.UTC(year, month - 1, day + dayOffset));

  return resolved.toISOString().slice(0, 10);
}
