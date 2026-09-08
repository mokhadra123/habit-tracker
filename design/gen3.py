# -*- coding: utf-8 -*-
from _kit import *

def srow(label, value='', ico=None, right=None, sub=None, danger=False):
    fg = 'oklch(0.50 0.14 30)' if danger else INK
    ic = ('<div style="width:32px; height:32px; border-radius:10px; background:%s; display:flex; align-items:center; '
          'justify-content:center; color:%s; flex-shrink:0;">%s</div>' % (SUNK, fg if danger else INK2, icon(ico, 17, 1.9))) if ico else ''
    sb = ('<div style="font-size:11px; color:%s; margin-top:3px; line-height:1.45;">%s</div>' % (INK3, sub)) if sub else ''
    rt = right if right is not None else ('<span style="font-size:12.5px; color:%s;">%s</span>%s' % (INK3, value, icon('right', 16, 2)))
    return ('<div style="display:flex; align-items:center; gap:12px; padding:13px 15px; background:%s; border:1px solid %s; '
            'border-radius:14px; min-height:44px;">%s<div style="flex-grow:1; min-width:0;">'
            '<div style="font-size:13.5px; font-weight:500; color:%s;">%s</div>%s</div>'
            '<div style="display:flex; align-items:center; gap:7px; color:%s; flex-shrink:0;">%s</div></div>'
            % (CARD, LINE, ic, fg, label, sb, INK3, rt))

# --------------------------------------------------------------- Habits list
def hcard(name, sub, pct, pattern, tone=INK, faces=None, dim=False):
    op = ' opacity:0.55;' if dim else ''
    f = stack(faces) if faces else ''
    return ('<div style="padding:14px; background:%s; border:1px solid %s; border-radius:16px;%s">'
            '<div style="display:flex; align-items:center; gap:12px;">'
            '<div style="flex-grow:1; min-width:0;"><div style="font-size:14.5px; font-weight:500;">%s</div>'
            '<div style="font-size:11.5px; color:%s; margin-top:3px;">%s</div></div>'
            '<div style="font-size:15px; font-weight:600; color:%s;">%s</div></div>'
            '<div style="display:flex; align-items:center; gap:12px; margin-top:12px;">%s'
            '<div style="flex-grow:1;"></div>%s</div></div>'
            % (CARD, LINE, op, name, INK3, sub, tone, pct, daydots(pattern, 17, 6, labels=False), f))

body = frame(
  header('Everything', 'Your habits',
         '<button style="width:40px; height:40px; border-radius:12px; border:none; background:%s; color:%s; display:flex; align-items:center; justify-content:center; cursor:pointer; padding:0;">%s</button>' % (TERRA, ON_TERRA, icon('plus', 20, 2.3)))
  + '<div style="display:flex; gap:7px; padding:20px 20px 0; overflow:hidden;">%s%s%s%s</div>'
    % (chip('All 5', 'terra'), chip('Building', 'neutral'), chip('Breaking', 'neutral'), chip('Shared', 'neutral'))
  + cap('Active', '22px 20px 11px')
  + col([
      hcard('Morning run', '4&times; a week &middot; 12 day run', '92%', 'xx.xxot', faces=['Y','A','H']),
      hcard('Read', '20 pages a day', '81%', 'xoxx.ot', faces=['A']),
      hcard('Meditate', '10 minutes daily', '64%', 'x.xs.xt', tone=AMBER_DEEP, faces=['H']),
      hcard('No phone after 22:00', 'Breaking &middot; 6 clean nights', '88%', 'xxxxxxt'),
      hcard('Swim', '3&times; a week &middot; started Tuesday', '&mdash;', '....o.t', tone=INK4, faces=['Y']),
    ])
  + cap('Archived &mdash; history kept', '24px 20px 11px')
  + col([hcard('Journal', 'Retired 2 August &middot; 46 days logged', '58%', '.......', tone=INK4, dim=True)])
  + '<div style="padding:20px 20px 0;">%s</div>' % note(
      'Archiving keeps every entry and takes the habit off Today. Nothing is ever really deleted unless you delete your account.', 'grey', 'archive')
  + nav('habits'))
write('HabitsList.dc.html', body)

# ------------------------------------------------- Habit detail: breaking
nights = ''.join(
  '<div style="width:19px; height:19px; border-radius:5px; background:%s;"></div>' % (
      'oklch(0.90 0.03 30)' if i in (3, 17, 26) else (PLUM if i > 30 else PLUM_SOFT))
  for i in range(42))
body = frame(
  topbar('left', '', '<button style="height:32px; padding:0 13px; border-radius:999px; border:1px solid %s; background:%s; font-family:inherit; font-size:12px; color:%s; cursor:pointer;">Edit</button>' % (LINE, CARD, INK2))
  + '<div style="padding:10px 20px 0;">'
    '<div style="display:flex; gap:9px;">%s%s</div>'
    '<div class="serif" style="font-size:34px; line-height:1.05; margin-top:12px;">No phone after 22:00</div></div>'
    % (chip('Breaking', 'plum', 'moon'), chip('Private', 'neutral', 'lock'))
  + '<div style="padding:18px 20px 0;">%s</div>' % card(
      '<div style="display:flex; align-items:flex-end; gap:20px;">'
      '<div><div class="serif" style="font-size:52px; line-height:0.9;">6</div>'
      '<div style="font-size:11.5px; color:%s; margin-top:8px;">clean nights in a row</div></div>'
      '<div style="flex-grow:1; text-align:right; padding-bottom:4px;">'
      '<div style="font-size:19px; font-weight:600;">88%%</div>'
      '<div style="font-size:11px; color:%s; margin-top:4px;">clean over 30 days</div></div></div>'
      '<div style="height:1px; background:%s; margin:16px 0 14px;"></div>'
      '<div style="display:flex; align-items:center; justify-content:space-between;">'
      '<span style="font-size:12px; color:%s;">Longest clean run</span>'
      '<span style="font-size:13px; font-weight:600;">19 nights, in June</span></div>'
      % (INK2, INK3, LINE_SOFT, INK2), pad='18px')
  + '<div style="padding:14px 20px 0;">%s</div>' % card(
      '<div class="cap" style="padding-bottom:14px;">Last six weeks</div>'
      '<div style="display:grid; grid-template-columns:repeat(14, minmax(0, 1fr)); gap:5px;">%s</div>'
      '<div style="display:flex; align-items:center; gap:7px; margin-top:14px;">'
      '<div style="width:13px; height:13px; border-radius:4px; background:%s;"></div>'
      '<span style="font-size:10.5px; color:%s;">clean</span>'
      '<div style="width:13px; height:13px; border-radius:4px; background:%s; margin-left:10px;"></div>'
      '<span style="font-size:10.5px; color:%s;">slipped</span></div>' % (nights, PLUM, INK3, 'oklch(0.90 0.03 30)', INK3), pad='18px')
  + '<div style="padding:14px 20px 0;">%s</div>' % note(
      'Three slips in six weeks, all on Fridays. That is a pattern, not a character flaw &mdash; try putting the charger in the kitchen on Friday.', 'plum', 'info')
  + cap('When it slips', '22px 20px 10px')
  + col([
      '<div style="display:flex; align-items:center; gap:12px; padding:12px 14px; background:%s; border:1px solid %s; border-radius:13px;">'
      '<div style="width:8px; height:8px; border-radius:999px; background:%s;"></div>'
      '<div style="flex-grow:1; font-size:13px;">Friday 15 August <span style="color:%s;">&middot; 23:40</span></div></div>'
      % (CARD, LINE, 'oklch(0.72 0.10 30)', INK3),
      '<div style="display:flex; align-items:center; gap:12px; padding:12px 14px; background:%s; border:1px solid %s; border-radius:13px;">'
      '<div style="width:8px; height:8px; border-radius:999px; background:%s;"></div>'
      '<div style="flex-grow:1; font-size:13px;">Friday 8 August <span style="color:%s;">&middot; 00:20</span></div></div>'
      % (CARD, LINE, 'oklch(0.72 0.10 30)', INK3),
    ], pad='0 20px 26px'))
write('HabitBreaking.dc.html', body)

# ----------------------------------------------------------------- Edit habit
body = frame(
  topbar('x', 'Edit habit', '<button style="min-width:56px; min-height:44px; border:none; background:transparent; font-family:inherit; font-size:13.5px; font-weight:600; color:%s; text-align:right; cursor:pointer; padding:0;">Save</button>' % TERRA)
  + '<div style="padding:14px 20px 0; display:flex; flex-direction:column; gap:10px;">%s%s%s</div>'
    % (field('Habit name', 'Morning run'), field('Target', '4 times a week', ico='calendar'), field('Reminder', '06:15', ico='bell'))
  + cap('Forgiveness', '22px 20px 10px')
  + col([
      srow('Misses allowed each week', '1', right=toggle(True) if False else '<span style="font-size:15px; font-weight:600;">1</span>' + icon('right', 16, 2)),
      srow('Pause until', 'Not paused', ico='pause', sub='Freeze the habit without ending it'),
    ])
  + cap('Sharing', '22px 20px 10px')
  + col([srow('Visible to', 'Sunrise Club', ico='users'),
         srow('Let the group verify', '', ico='check', sub='Someone confirms your entry', right=toggle(False))])
  + cap('Ending it', '24px 20px 10px')
  + col([
      '<div style="padding:15px; background:%s; border:1px solid %s; border-radius:14px;">'
      '<div style="display:flex; align-items:center; gap:12px;">'
      '<div style="width:32px; height:32px; border-radius:10px; background:%s; display:flex; align-items:center; justify-content:center; color:%s;">%s</div>'
      '<div style="flex-grow:1;"><div style="font-size:13.5px; font-weight:500;">Archive</div>'
      '<div style="font-size:11px; color:%s; margin-top:3px; line-height:1.45;">Off Today, all 128 entries kept</div></div>%s</div></div>'
      % (CARD, LINE, SUNK, INK2, icon('archive', 17, 1.9), INK3, icon('right', 16, 2)),
      '<div style="padding:15px; background:oklch(0.98 0.012 30); border:1px solid oklch(0.90 0.03 30); border-radius:14px;">'
      '<div style="display:flex; align-items:center; gap:12px;">'
      '<div style="width:32px; height:32px; border-radius:10px; background:oklch(0.95 0.025 30); display:flex; align-items:center; justify-content:center; color:oklch(0.52 0.14 30);">%s</div>'
      '<div style="flex-grow:1;"><div style="font-size:13.5px; font-weight:500; color:oklch(0.44 0.13 30);">Delete permanently</div>'
      '<div style="font-size:11px; color:oklch(0.55 0.08 30); margin-top:3px; line-height:1.45;">128 entries gone. This cannot be undone.</div></div></div></div>'
      % icon('trash', 17, 1.9),
    ], pad='0 20px 28px'))
write('EditHabit.dc.html', body)

# -------------------------------------------------------------- Group members
def member(k, role, streak, you=False):
    ini, tint, ink, name = PEOPLE[k]
    tag = chip('You', 'terra') if you else (chip(role, 'neutral') if role else '')
    return ('<div style="display:flex; align-items:center; gap:12px; padding:13px 14px; background:%s; border:1px solid %s; '
            'border-radius:14px;">%s<div style="flex-grow:1; min-width:0;">'
            '<div style="display:flex; align-items:center; gap:8px;"><span style="font-size:14px; font-weight:500;">%s</span>%s</div>'
            '<div style="font-size:11px; color:%s; margin-top:3px;">%s</div></div>%s</div>'
            % (CARD, LINE, avatar(k, 38), name, tag, INK3, streak, icon('right', 16, 2)))

body = frame(
  topbar('left', 'Sunrise Club')
  + '<div style="padding:16px 20px 0;">%s</div>' % card(
      '<div style="display:flex; align-items:center; gap:13px;">'
      '<div style="width:38px; height:38px; border-radius:11px; background:%s; display:flex; align-items:center; justify-content:center; color:%s; flex-shrink:0;">%s</div>'
      '<div style="flex-grow:1; min-width:0;"><div style="font-size:12.5px; font-weight:600;">habit.app/j/sunrise-4f2a</div>'
      '<div style="font-size:11px; color:%s; margin-top:3px;">Anyone with the link can join &middot; expires in 7 days</div></div>'
      '<button style="width:38px; height:38px; border-radius:11px; border:1px solid %s; background:%s; color:%s; display:flex; align-items:center; justify-content:center; cursor:pointer; padding:0;">%s</button></div>'
      % (TERRA_SOFT, TERRA_DEEP, icon('link', 19, 1.9), INK3, LINE, SUNK, INK, icon('copy', 17, 1.9)), pad='15px')
  + cap('Five members', '24px 20px 11px')
  + col([member('M', 'Owner', 'Since April &middot; 86% this month', you=True),
         member('Y', '', 'Since April &middot; 94% this month'),
         member('A', '', 'Since April &middot; 78% this month'),
         member('S', '', 'Quiet for 6 days &middot; 41% this month'),
         member('H', '', 'Joined June &middot; 71% this month')], gap=9)
  + cap('Group rules', '24px 20px 11px')
  + col([srow('Leaderboard', 'Off', ico='trend', sub='Ranking friends helps whoever is winning and nobody else', right=toggle(False)),
         srow('Nudges', 'Once a week each', ico='bell'),
         srow('Who can invite', 'Owner only', ico='users')], gap=9, pad='0 20px 28px'))
write('GroupMembers.dc.html', body)

# --------------------------------------------------------------- Weekly review
def rev(label, val, bar, tone=SAGE):
    return ('<div style="display:flex; align-items:center; gap:12px;">'
            '<div style="width:112px; font-size:12.5px; color:%s;">%s</div>'
            '<div style="flex-grow:1; height:8px; border-radius:999px; background:%s; overflow:hidden;">'
            '<div style="width:%s; height:8px; border-radius:999px; background:%s;"></div></div>'
            '<div style="width:38px; text-align:right; font-size:12px; font-weight:600;">%s</div></div>'
            % (INK2, label, LINE_SOFT, bar, tone, val))

body = frame(
  '<div style="padding:34px 24px 0;">'
  '<div class="cap">Sunday evening</div>'
  '<div class="serif" style="font-size:34px; line-height:1.06; margin-top:7px;">How the week<br>actually went.</div>'
  '<div style="font-size:13px; color:%s; margin-top:11px; line-height:1.6; text-wrap:pretty;">Two minutes. It is the only screen that asks you to think rather than tap.</div></div>' % INK2
  + '<div style="padding:24px 24px 0;">%s</div>' % card(
      '<div style="display:flex; flex-direction:column; gap:13px;">%s%s%s%s</div>'
      % (rev('Morning run', '4/4', '100%'), rev('Read', '5/7', '71%', SAGE_MID),
         rev('Meditate', '2/7', '29%', AMBER), rev('No phone', '6/7', '86%', PLUM)), pad='18px')
  + '<div style="padding:14px 24px 0;">%s</div>' % note(
      'Meditation has been under half for three weeks. It is usually the schedule, not the willpower.', 'amber', 'alert')
  + cap('One thing for next week', '24px 24px 11px')
  + col([
      btn('Drop meditation to 3&times; a week', 'secondary', 'calendar', sub='Recommended &mdash; a target you will actually hit'),
      btn('Move the reminder to 21:00', 'secondary', 'clock', sub='You log it late on the days you do it'),
      btn('Leave it alone', 'dashed', full=True),
    ], gap=9, pad='0 24px')
  + '<div style="padding:22px 24px 0;">%s</div>' % card(
      '<div style="display:flex; align-items:center; gap:12px;">%s'
      '<div style="flex-grow:1;"><div style="font-size:12.5px; font-weight:600; color:%s;">Sunrise Club, this week</div>'
      '<div style="font-size:11.5px; color:%s; margin-top:3px;">24 of 35 between the five of you</div></div>%s</div>'
      % (stack(['Y','A','S','H'], 28, TERRA_SOFT), 'oklch(0.38 0.07 45)', 'oklch(0.50 0.05 45)', icon('right', 17, 2)),
      pad='15px 16px', bg=TERRA_SOFT, border=False)
  + '<div style="padding:22px 24px 30px;">%s</div>' % btn('Start the new week', 'primary'))
write('WeeklyReview.dc.html', body)

# ---------------------------------------------------------------- Group empty
body = frame(
  header('Group', 'Nobody yet')
  + '<div style="flex-grow:1; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:0 30px; text-align:center;">'
    '<div style="display:flex; align-items:center;">'
    '<div style="width:46px; height:46px; border-radius:999px; border:1.5px dashed %s;"></div>'
    '<div style="width:46px; height:46px; border-radius:999px; border:1.5px dashed %s; margin-left:-12px;"></div>'
    '<div style="width:46px; height:46px; border-radius:999px; border:1.5px dashed %s; margin-left:-12px;"></div></div>'
    '<div class="serif" style="font-size:29px; line-height:1.12; margin-top:26px;">This is the part<br>that works.</div>'
    '<div style="font-size:13px; color:%s; margin-top:12px; line-height:1.65; text-wrap:pretty;">'
    'People who track alone mostly stop by week six. People who can see three friends doing the same thing mostly do not.</div>'
    '<div style="width:100%%; margin-top:28px; display:flex; flex-direction:column; gap:10px;">%s%s</div>'
    '<div style="font-size:11.5px; color:%s; margin-top:18px; line-height:1.6;">Three to five people. More than that and nobody notices when you go quiet.</div>'
    '</div>' % (LINE_STRONG, LINE_STRONG, LINE_STRONG, INK2,
                btn('Start a group', 'primary', 'users'), btn('Join with a code', 'secondary', 'link'), INK4)
  + nav('group', badge_group=False))
write('GroupEmpty.dc.html', body)

# -------------------------------------------------------------------- Profile
body = frame(
  header('You', 'Mohamed')
  + '<div style="padding:20px 20px 0;">%s</div>' % card(
      '<div style="display:flex; align-items:center; gap:15px;">%s'
      '<div style="flex-grow:1;"><div style="font-size:15px; font-weight:600;">Mohamed Khadra</div>'
      '<div style="font-size:11.5px; color:%s; margin-top:3px;">Tracking since 12 April &middot; 133 days</div></div></div>'
      '<div style="height:1px; background:%s; margin:16px 0 14px;"></div>'
      '<div style="display:flex; justify-content:space-between; text-align:center;">'
      '<div><div class="serif" style="font-size:26px;">86%%</div><div style="font-size:10.5px; color:%s; margin-top:4px;">30 days</div></div>'
      '<div><div class="serif" style="font-size:26px;">79%%</div><div style="font-size:10.5px; color:%s; margin-top:4px;">lifetime</div></div>'
      '<div><div class="serif" style="font-size:26px;">23</div><div style="font-size:10.5px; color:%s; margin-top:4px;">longest run</div></div>'
      '<div><div class="serif" style="font-size:26px;">412</div><div style="font-size:10.5px; color:%s; margin-top:4px;">entries</div></div></div>'
      % (avatar('M', 52), INK3, LINE_SOFT, INK3, INK3, INK3, INK3), pad='18px')
  + cap('Your day', '24px 20px 11px')
  + col([srow('Time zone', 'Africa / Cairo', ico='pin'),
         srow('Day starts at', '04:00', ico='clock', sub='A 01:00 log still counts for the night before')], gap=9)
  + cap('App', '22px 20px 11px')
  + col([srow('Reminders', '3 of 3 used', ico='bell'),
         srow('Groups', 'Sunrise Club', ico='users'),
         srow('Data and privacy', '', ico='lock')], gap=9)
  + '<div style="padding:22px 20px 0;">%s</div>' % srow('Sign out', '', ico='key', right='')
  + nav('you', badge_group=False))
write('Profile.dc.html', body)

# ------------------------------------------------------- Notification settings
body = frame(
  topbar('left', 'Reminders')
  + '<div style="padding:16px 20px 0;">%s</div>' % card(
      '<div style="display:flex; align-items:center; justify-content:space-between;">'
      '<div><div class="cap">Daily budget</div>'
      '<div class="serif" style="font-size:38px; line-height:1; margin-top:7px;">3 <span style="font-size:19px; color:%s;">of 3</span></div></div>'
      '<div style="display:flex; gap:6px;">'
      '<div style="width:12px; height:12px; border-radius:999px; background:%s;"></div>'
      '<div style="width:12px; height:12px; border-radius:999px; background:%s;"></div>'
      '<div style="width:12px; height:12px; border-radius:999px; background:%s;"></div></div></div>'
      '<div style="font-size:11.5px; color:%s; margin-top:12px; line-height:1.55;">'
      'This is a hard cap we put on ourselves. To add a fourth reminder you have to turn one off.</div>'
      % (INK3, TERRA, TERRA, TERRA, INK2), pad='18px')
  + cap('In use', '22px 20px 11px')
  + col([srow('Morning run', '06:15', ico='bell', right=toggle(True)),
         srow('Read', '21:30', ico='bell', right=toggle(True)),
         srow('No phone', '21:45', ico='bell', right=toggle(True)),
         srow('Meditate', 'No reminder &mdash; budget full', ico='bell-off', right=toggle(False))], gap=9)
  + cap('Behaviour', '22px 20px 11px')
  + col([
      srow('Skip if already logged', '', ico='check', sub='No reminder for something you have done', right=toggle(True)),
      srow('Back off when ignored', '', ico='trend', sub='Ignored three times running, it halves and tells you', right=toggle(True)),
      srow('Quiet hours', '22:30 &ndash; 07:00', ico='moon'),
    ], gap=9)
  + '<div style="padding:20px 20px 28px;">%s</div>' % note(
      'Notification fatigue is the single most common reason people delete a habit app around week six. Fewer, later.', 'terra', 'info'))
write('NotifSettings.dc.html', body)

# ----------------------------------------------------------- Data and privacy
body = frame(
  topbar('left', 'Data and privacy')
  + cap('What the group sees', '18px 20px 11px')
  + col([srow('Shared habits', '3 of 5', ico='users', sub='Morning run, Read, Swim'),
         srow('Private habits', '2', ico='lock', sub='Never appear in any feed or digest'),
         srow('Notes on entries', 'Shared with the habit', ico='note')], gap=9)
  + cap('Your copy', '22px 20px 11px')
  + col([srow('Export as JSON', '', ico='download', sub='Every habit, entry, note and skip'),
         srow('Export as CSV', '', ico='download', sub='One row per entry, opens in a spreadsheet')], gap=9)
  + '<div style="padding:16px 20px 0;">%s</div>' % note(
      'Export is not a premium feature and never will be. It is your data and you should be able to walk away with it.', 'sage', 'check')
  + cap('Ending it', '24px 20px 11px')
  + col([
      srow('Leave Sunrise Club', '', ico='users', sub='Your shared entries stop appearing for them'),
      '<div style="padding:15px; background:oklch(0.98 0.012 30); border:1px solid oklch(0.90 0.03 30); border-radius:14px;">'
      '<div style="display:flex; align-items:center; gap:12px;">'
      '<div style="width:32px; height:32px; border-radius:10px; background:oklch(0.95 0.025 30); display:flex; align-items:center; justify-content:center; color:oklch(0.52 0.14 30);">%s</div>'
      '<div style="flex-grow:1;"><div style="font-size:13.5px; font-weight:500; color:oklch(0.44 0.13 30);">Delete account</div>'
      '<div style="font-size:11px; color:oklch(0.55 0.08 30); margin-top:3px; line-height:1.45;">412 entries and 5 habits, gone within 24 hours</div></div></div></div>'
      % icon('trash', 17, 1.9),
    ], gap=9, pad='0 20px 28px'))
write('DataPrivacy.dc.html', body)

# --------------------------------------------------------------- System states
def mini(title, inner):
    return ('<div><div class="cap" style="padding-bottom:9px;">%s</div>'
            '<div style="border:1px solid %s; border-radius:16px; overflow:hidden; background:%s;">%s</div></div>'
            % (title, LINE, PAPER, inner))

banner_off = ('<div style="display:flex; align-items:center; gap:11px; padding:12px 15px; background:%s;">'
              '<span style="color:%s;">%s</span>'
              '<div style="flex-grow:1;"><div style="font-size:12.5px; font-weight:600; color:%s;">Offline &mdash; still logging</div>'
              '<div style="font-size:11px; color:%s; margin-top:2px;">3 entries waiting to sync</div></div></div>'
              % (AMBER_SOFT, AMBER_DEEP, icon('wifi-off', 17, 1.9), AMBER_DEEP, 'oklch(0.52 0.07 75)'))

skeleton = ''.join('<div style="display:flex; align-items:center; gap:13px; padding:13px 15px;">'
                   '<div style="width:40px; height:40px; border-radius:999px; background:%s;"></div>'
                   '<div style="flex-grow:1;"><div style="height:10px; width:%spx; background:%s; border-radius:3px;"></div>'
                   '<div style="height:8px; width:%spx; background:%s; border-radius:3px; margin-top:8px;"></div></div></div>'
                   % (EMPTY, 132 - i*22, 'oklch(0.92 0.008 80)', 88 - i*14, LINE_SOFT) for i in range(3))

err = ('<div style="padding:26px 20px; text-align:center;">'
       '<div style="width:44px; height:44px; border-radius:999px; background:%s; display:flex; align-items:center; justify-content:center; color:%s; margin:0 auto;">%s</div>'
       '<div style="font-size:14.5px; font-weight:600; margin-top:14px;">Could not reach the server</div>'
       '<div style="font-size:12px; color:%s; margin-top:7px; line-height:1.55;">Everything you logged is safe on this device and will sync by itself.</div>'
       '<div style="display:flex; gap:9px; justify-content:center; margin-top:16px;">'
       '<button style="height:38px; padding:0 16px; border-radius:12px; border:1.5px solid %s; background:%s; font-family:inherit; font-size:12.5px; font-weight:600; color:%s; cursor:pointer;">Try again</button>'
       '</div></div>' % (AMBER_SOFT, AMBER_DEEP, icon('alert', 22, 2), INK2, LINE_STRONG, CARD, INK))

conflict = ('<div style="padding:16px;">%s</div>' % note(
    'You logged Read on two devices. We kept the higher value (20 pages) and left a note on the entry.', 'grey', 'info'))

sync_ok = ('<div style="display:flex; align-items:center; gap:11px; padding:12px 15px; background:%s;">'
           '<span style="color:%s;">%s</span>'
           '<div style="font-size:12.5px; font-weight:600; color:%s;">All 3 entries synced</div></div>'
           % (SAGE_SOFT, SAGE_DEEP, icon('check', 17, 2.4), SAGE_DEEP))

body = frame('''
<div style="padding:30px 24px;">
  <div class="cap">System states</div>
  <div class="serif" style="font-size:29px; line-height:1.08; margin-top:6px;">When things go wrong</div>
  <div style="font-size:12.5px; color:%s; margin-top:9px; line-height:1.6; text-wrap:pretty;">
    A habit tracker that loses a log entry is worse than no habit tracker. Every failure state says where the data is.</div>
  <div style="display:flex; flex-direction:column; gap:20px; margin-top:26px;">%s%s%s%s%s</div>
</div>''' % (INK2,
             mini('Offline banner &mdash; logging still works', banner_off),
             mini('Back online', sync_ok),
             mini('Loading', skeleton),
             mini('Server unreachable', err),
             mini('Sync conflict &mdash; resolved, not lost', conflict)), w=440, minh=880)
write('SystemStates.dc.html', body)
print('gen3 ok')
