# -*- coding: utf-8 -*-
from _kit import *

SIDEBAR = ('<div style="width:238px; flex-shrink:0; border-right:1px solid oklch(0.915 0.010 80); background:%s; '
  'display:flex; flex-direction:column; padding:26px 16px 20px;">'
  '<div style="display:flex; align-items:center; gap:10px; padding:0 8px 26px;">'
  '<div style="width:26px; height:26px; border-radius:8px; background:%s; display:flex; align-items:center; justify-content:center;">%s</div>'
  '<span class="serif" style="font-size:19px;">Daybreak</span></div>'
  '<div style="display:flex; flex-direction:column; gap:2px;">'
  '<div style="display:flex; align-items:center; gap:11px; padding:10px 12px; border-radius:10px; font-size:13.5px; color:%s;">%s Today</div>'
  '<div style="display:flex; align-items:center; gap:11px; padding:10px 12px; border-radius:10px; background:%s; border:1px solid %s; font-size:13.5px; font-weight:600;">%s All habits</div>'
  '<div style="display:flex; align-items:center; gap:11px; padding:10px 12px; border-radius:10px; font-size:13.5px; color:%s;">%s Insights</div></div>'
  '<div class="cap" style="padding:26px 12px 10px;">Group</div>'
  '<div style="display:flex; align-items:center; gap:11px; padding:11px 12px; border-radius:10px; background:%s;">%s'
  '<div style="flex-grow:1; font-size:13px; font-weight:600; color:oklch(0.38 0.07 45);">Sunrise Club</div></div>'
  '<div style="margin-top:auto; display:flex; align-items:center; gap:11px; padding:16px 12px 10px; border-top:1px solid %s;">%s'
  '<div style="flex-grow:1;"><div style="font-size:12.5px; font-weight:500;">Mohamed</div>'
  '<div style="font-size:10.5px; color:%s;">Cairo &middot; day starts 04:00</div></div></div></div>'
  % (SUNK, TERRA, icon('check', 15, 2.6, ON_TERRA), INK2, icon('calendar', 18, 1.9), CARD, LINE,
     icon('list', 18, 1.9), INK2, icon('trend', 18, 1.9), TERRA_SOFT,
     stack(['Y','A','H'], 22, TERRA_SOFT), 'oklch(0.92 0.010 80)', avatar('M', 30), INK4))

def stat(big, label, sub=''):
    s = ('<div style="font-size:10.5px; color:%s; margin-top:5px;">%s</div>' % (INK4, sub)) if sub else ''
    return ('<div style="flex-grow:1;"><div class="serif" style="font-size:38px; line-height:0.95;">%s</div>'
            '<div style="font-size:11.5px; color:%s; margin-top:8px;">%s</div>%s</div>' % (big, INK2, label, s))

bars = ''.join(
  '<div style="flex-grow:1; display:flex; flex-direction:column; align-items:center; gap:8px;">'
  '<div style="width:100%%; height:%spx; background:%s; border-radius:5px 5px 0 0;"></div>'
  '<span style="font-size:10px; color:%s;">%s</span></div>'
  % (h, (AMBER if h < 50 else SAGE), (INK if h < 50 else INK3), d)
  for d, h in [('Mon',104),('Tue',96),('Wed',88),('Thu',110),('Fri',82),('Sat',38),('Sun',72)])

entries = ''.join(
  '<div style="display:flex; align-items:center; gap:14px; padding:11px 14px; border-bottom:1px solid %s;">'
  '<div style="width:8px; height:8px; border-radius:999px; %s"></div>'
  '<div style="width:150px; font-size:12.5px;">%s</div>'
  '<div style="width:90px; font-size:12.5px; color:%s;">%s</div>'
  '<div style="flex-grow:1; font-size:12px; color:%s; font-style:%s;">%s</div>'
  '<div style="font-size:11.5px; color:%s;">%s</div></div>'
  % (LINE_SOFT, dot, day, INK2, val, INK2, ('italic' if n else 'normal'), n or '&mdash;', INK4, t)
  for day, val, n, t, dot in [
    ('Sunday 23 Aug', '5.2 km', '', '06:40', 'background:%s;' % SAGE),
    ('Saturday 22 Aug', '&mdash;', 'Skipped, travelling', '', 'border:1.5px dashed %s;' % LINE_STRONG),
    ('Friday 21 Aug', '4.0 km', 'Legs heavy, went slow. Still counts.', '07:05', 'background:%s;' % SAGE),
    ('Thursday 20 Aug', '6.4 km', '', '06:32', 'background:%s;' % SAGE),
    ('Wednesday 19 Aug', '&mdash;', '', '', 'background:%s;' % EMPTY),
  ])

body = ('<div style="width:1280px; height:860px; display:flex; background:%s;">%s'
  '<div style="flex-grow:1; padding:32px; min-width:0; display:flex; flex-direction:column;">'
  '<div style="display:flex; align-items:flex-start; justify-content:space-between;">'
  '<div><div style="display:flex; gap:9px;">%s%s</div>'
  '<div class="serif" style="font-size:38px; line-height:1.04; margin-top:11px;">Morning run</div></div>'
  '<div style="display:flex; gap:9px;">'
  '<button style="height:38px; padding:0 15px; border-radius:11px; border:1px solid %s; background:%s; font-family:inherit; font-size:12.5px; color:%s; cursor:pointer;">Edit</button>'
  '<button style="height:38px; padding:0 15px; border-radius:11px; border:1px solid %s; background:%s; font-family:inherit; font-size:12.5px; color:%s; cursor:pointer; display:flex; align-items:center; gap:7px;">%s Export</button>'
  '</div></div>'
  '<div style="display:flex; gap:16px; margin-top:26px;">%s</div>'
  '<div style="margin-top:18px;">%s</div>'
  '<div style="display:flex; gap:16px; margin-top:16px; flex-grow:1; min-height:0;">'
  '<div style="width:330px; flex-shrink:0;">%s</div>'
  '<div style="flex-grow:1; min-width:0;">%s</div>'
  '</div></div></div>'
  % (PAPER, SIDEBAR,
     chip('4&times; a week', 'sage'), chip('Shared with Sunrise Club', 'terra', 'users'),
     LINE, CARD, INK2, LINE, CARD, INK2, icon('download', 15, 1.9),
     card('<div style="display:flex; gap:26px;">%s%s%s%s</div>'
          % (stat('86%', '30-day consistency', 'up 9 points on last month'),
             stat('12', 'day run', '1 miss left this week'),
             stat('23', 'longest run', 'June'),
             stat('128', 'entries', 'since 12 April')), pad='20px 24px'),
     card('<div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:16px;">'
          '<div class="cap">A full year</div><div style="font-size:11px; color:%s;">Sep 2025 &ndash; Aug 2026</div></div>'
          '<div style="display:flex; gap:3px;">'
          '<sc-for list="{{weeks}}" as="w" hint-placeholder-count="52">'
          '<div style="display:flex; flex-direction:column; gap:3px;">'
          '<sc-for list="{{w.days}}" as="c" hint-placeholder-count="7">'
          '<div style="width:15px; height:15px; border-radius:4px; background: {{c.bg}}; border: {{c.border}};"></div>'
          '</sc-for></div></sc-for></div>' % INK4, pad='20px 24px'),
     card('<div class="cap" style="padding-bottom:18px;">Completion by weekday</div>'
          '<div style="display:flex; align-items:flex-end; gap:9px; height:130px;">%s</div>'
          '<div style="font-size:11.5px; color:%s; line-height:1.55; margin-top:16px;">'
          '<strong style="color:%s;">Saturday is the outlier.</strong> 41%% against 94%% on weekdays. '
          'Dropping it from the schedule would raise your consistency without changing anything you actually do.</div>'
          % (bars, INK2, INK), pad='20px 24px'),
     card('<div style="display:flex; justify-content:space-between; align-items:baseline; padding-bottom:6px;">'
          '<div class="cap">Recent entries</div>'
          '<div style="font-size:11px; color:%s;">128 total</div></div>%s' % (INK4, entries), pad='20px 8px 8px 8px')))

script = """  renderVals() {
    var levels = ['%s', '%s', '%s', 'oklch(0.68 0.095 155)', '%s'];
    var seed = 4711;
    function rnd() { seed = (seed * 1103515245 + 12345) %% 2147483648; return seed / 2147483648; }
    var weeks = [];
    for (var w = 0; w < 52; w++) {
      var days = [];
      for (var d = 0; d < 7; d++) {
        var bg = levels[0], border = '1px solid transparent';
        if (d === 5) { bg = rnd() < 0.6 ? levels[0] : levels[2]; }
        else if (w < 8) { bg = levels[Math.floor(rnd() * 3)]; }
        else { var pool = [1, 2, 3, 4, 4, 3, 4, 2]; bg = levels[pool[Math.floor(rnd() * pool.length)]]; }
        if ((w * 7 + d) %% 47 === 11) { bg = 'transparent'; border = '1.5px dashed %s'; }
        days.push({ bg: bg, border: border });
      }
      weeks.push({ days: days });
    }
    return { weeks: weeks };
  }""" % (EMPTY, SAGE_PALE, SAGE_MID, SAGE, LINE_STRONG)

write('DesktopHabit.dc.html', body, script)
print('desktop habit ok')
