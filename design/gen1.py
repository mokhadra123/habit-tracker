# -*- coding: utf-8 -*-
from _kit import *

# ---------------------------------------------------------------- Foundations
def swatch(name, val, note=''):
    return ('<div style="display:flex; flex-direction:column; gap:7px;">'
            '<div style="height:56px; border-radius:11px; background:%s; border:1px solid %s;"></div>'
            '<div><div style="font-size:11.5px; font-weight:600;">%s</div>'
            '<div style="font-size:9.5px; color:%s; margin-top:2px; font-variant-numeric:tabular-nums;">%s</div></div></div>'
            % (val, LINE, name, INK4, note or val.replace('oklch(', '').replace(')', '')))

pal_core = [('Paper', PAPER), ('Card', CARD), ('Sunk', SUNK), ('Line', LINE), ('Ink', INK), ('Ink muted', INK2)]
pal_acc  = [('Terracotta', TERRA), ('Terracotta soft', TERRA_SOFT), ('Sage', SAGE), ('Sage soft', SAGE_SOFT),
            ('Plum', PLUM), ('Amber', AMBER)]
ramp = [('Display', 'serif', 40, '23 August'), ('Title', 'serif', 30, 'Morning run'),
        ('Metric', 'serif', 46, '86%'), ('Body', '', 15, 'Read 20 pages a day'),
        ('Secondary', '', 12.5, 'Four times a week, three done'),
        ('Caption', '', 11, 'Wednesday was a rest day'), ('Label', 'cap', 10, 'This week')]

rows = []
for nm, cls, sz, txt in ramp:
    c = 'class="serif"' if cls == 'serif' else ('class="cap"' if cls == 'cap' else '')
    rows.append('<div style="display:flex; align-items:baseline; gap:22px; padding:9px 0; border-bottom:1px solid %s;">'
                '<div style="width:88px; font-size:10.5px; color:%s; flex-shrink:0;">%s</div>'
                '<div style="width:46px; font-size:10.5px; color:%s; flex-shrink:0;">%spx</div>'
                '<div %s style="font-size:%spx; line-height:1.15;">%s</div></div>'
                % (LINE_SOFT, INK3, nm, INK4, sz, c, sz, txt))

ic_names = ['check','plus','minus','x','right','left','calendar','list','users','user','bell','bell-off',
            'lock','clock','moon','book','run','bars','trend','info','alert','sparkle','heart','mail',
            'camera','note','archive','trash','download','settings','link','copy','play','pause','skip',
            'search','wifi-off','key','pin','flag','down']
ic_cells = ''.join('<div style="display:flex; flex-direction:column; align-items:center; gap:6px;">'
                   '<div style="width:38px; height:38px; border-radius:10px; background:%s; border:1px solid %s; '
                   'display:flex; align-items:center; justify-content:center; color:%s;">%s</div>'
                   '<span style="font-size:8px; color:%s;">%s</span></div>'
                   % (CARD, LINE, INK, icon(n, 19, 1.9), INK4, n) for n in ic_names)

body = frame('''
<div style="padding:34px 36px;">
  <div class="cap">Foundations</div>
  <div class="serif" style="font-size:34px; line-height:1.05; margin-top:6px;">Warm paper, one accent</div>
  <div style="font-size:13.5px; color:%s; margin-top:10px; max-width:560px; line-height:1.6; text-wrap:pretty;">
    Terracotta is the only action colour. Sage means completed and nothing else. Nothing in the system is red
    for a missed day &mdash; absence is drawn as an empty square, never as an error.</div>

  <div style="display:grid; grid-template-columns:repeat(6, minmax(0, 1fr)); gap:14px; margin-top:30px;">%s</div>
  <div style="display:grid; grid-template-columns:repeat(6, minmax(0, 1fr)); gap:14px; margin-top:16px;">%s</div>

  <div style="display:flex; gap:44px; margin-top:36px; align-items:flex-start;">
    <div style="flex-grow:1; min-width:0;">
      <div class="cap" style="padding-bottom:8px;">Type &mdash; Instrument Serif + Archivo</div>
      %s
    </div>
    <div style="width:300px; flex-shrink:0;">
      <div class="cap" style="padding-bottom:12px;">Completion scale</div>
      <div style="display:flex; gap:7px; align-items:center;">
        <div style="width:30px; height:30px; border-radius:8px; background:%s;"></div>
        <div style="width:30px; height:30px; border-radius:8px; background:%s;"></div>
        <div style="width:30px; height:30px; border-radius:8px; background:%s;"></div>
        <div style="width:30px; height:30px; border-radius:8px; background:%s;"></div>
        <div style="width:30px; height:30px; border-radius:8px; background:%s;"></div>
        <div style="width:30px; height:30px; border-radius:8px; border:1.5px dashed %s;"></div>
        <div style="width:30px; height:30px; border-radius:8px; border:2px solid %s;"></div>
      </div>
      <div style="font-size:10.5px; color:%s; margin-top:9px; line-height:1.6;">
        none &middot; light &middot; mid &middot; strong &middot; full &middot; <strong>skipped</strong> &middot; <strong>today</strong></div>
      <div class="cap" style="padding:26px 0 12px;">Radius &amp; hit area</div>
      <div style="display:flex; gap:10px; align-items:flex-end;">
        <div style="width:44px; height:44px; border-radius:10px; border:1.5px solid %s;"></div>
        <div style="width:44px; height:44px; border-radius:14px; border:1.5px solid %s;"></div>
        <div style="width:44px; height:44px; border-radius:16px; border:1.5px solid %s;"></div>
        <div style="width:44px; height:44px; border-radius:999px; border:1.5px solid %s;"></div>
      </div>
      <div style="font-size:10.5px; color:%s; margin-top:9px;">10 controls &middot; 14 fields &middot; 16 cards &middot; full circles. Never below 44px.</div>
    </div>
  </div>

  <div class="cap" style="padding:34px 0 12px;">Icons &mdash; 24px grid, 1.9 stroke, never emoji</div>
  <div style="display:grid; grid-template-columns:repeat(14, minmax(0, 1fr)); gap:11px;">%s</div>
</div>''' % (INK2,
             ''.join(swatch(n, v) for n, v in pal_core),
             ''.join(swatch(n, v) for n, v in pal_acc),
             ''.join(rows),
             EMPTY, SAGE_PALE, SAGE_MID, 'oklch(0.68 0.095 155)', SAGE, LINE_STRONG, TERRA, INK2,
             LINE_STRONG, LINE_STRONG, LINE_STRONG, LINE_STRONG, INK2,
             ic_cells), w=1080, minh=980)
write('Foundations.dc.html', body)

# ---------------------------------------------------------------- Components
def grp(title, inner, note_=''):
    n = ('<div style="font-size:10.5px; color:%s; margin-top:9px; line-height:1.5;">%s</div>' % (INK4, note_)) if note_ else ''
    return ('<div><div class="cap" style="padding-bottom:11px;">%s</div>'
            '<div style="display:flex; flex-wrap:wrap; gap:10px; align-items:center;">%s</div>%s</div>'
            % (title, inner, n))

body = frame('''
<div style="padding:34px 36px;">
  <div class="cap">Components</div>
  <div class="serif" style="font-size:34px; line-height:1.05; margin-top:6px;">Every control, every state</div>

  <div style="display:grid; grid-template-columns:repeat(2, minmax(0, 1fr)); gap:34px 44px; margin-top:30px;">
    %s %s %s %s %s %s
  </div>

  <div class="cap" style="padding:34px 0 12px;">Fields</div>
  <div style="display:grid; grid-template-columns:repeat(3, minmax(0, 1fr)); gap:12px;">%s %s %s</div>

  <div class="cap" style="padding:30px 0 12px;">Week strip &mdash; the five cell states</div>
  <div style="display:flex; gap:34px; align-items:center;">
    %s
    <div style="font-size:11px; color:%s; line-height:1.7;">
      filled = done &middot; mid = partial &middot; empty = nothing logged<br>
      dashed = deliberately skipped &middot; ringed = today</div>
  </div>
</div>''' % (
  grp('Buttons', btn('Save habit', 'primary', full=False) + btn('Not now', 'secondary', full=False)
      + btn('Add a habit', 'dashed', 'plus', full=False) + btn('Delete', 'danger', 'trash', full=False)),
  grp('Chips', chip('4× a week', 'sage') + chip('Shared', 'terra', 'users') + chip('Private', 'neutral', 'lock')
      + chip('Breaking', 'plum', 'moon') + chip('Behind', 'amber', 'alert')),
  grp('Toggles', toggle(True) + toggle(False), 'On uses sage, never terracotta &mdash; it reports a state, it is not an action.'),
  grp('Avatars', stack(['Y','A','S','H'], 30) + avatar('M', 40) + avatar('Y', 30) + avatar('S', 24)),
  grp('Reactions', '<div style="display:flex; gap:7px;">'
      + '<div style="height:30px; padding:0 11px; border-radius:999px; background:%s; display:flex; align-items:center; gap:6px; color:%s; font-size:11.5px; font-weight:600;">%s3</div>' % (TERRA_SOFT, TERRA_DEEP, solid('sparkle', 13))
      + '<div style="height:30px; padding:0 11px; border-radius:999px; border:1px solid %s; display:flex; align-items:center; gap:6px; color:%s; font-size:11.5px;">%s1</div>' % (LINE, INK2, icon('heart', 13, 2))
      + '<button style="width:30px; height:30px; border-radius:999px; border:1px dashed %s; background:transparent; display:flex; align-items:center; justify-content:center; color:%s; cursor:pointer; padding:0;">%s</button>' % (LINE_STRONG, INK3, icon('plus', 13, 2.2))
      + '</div>', 'Positive only. There is no downvote and there never will be.'),
  grp('Progress', '<div style="width:150px; height:7px; border-radius:999px; background:%s; overflow:hidden;">'
      '<div style="width:72%%; height:7px; border-radius:999px; background:%s;"></div></div>' % (LINE_SOFT, SAGE)
      + '<div style="width:44px; height:44px; border-radius:999px; border:2.5px solid %s; display:flex; align-items:center; justify-content:center; font-size:12px; font-weight:600;">12</div>' % SAGE_MID),
  field('Habit name', 'Swim', caret=True),
  field('Reminder', '07:00', ico='clock'),
  field('Email', 'you@example.com', ico='mail', placeholder=True),
  daydots('xxosxt.'), INK2), w=1080, minh=760)
write('Components.dc.html', body)

# ---------------------------------------------------------------- Row states
states = [
    ('Not done yet', habit_row('Meditate', '10 minutes &middot; every day', 'todo',
        '<button style="height:30px; padding:0 12px; border-radius:999px; border:1px solid %s; background:transparent; font-family:inherit; font-size:11.5px; color:%s; cursor:pointer;">Skip</button>' % (LINE, INK2))),
    ('Done', habit_row('Morning run', '4&times; a week &middot; 3 done', 'done', stack(['Y','A','H']))),
    ('Partial &mdash; counts, not a failure', habit_row('Read', '12 of 20 pages', 'partial',
        '<button style="width:44px; height:44px; border-radius:12px; border:1px solid %s; background:%s; color:%s; display:flex; align-items:center; justify-content:center; cursor:pointer; padding:0;">%s</button>' % (LINE, SUNK, INK, icon('plus', 19, 2)), mark='12')),
    ('Skipped on purpose', habit_row('Gym', 'Skipped &middot; travelling', 'skipped', chip('Skipped', 'neutral'))),
    ('Missed &mdash; still no red', habit_row('Journal', 'Missed Tuesday &middot; 1 forgiveness left', 'missed', chip('1 left', 'amber'))),
    ('Breaking a habit', habit_row('No phone after 22:00', 'Breaking &middot; 6 clean nights', 'breaking', chip('Tonight', 'plum'))),
    ('Behind for the week', habit_row('Swim', '1 of 3 this week', 'todo', chip('2 to go', 'amber'), tint=AMBER_SOFT)),
]
items = ''.join('<div><div class="cap" style="padding-bottom:8px;">%s</div>%s</div>' % (t, r) for t, r in states)
body = frame('''
<div style="padding:30px 24px;">
  <div class="cap">The habit row</div>
  <div class="serif" style="font-size:28px; line-height:1.08; margin-top:6px;">One component, seven states</div>
  <div style="font-size:12px; color:%s; margin-top:9px; line-height:1.6; text-wrap:pretty;">
    The control on the left is always 44&thinsp;px and always in the same place, so logging is muscle memory.</div>
  <div style="display:flex; flex-direction:column; gap:18px; margin-top:24px;">%s</div>
</div>''' % (INK2, items), w=440, minh=880)
write('HabitRowStates.dc.html', body)
print('foundations ok')
