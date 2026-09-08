# -*- coding: utf-8 -*-
from _kit import *

def sheet_screen(sheet_inner, behind_rows=3):
    ghost = ''.join('<div style="display:flex; align-items:center; gap:13px; padding:14px; background:%s; '
                    'border:1px solid %s; border-radius:16px;">'
                    '<div style="width:44px; height:44px; border-radius:999px; background:%s;"></div>'
                    '<div style="flex-grow:1;"><div style="height:10px; width:%spx; background:%s; border-radius:3px;"></div>'
                    '<div style="height:8px; width:%spx; background:%s; border-radius:3px; margin-top:8px;"></div></div></div>'
                    % (CARD, LINE, EMPTY, 120 - i*18, 'oklch(0.90 0.008 80)', 84 - i*10, LINE_SOFT)
                    for i in range(behind_rows))
    return frame(
        '<div style="position:relative; flex-grow:1; display:flex; flex-direction:column;">'
        '  <div style="filter:blur(1px); opacity:0.5;">'
        '    <div style="padding:26px 20px 0;"><div class="cap">Sunday</div>'
        '    <div class="serif" style="font-size:32px; margin-top:5px;">23 August</div></div>'
        '    <div style="display:flex; flex-direction:column; gap:10px; padding:20px 20px 0;">%s</div>'
        '  </div>'
        '  <div style="position:absolute; inset:0; background:oklch(0.24 0.018 55 / 0.34);"></div>'
        '  <div style="position:absolute; left:0; right:0; bottom:0; background:%s; border-radius:24px 24px 0 0; '
        '       box-shadow:0 -12px 40px oklch(0.24 0.018 55 / 0.13); padding:12px 20px 26px;">'
        '    <div style="width:38px; height:4px; border-radius:999px; background:%s; margin:0 auto 18px;"></div>%s'
        '  </div>'
        '</div>' % (ghost, CARD, LINE_STRONG, sheet_inner))

# ------------------------------------------------------------------- Sign in
body = frame('''
<div style="padding:66px 26px 0; flex-grow:1; display:flex; flex-direction:column;">
  <div style="width:44px; height:44px; border-radius:13px; background:%s; display:flex; align-items:center; justify-content:center;">%s</div>
  <div class="serif" style="font-size:38px; line-height:1.08; margin-top:24px;">Keep going,<br>together.</div>
  <div style="font-size:14px; color:%s; margin-top:12px; line-height:1.6; text-wrap:pretty;">A habit tracker for a few friends who actually check on each other.</div>

  <div style="display:flex; flex-direction:column; gap:10px; margin-top:34px;">
    %s
    %s
  </div>

  <div style="display:flex; align-items:center; gap:14px; margin:22px 0;">
    <div style="flex-grow:1; height:1px; background:%s;"></div>
    <span style="font-size:11px; color:%s;">or</span>
    <div style="flex-grow:1; height:1px; background:%s;"></div>
  </div>

  <div style="display:flex; flex-direction:column; gap:10px;">
    %s
    %s
  </div>
  %s

  <div style="margin-top:auto; padding:26px 0 32px; text-align:center;">
    <span style="font-size:12.5px; color:%s;">No account yet? </span>
    <span style="font-size:12.5px; font-weight:600; color:%s;">Create one</span>
  </div>
</div>''' % (TERRA, icon('check', 24, 2.6, ON_TERRA), INK2,
             field('Email', 'mohamed@example.com', ico='mail'),
             field('Password', '••••••••••', ico='key'),
             LINE, INK3, LINE,
             btn('Sign in', 'primary'),
             btn('Continue with Google', 'secondary'),
             spacer(16) + note('Sessions last 90 days on this device. We never post anything anywhere.', 'grey', 'lock'),
             INK2, TERRA))
write('SignIn.dc.html', body)

# ------------------------------------------------------------- Create account
body = frame(topbar('left', 'Create account') + '''
<div style="padding:18px 26px 0; flex-grow:1; display:flex; flex-direction:column;">
  <div class="serif" style="font-size:32px; line-height:1.08;">Two fields and a<br>time zone.</div>
  <div style="font-size:13px; color:%s; margin-top:10px; line-height:1.6;">The time zone matters more than it sounds &mdash; it decides when your day rolls over.</div>

  <div style="display:flex; flex-direction:column; gap:10px; margin-top:26px;">
    %s %s %s
    <div style="display:flex; gap:10px;">
      <div style="flex-grow:1;">%s</div>
      <div style="flex-grow:1;">%s</div>
    </div>
  </div>

  %s

  <div style="display:flex; align-items:flex-start; gap:11px; margin-top:22px;">
    <div style="width:22px; height:22px; border-radius:7px; background:%s; display:flex; align-items:center; justify-content:center; color:%s; flex-shrink:0;">%s</div>
    <div style="font-size:11.5px; color:%s; line-height:1.55;">I understand my habit data is visible to any group I join, for the habits I mark as shared.</div>
  </div>

  <div style="margin-top:auto; padding:24px 0 30px;">%s</div>
</div>''' % (INK2,
             field('Name', 'Mohamed Khadra'),
             field('Email', 'mohamed@example.com', ico='mail'),
             field('Password', '••••••••••', ico='key'),
             field('Time zone', 'Africa / Cairo', ico='pin'),
             field('Day starts', '04:00', ico='clock'),
             spacer(14) + note('Day starts at 04:00 means a 1am log still counts for the night before. Night owls should change this.', 'terra', 'info'),
             SAGE, ON_SAGE, icon('check', 14, 3), INK2,
             btn('Create account', 'primary')))
write('CreateAccount.dc.html', body)

# ------------------------------------------------------- Onboarding: habits
def starter(name, sub, ic, picked=False):
    bd = TERRA if picked else LINE
    bg = TERRA_SOFT if picked else CARD
    mark = ('<div style="width:22px; height:22px; border-radius:999px; background:%s; display:flex; align-items:center; justify-content:center; color:%s;">%s</div>' % (TERRA, ON_TERRA, icon('check', 13, 3))) \
        if picked else '<div style="width:22px; height:22px; border-radius:999px; border:1.5px solid %s;"></div>' % LINE_STRONG
    return ('<div style="display:flex; align-items:center; gap:12px; padding:13px 14px; background:%s; '
            'border:1.5px solid %s; border-radius:14px; min-height:44px;">'
            '<div style="width:34px; height:34px; border-radius:10px; background:%s; display:flex; align-items:center; '
            'justify-content:center; color:%s; flex-shrink:0;">%s</div>'
            '<div style="flex-grow:1;"><div style="font-size:14px; font-weight:500;">%s</div>'
            '<div style="font-size:11px; color:%s; margin-top:2px;">%s</div></div>%s</div>'
            % (bg, bd, SUNK, INK2, icon(ic, 17, 1.9), name, INK3, sub, mark))

body = frame('''
<div style="padding:46px 24px 0; flex-grow:1; display:flex; flex-direction:column;">
  <div style="display:flex; gap:6px;">
    <div style="flex-grow:1; height:4px; border-radius:999px; background:%s;"></div>
    <div style="flex-grow:1; height:4px; border-radius:999px; background:%s;"></div>
    <div style="flex-grow:1; height:4px; border-radius:999px; background:%s;"></div>
  </div>
  <div class="cap" style="padding-top:22px;">Step 1 of 3</div>
  <div class="serif" style="font-size:32px; line-height:1.08; margin-top:7px;">Pick two. Not five.</div>
  <div style="font-size:13px; color:%s; margin-top:10px; line-height:1.6; text-wrap:pretty;">
    Everyone starts with six and quits in a fortnight. You can add more once these are boring.</div>

  <div style="display:flex; flex-direction:column; gap:9px; margin-top:22px;">%s%s%s%s%s</div>

  %s

  <div style="margin-top:auto; padding:22px 0 30px; display:flex; gap:10px;">
    <div style="width:112px;">%s</div>
    <div style="flex-grow:1;">%s</div>
  </div>
</div>''' % (TERRA, TERRA, LINE, INK2,
             starter('Morning run', 'A few times a week', 'run', True),
             starter('Read', 'A page count each day', 'book', True),
             starter('Meditate', 'Ten quiet minutes', 'clock'),
             starter('No phone after 22:00', 'Something to stop doing', 'moon'),
             starter('Write my own', 'Anything you like', 'plus'),
             spacer(16) + note('Two chosen. That is the right number.', 'sage', 'check'),
             btn('Skip', 'secondary'), btn('Continue', 'primary')))
write('OnboardHabits.dc.html', body)

# -------------------------------------------------------- Onboarding: group
body = frame('''
<div style="padding:46px 24px 0; flex-grow:1; display:flex; flex-direction:column;">
  <div style="display:flex; gap:6px;">
    <div style="flex-grow:1; height:4px; border-radius:999px; background:%s;"></div>
    <div style="flex-grow:1; height:4px; border-radius:999px; background:%s;"></div>
    <div style="flex-grow:1; height:4px; border-radius:999px; background:%s;"></div>
  </div>
  <div class="cap" style="padding-top:22px;">Step 2 of 3</div>
  <div class="serif" style="font-size:32px; line-height:1.08; margin-top:7px;">Who is doing this<br>with you?</div>
  <div style="font-size:13px; color:%s; margin-top:10px; line-height:1.6; text-wrap:pretty;">
    This is the part that actually works. Alone, most people stop by week six.</div>

  <div style="display:flex; flex-direction:column; gap:10px; margin-top:24px;">
    %s
    %s
  </div>

  %s

  <div style="margin-top:auto; padding:22px 0 30px;">
    <div style="text-align:center; font-size:12.5px; color:%s;">I will do this on my own for now</div>
  </div>
</div>''' % (TERRA, TERRA, LINE, INK2,
             btn('Start a group', 'primary', 'users', sub='Invite three or four people by link'),
             btn('Join with a code', 'secondary', 'link', sub='Someone already sent you one'),
             spacer(18) + note('Three to five people is the sweet spot. Big groups stop feeling personal and nobody notices when you go quiet.', 'terra', 'info'),
             INK2))
write('OnboardGroup.dc.html', body)

# ------------------------------------------------------------ Invite accept
body = frame('''
<div style="padding:70px 26px 0; flex-grow:1; display:flex; flex-direction:column; align-items:center; text-align:center;">
  <div style="display:flex; align-items:center;">%s</div>
  <div class="cap" style="padding-top:24px;">You have been invited</div>
  <div class="serif" style="font-size:36px; line-height:1.08; margin-top:9px;">Sunrise Club</div>
  <div style="font-size:13.5px; color:%s; margin-top:12px; line-height:1.6; max-width:290px; text-wrap:pretty;">
    Yasmin, Adam, Sara and Hussein have been going since April. They are at 71%% between them.</div>

  <div style="width:100%%; margin-top:30px;">%s</div>

  <div style="width:100%%; display:flex; flex-direction:column; gap:10px; margin-top:26px;">
    %s
    %s
  </div>

  <div style="margin-top:auto; padding:24px 0 32px; font-size:11.5px; color:%s; line-height:1.6; max-width:300px;">
    Joining shows them the habits you mark as shared. Everything else stays private, and you can leave whenever.</div>
</div>''' % (stack(['Y','A','S','H'], 46, PAPER, 12), INK2,
             card('<div style="display:flex; align-items:center; justify-content:space-between;">'
                  '<div style="text-align:left;"><div style="font-size:11.5px; color:%s;">This week</div>'
                  '<div class="serif" style="font-size:26px; margin-top:3px;">24 of 35</div></div>%s</div>'
                  % (INK3, daydots('xxoxxo.', 17, 6)), pad='16px 18px'),
             btn('Join Sunrise Club', 'primary'),
             btn('Have a look first', 'secondary'), INK4))
write('InviteAccept.dc.html', body)

# --------------------------------------------------------------- Today empty
body = frame(
  header('Sunday', '23 August', '<div style="width:40px; height:40px; border-radius:999px; background:%s; display:flex; align-items:center; justify-content:center; font-size:13px; font-weight:600; color:%s;">MK</div>' % (TERRA_SOFT, TERRA_DEEP))
  + '''
<div style="flex-grow:1; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:0 34px; text-align:center;">
  <div style="display:flex; gap:8px;">
    <div style="width:26px; height:26px; border-radius:8px; border:1.5px dashed %s;"></div>
    <div style="width:26px; height:26px; border-radius:8px; border:1.5px dashed %s;"></div>
    <div style="width:26px; height:26px; border-radius:8px; border:2px solid %s;"></div>
  </div>
  <div class="serif" style="font-size:28px; line-height:1.15; margin-top:26px;">Nothing to track yet.</div>
  <div style="font-size:13px; color:%s; margin-top:11px; line-height:1.6; text-wrap:pretty;">
    Start with one thing you already half do. The ones you pick out of guilt never survive the month.</div>
  <div style="width:100%%; margin-top:26px;">%s</div>
  <div style="font-size:12px; color:%s; margin-top:16px;">or copy a habit from Sunrise Club</div>
</div>''' % (LINE_STRONG, LINE_STRONG, TERRA, INK2, btn('Add your first habit', 'primary', 'plus'), TERRA)
  + nav('today', badge_group=False))
write('TodayEmpty.dc.html', body)

# ------------------------------------------------------------ Today all done
body = frame(
  header('Sunday', '23 August', '<div style="width:40px; height:40px; border-radius:999px; background:%s; display:flex; align-items:center; justify-content:center; font-size:13px; font-weight:600; color:%s;">MK</div>' % (TERRA_SOFT, TERRA_DEEP))
  + '<div style="padding:20px 20px 0;">%s</div>' % card(
      '<div style="display:flex; align-items:center; gap:15px;">'
      '<div style="width:46px; height:46px; border-radius:999px; background:%s; display:flex; align-items:center; justify-content:center; color:%s; flex-shrink:0;">%s</div>'
      '<div><div class="serif" style="font-size:24px; line-height:1.15;">That is the lot.</div>'
      '<div style="font-size:12px; color:%s; margin-top:4px;">Four of four, and it is only 09:20.</div></div></div>'
      % (SAGE, ON_SAGE, icon('check', 24, 2.8), INK2), pad='18px', bg=SAGE_SOFT, border=False)
  + cap('Done today', '26px 20px 11px')
  + col([
      habit_row('Morning run', '5.2 km &middot; 06:40', 'done', stack(['Y','A','H'])),
      habit_row('Read', '20 of 20 pages', 'done', stack(['A'])),
      habit_row('Meditate', '11 minutes', 'done'),
      habit_row('No phone after 22:00', '7 clean nights', 'breaking', chip('On track', 'plum')),
    ])
  + '<div style="padding:22px 20px 0;">%s</div>' % note(
      'Nothing else is due. We are not going to invent something for you to do.', 'grey', 'info')
  + nav('today'))
write('TodayAllDone.dc.html', body)

# ------------------------------------------------------------- Sheet: amount
inner = ('<div style="display:flex; align-items:center; gap:12px;">'
         '<div style="width:38px; height:38px; border-radius:11px; background:%s; display:flex; align-items:center; justify-content:center; color:%s;">%s</div>'
         '<div style="flex-grow:1;"><div style="font-size:15px; font-weight:600;">Read</div>'
         '<div style="font-size:11.5px; color:%s; margin-top:2px;">Target 20 pages</div></div>'
         '<button style="width:34px; height:34px; border-radius:999px; border:1px solid %s; background:transparent; display:flex; align-items:center; justify-content:center; color:%s; cursor:pointer; padding:0;">%s</button></div>'
         % (SUNK, INK2, icon('book', 19, 1.9), INK3, LINE, INK2, icon('x', 16, 2.2))
  + '<div style="display:flex; align-items:center; justify-content:center; gap:26px; padding:30px 0 6px;">'
    '<button style="width:52px; height:52px; border-radius:999px; border:1.5px solid %s; background:%s; color:%s; display:flex; align-items:center; justify-content:center; cursor:pointer; padding:0;">%s</button>'
    '<div style="text-align:center;"><div class="serif" style="font-size:60px; line-height:0.9;">12</div>'
    '<div style="font-size:11.5px; color:%s; margin-top:7px;">pages</div></div>'
    '<button style="width:52px; height:52px; border-radius:999px; border:1.5px solid %s; background:%s; color:%s; display:flex; align-items:center; justify-content:center; cursor:pointer; padding:0;">%s</button></div>'
    % (LINE, SUNK, INK, icon('minus', 22, 2.4), INK3, TERRA, TERRA_SOFT, TERRA_DEEP, icon('plus', 22, 2.4))
  + '<div style="width:100%%; height:8px; border-radius:999px; background:%s; overflow:hidden; margin-top:18px;">'
    '<div style="width:60%%; height:8px; border-radius:999px; background:%s;"></div></div>'
    % (LINE_SOFT, SAGE_MID)
  + '<div style="display:flex; justify-content:space-between; margin-top:8px;">'
    '<span style="font-size:11px; color:%s;">60%% of today\'s target</span>'
    '<span style="font-size:11px; color:%s;">8 to go</span></div>' % (INK3, INK3)
  + '<div style="display:flex; gap:8px; margin-top:18px;">%s%s%s</div>'
    % (chip('+5', 'neutral'), chip('+10', 'neutral'), chip('Set to 20', 'sage'))
  + '<div style="display:flex; align-items:center; gap:10px; padding:16px 14px; border:1px dashed %s; border-radius:14px; margin-top:18px; color:%s;">%s'
    '<span style="font-size:12.5px; color:%s;">Add a note</span></div>' % (LINE_STRONG, INK3, icon('note', 17, 1.9), INK3)
  + '<div style="margin-top:18px;">%s</div>' % btn('Log 12 pages', 'primary')
  + '<div style="text-align:center; margin-top:14px; font-size:12px; color:%s;">Partial counts. It is not nothing.</div>' % INK3)
write('SheetAmount.dc.html', sheet_screen(inner))

# -------------------------------------------------------------- Sheet: timer
inner = ('<div style="display:flex; align-items:center; gap:12px;">'
         '<div style="width:38px; height:38px; border-radius:11px; background:%s; display:flex; align-items:center; justify-content:center; color:%s;">%s</div>'
         '<div style="flex-grow:1;"><div style="font-size:15px; font-weight:600;">Meditate</div>'
         '<div style="font-size:11.5px; color:%s; margin-top:2px;">Target 10 minutes</div></div>'
         '<button style="width:34px; height:34px; border-radius:999px; border:1px solid %s; background:transparent; display:flex; align-items:center; justify-content:center; color:%s; cursor:pointer; padding:0;">%s</button></div>'
         % (SUNK, INK2, icon('clock', 19, 1.9), INK3, LINE, INK2, icon('x', 16, 2.2))
  + '<div style="display:flex; justify-content:center; padding:26px 0 4px;">'
    '<div style="width:186px; height:186px; border-radius:999px; border:3px solid %s; position:relative; display:flex; align-items:center; justify-content:center;">'
    '<div style="position:absolute; inset:-3px; border-radius:999px; background: conic-gradient(%s 0turn 0.62turn, transparent 0.62turn 1turn); '
    '-webkit-mask: radial-gradient(circle, transparent 89px, black 90px); mask: radial-gradient(circle, transparent 89px, black 90px);"></div>'
    '<div style="text-align:center; position:relative;"><div class="serif" style="font-size:52px; line-height:0.92;">6:12</div>'
    '<div style="font-size:11px; color:%s; margin-top:7px;">of 10:00</div></div></div></div>'
    % (LINE_SOFT, SAGE, INK3)
  + '<div style="display:flex; justify-content:center; gap:12px; margin-top:22px;">'
    '<button style="width:54px; height:54px; border-radius:999px; border:1.5px solid %s; background:%s; color:%s; display:flex; align-items:center; justify-content:center; cursor:pointer; padding:0;">%s</button>'
    '<button style="height:54px; padding:0 26px; border-radius:999px; border:none; background:%s; color:%s; font-family:inherit; font-size:14px; font-weight:600; display:flex; align-items:center; gap:9px; cursor:pointer;">%s Pause</button>'
    '</div>' % (LINE, SUNK, INK, icon('x', 20, 2.2), TERRA, ON_TERRA, icon('pause', 18, 2.4, ON_TERRA))
  + '<div style="margin-top:20px;">%s</div>' % btn('Finish early &mdash; log 6 minutes', 'secondary')
  + '<div style="margin-top:16px;">%s</div>' % note('Six minutes beats a skipped day, and it keeps the week intact.', 'sage', 'check'))
write('SheetTimer.dc.html', sheet_screen(inner))

# --------------------------------------------------------------- Sheet: skip
def reason(label, sub, ic, sel=False):
    bd = TERRA if sel else LINE
    bg = TERRA_SOFT if sel else CARD
    dot = ('<div style="width:18px; height:18px; border-radius:999px; border:5px solid %s; flex-shrink:0;"></div>' % TERRA) \
        if sel else '<div style="width:18px; height:18px; border-radius:999px; border:1.5px solid %s; flex-shrink:0;"></div>' % LINE_STRONG
    return ('<div style="display:flex; align-items:center; gap:12px; padding:13px 14px; background:%s; border:1.5px solid %s; '
            'border-radius:14px; min-height:44px;">%s<div style="width:30px; height:30px; border-radius:9px; background:%s; '
            'display:flex; align-items:center; justify-content:center; color:%s; flex-shrink:0;">%s</div>'
            '<div style="flex-grow:1;"><div style="font-size:13.5px; font-weight:500;">%s</div>'
            '<div style="font-size:11px; color:%s; margin-top:2px;">%s</div></div></div>'
            % (bg, bd, dot, SUNK, INK2, icon(ic, 16, 1.9), label, INK3, sub))

inner = ('<div style="display:flex; align-items:center; gap:12px;">'
         '<div style="flex-grow:1;"><div style="font-size:15px; font-weight:600;">Skip today</div>'
         '<div style="font-size:11.5px; color:%s; margin-top:2px;">Gym &middot; Sunday 23 August</div></div>'
         '<button style="width:34px; height:34px; border-radius:999px; border:1px solid %s; background:transparent; display:flex; align-items:center; justify-content:center; color:%s; cursor:pointer; padding:0;">%s</button></div>'
         % (INK3, LINE, INK2, icon('x', 16, 2.2))
  + '<div style="margin-top:16px;">%s</div>' % note(
      'A skip is not a miss. It leaves today out of the sum entirely, so your consistency does not move at all.', 'sage', 'check')
  + '<div class="cap" style="padding:20px 0 10px;">Why, roughly</div>'
  + '<div style="display:flex; flex-direction:column; gap:8px;">%s%s%s%s</div>'
    % (reason('Travelling', 'Away from the usual set-up', 'pin', True),
       reason('Ill or injured', 'Resting is the correct move', 'heart'),
       reason('Rest day', 'Planned, not a slip', 'moon'),
       reason('Just not today', 'No reason needed', 'flag'))
  + '<div style="display:flex; gap:10px; margin-top:20px;">'
    '<div style="width:118px;">%s</div><div style="flex-grow:1;">%s</div></div>'
    % (btn('Cancel', 'secondary'), btn('Skip today', 'primary'))
  + '<div style="text-align:center; margin-top:13px; font-size:11.5px; color:%s;">You have used 1 of 2 skips this week</div>' % INK3)
write('SheetSkip.dc.html', sheet_screen(inner, 4))
print('onboarding + daily ok')
