# -*- coding: utf-8 -*-
"""Shared token + component kit for the habit tracker design canvas."""

PAPER      = 'oklch(0.982 0.008 80)'
PAPER_WARM = 'oklch(0.975 0.014 70)'
CARD       = 'oklch(0.999 0.003 80)'
SUNK       = 'oklch(0.9725 0.010 80)'
INK        = 'oklch(0.24 0.018 55)'
INK2       = 'oklch(0.50 0.014 55)'
INK3       = 'oklch(0.66 0.010 55)'
INK4       = 'oklch(0.72 0.010 55)'
LINE       = 'oklch(0.905 0.010 80)'
LINE_SOFT  = 'oklch(0.93 0.008 80)'
LINE_STRONG= 'oklch(0.86 0.012 80)'

TERRA      = 'oklch(0.58 0.12 45)'
TERRA_DEEP = 'oklch(0.46 0.11 45)'
TERRA_SOFT = 'oklch(0.955 0.024 45)'
TERRA_MID  = 'oklch(0.90 0.045 45)'
ON_TERRA   = 'oklch(0.99 0.008 45)'

SAGE       = 'oklch(0.58 0.10 155)'
SAGE_DEEP  = 'oklch(0.44 0.09 155)'
SAGE_SOFT  = 'oklch(0.945 0.028 155)'
SAGE_MID   = 'oklch(0.79 0.075 155)'
SAGE_PALE  = 'oklch(0.885 0.045 155)'
ON_SAGE    = 'oklch(0.99 0.01 155)'

PLUM       = 'oklch(0.52 0.09 280)'
PLUM_SOFT  = 'oklch(0.955 0.020 280)'
AMBER      = 'oklch(0.62 0.11 75)'
AMBER_SOFT = 'oklch(0.955 0.030 75)'
AMBER_DEEP = 'oklch(0.48 0.10 75)'
EMPTY      = 'oklch(0.945 0.006 80)'

PEOPLE = {
    'M': ('MK', 'oklch(0.945 0.030 45)',  'oklch(0.47 0.12 45)',  'Mohamed'),
    'Y': ('Y',  'oklch(0.90 0.045 250)',  'oklch(0.45 0.09 250)', 'Yasmin'),
    'A': ('A',  'oklch(0.91 0.045 320)',  'oklch(0.46 0.09 320)', 'Adam'),
    'S': ('S',  'oklch(0.93 0.020 80)',   'oklch(0.58 0.014 55)', 'Sara'),
    'H': ('H',  'oklch(0.92 0.040 120)',  'oklch(0.44 0.09 120)', 'Hussein'),
}

_P = {
 'check':'<path d="M20 6 9 17l-5-5"/>',
 'plus':'<path d="M12 5v14M5 12h14"/>',
 'minus':'<path d="M5 12h14"/>',
 'x':'<path d="M18 6 6 18M6 6l12 12"/>',
 'right':'<path d="m9 18 6-6-6-6"/>',
 'left':'<path d="m15 18-6-6 6-6"/>',
 'down':'<path d="m6 9 6 6 6-6"/>',
 'calendar':'<rect x="3" y="4.5" width="18" height="17" rx="4"/><path d="M8 2.5v4M16 2.5v4M3 10h18"/>',
 'list':'<path d="M4 6.5h16M4 12h16M4 17.5h16"/>',
 'users':'<path d="M16 20v-1.5a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4V20"/><circle cx="9" cy="7" r="3.6"/><path d="M22 20v-1.5a4 4 0 0 0-3-3.85"/><path d="M16.5 3.6a4 4 0 0 1 0 7"/>',
 'user':'<circle cx="12" cy="8" r="4"/><path d="M4.5 20.5a7.5 7.5 0 0 1 15 0"/>',
 'bell':'<path d="M18 8.5a6 6 0 1 0-12 0c0 6.5-2.6 8.5-2.6 8.5h17.2S18 15 18 8.5"/><path d="M13.7 20.5a2 2 0 0 1-3.4 0"/>',
 'bell-off':'<path d="M8.7 4.2A6 6 0 0 1 18 8.5c0 2 .25 3.5.6 4.6M5.9 6.9C6 7.4 6 8 6 8.5c0 6.5-2.6 8.5-2.6 8.5h13.4"/><path d="M13.7 20.5a2 2 0 0 1-3.4 0"/><path d="m2.5 2.5 19 19"/>',
 'lock':'<rect x="4" y="11" width="16" height="10" rx="3"/><path d="M8 11V7.5a4 4 0 0 1 8 0V11"/>',
 'clock':'<circle cx="12" cy="13" r="8.2"/><path d="M12 9.4V13l2.3 2.3M9.2 2.6h5.6"/>',
 'moon':'<path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/>',
 'book':'<path d="M4 19.2A2.8 2.8 0 0 1 6.8 16.4H20"/><path d="M6.8 2.5H20v19H6.8A2.8 2.8 0 0 1 4 18.7V5.3a2.8 2.8 0 0 1 2.8-2.8z"/>',
 'run':'<path d="M22 12h-4l-3 8.5L9.5 3.5 6.5 12H2"/>',
 'bars':'<path d="M4 19V9M10 19V5M16 19v-7M22 19H2"/>',
 'trend':'<path d="m4 16 6-6 4 4 6-7"/><path d="M20 7v4.5h-4.5"/>',
 'info':'<circle cx="12" cy="12" r="9.2"/><path d="M12 16.5v-5"/><circle cx="12" cy="8" r="0.7" fill="currentColor"/>',
 'alert':'<path d="M10.3 3.6 1.9 18a2 2 0 0 0 1.7 3h16.8a2 2 0 0 0 1.7-3L13.7 3.6a2 2 0 0 0-3.4 0z"/><path d="M12 9.5v4"/><circle cx="12" cy="17" r="0.7" fill="currentColor"/>',
 'sparkle':'<path d="M12 3.2l1.9 5.4 5.4 1.9-5.4 1.9L12 17.8l-1.9-5.4L4.7 10.5l5.4-1.9z"/>',
 'heart':'<path d="M20.4 5.1a5 5 0 0 0-7.1 0L12 6.4l-1.3-1.3a5 5 0 1 0-7.1 7.1l8.4 8.3 8.4-8.3a5 5 0 0 0 0-7.1z"/>',
 'mail':'<rect x="2.5" y="4.5" width="19" height="15" rx="3"/><path d="m3.5 6.5 8.5 6 8.5-6"/>',
 'key':'<circle cx="8" cy="15" r="4.5"/><path d="m11.4 11.6 8.1-8.1M17 6l2.5 2.5M14.5 8.5 17 11"/>',
 'camera':'<path d="M3 8.5h3l1.6-2.4h8.8L18 8.5h3v11H3z"/><circle cx="12" cy="13.5" r="3.4"/>',
 'note':'<path d="M4 4.5h16v10l-5 5H4z"/><path d="M20 14.5h-5v5"/>',
 'archive':'<rect x="3" y="4" width="18" height="4.5" rx="1.5"/><path d="M4.5 8.5v10a1.5 1.5 0 0 0 1.5 1.5h12a1.5 1.5 0 0 0 1.5-1.5v-10"/><path d="M10 12.5h4"/>',
 'trash':'<path d="M4 6.5h16M9.5 6.5V4h5v2.5"/><path d="M6 6.5v13a1.5 1.5 0 0 0 1.5 1.5h9a1.5 1.5 0 0 0 1.5-1.5v-13"/><path d="M10 10.5v7M14 10.5v7"/>',
 'download':'<path d="M12 3.5v11"/><path d="m7.5 10.5 4.5 4.5 4.5-4.5"/><path d="M3.5 19.5h17"/>',
 'wifi-off':'<path d="m2.5 2.5 19 19"/><path d="M8.8 15.2a5 5 0 0 1 6.4 0"/><path d="M5.5 11.8a10 10 0 0 1 3.2-2.1M18.5 11.8a10 10 0 0 0-6.8-2.6"/><path d="M2.2 8.3A15 15 0 0 1 7 5.4M21.8 8.3a15 15 0 0 0-7.4-3.2"/><circle cx="12" cy="19" r="0.8" fill="currentColor"/>',
 'settings':'<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.6 1.6 0 0 0 .33 1.8l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.6 1.6 0 0 0-1.8-.33 1.6 1.6 0 0 0-1 1.47V21a2 2 0 1 1-4 0v-.1A1.6 1.6 0 0 0 9 19.4a1.6 1.6 0 0 0-1.8.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.6 1.6 0 0 0 .33-1.8 1.6 1.6 0 0 0-1.47-1H3a2 2 0 1 1 0-4h.1A1.6 1.6 0 0 0 4.6 9a1.6 1.6 0 0 0-.33-1.8l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06A1.6 1.6 0 0 0 9 4.6h.08A1.6 1.6 0 0 0 10.1 3.1V3a2 2 0 1 1 4 0v.1a1.6 1.6 0 0 0 1 1.47 1.6 1.6 0 0 0 1.8-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.6 1.6 0 0 0-.33 1.8v.08a1.6 1.6 0 0 0 1.47 1H21a2 2 0 1 1 0 4h-.1a1.6 1.6 0 0 0-1.5 1.02z"/>',
 'link':'<path d="M10 13.5a4.5 4.5 0 0 0 6.8.5l2.7-2.7a4.5 4.5 0 1 0-6.4-6.4l-1.5 1.5"/><path d="M14 10.5a4.5 4.5 0 0 0-6.8-.5l-2.7 2.7a4.5 4.5 0 1 0 6.4 6.4l1.5-1.5"/>',
 'copy':'<rect x="8.5" y="8.5" width="12" height="12" rx="2.5"/><path d="M15.5 8.5v-3a2 2 0 0 0-2-2h-8a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h3"/>',
 'play':'<path d="M7 4.5 19.5 12 7 19.5z"/>',
 'pause':'<path d="M9 4.5v15M15 4.5v15"/>',
 'skip':'<path d="M6.5 6.5 13 12l-6.5 5.5z"/><path d="M17 6.5v11"/>',
 'search':'<circle cx="11" cy="11" r="7"/><path d="m16.5 16.5 4 4"/>',
 'pin':'<path d="M12 21s7-6.2 7-11a7 7 0 1 0-14 0c0 4.8 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/>',
 'flag':'<path d="M5 21V4.5h11l-1.6 3.5L16 11.5H5"/>',
}

def icon(name, size=18, sw=1.9, stroke='currentColor', fill='none'):
    return ('<svg width="%s" height="%s" viewBox="0 0 24 24" fill="%s" stroke="%s" '
            'stroke-width="%s" stroke-linecap="round" stroke-linejoin="round">%s</svg>'
            % (size, size, fill, stroke, sw, _P[name]))

def solid(name, size=13, color='currentColor'):
    return ('<svg width="%s" height="%s" viewBox="0 0 24 24" fill="%s">%s</svg>'
            % (size, size, color, _P[name]))

HELMET = """<helmet>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600&family=Instrument+Serif:ital@0;1&display=swap">
  <style>
    *{ box-sizing: border-box; }
    body{ margin:0; background: %s; color: %s;
          font-family: Archivo, "Helvetica Neue", Arial, sans-serif; -webkit-font-smoothing: antialiased; }
    a{ color: %s; } a:hover{ color: oklch(0.47 0.12 45); }
    .serif{ font-family: "Instrument Serif", Georgia, serif; font-weight:400; }
    .cap{ font-size:10px; letter-spacing:0.12em; text-transform:uppercase; font-weight:600; color: %s; }
  </style>
</helmet>""" % (PAPER, INK, TERRA, INK3)

def doc(body, script=None, bg=None):
    helmet = HELMET if bg is None else HELMET.replace('background: %s;' % PAPER, 'background: %s;' % bg, 1)
    sc = ''
    if script:
        sc = ('\n<script data-dc-script data-props=\'{}\'>\nclass Component extends DCLogic {\n%s\n}\n</script>'
              % script)
    return ('<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n'
            '  <script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n'
            '%s\n\n%s\n</x-dc>%s\n</body>\n</html>\n' % (helmet, body, sc))

def frame(inner, w=390, minh=880, bg=PAPER, pad='0'):
    return ('<div style="width:%spx; min-height:%spx; display:flex; flex-direction:column; '
            'background: %s; padding:%s;">\n%s\n</div>' % (w, minh, bg, pad, inner))

def cap(t, pad='0'):
    return '<div class="cap" style="padding:%s;">%s</div>' % (pad, t)

def card(inner, pad='16px', bg=CARD, border=LINE, radius=16, style=''):
    b = ('border:1px solid %s; ' % border) if border else ''
    return ('<div style="padding:%s; background:%s; %sborder-radius:%spx; %s">%s</div>'
            % (pad, bg, b, radius, style, inner))

def avatar(k, size=30, ring=None, fs=None):
    ini, tint, ink, _ = PEOPLE[k]
    fs = fs or max(9, int(size * 0.38))
    r = ('border:2px solid %s; ' % ring) if ring else ''
    return ('<div style="width:%spx; height:%spx; border-radius:999px; background:%s; %s'
            'display:flex; align-items:center; justify-content:center; font-size:%spx; '
            'font-weight:600; color:%s; flex-shrink:0;">%s</div>'
            % (size, size, tint, r, fs, ink, ini))

def stack(items, size=24, ring=CARD, overlap=8):
    out = []
    for i, k in enumerate(items):
        ml = '' if i == 0 else ' margin-left:-%spx;' % overlap
        ini, tint, ink, _ = PEOPLE[k]
        out.append('<div style="width:%spx; height:%spx; border-radius:999px; background:%s; '
                   'border:2px solid %s; display:flex; align-items:center; justify-content:center; '
                   'font-size:%spx; font-weight:600; color:%s;%s">%s</div>'
                   % (size, size, tint, ring, max(8, int(size*0.37)), ink, ml, ini))
    return '<div style="display:flex; align-items:center;">%s</div>' % ''.join(out)

def btn(label, kind='primary', ico=None, full=True, h=48, fs=14, sub=None):
    grow = 'width:100%; ' if full else ''
    if kind == 'primary':
        st = 'background:%s; border:1.5px solid %s; color:%s;' % (TERRA, TERRA, ON_TERRA)
    elif kind == 'secondary':
        st = 'background:%s; border:1.5px solid %s; color:%s;' % (CARD, LINE_STRONG, INK)
    elif kind == 'dashed':
        st = 'background:transparent; border:1.5px dashed %s; color:%s;' % (LINE_STRONG, INK2)
    elif kind == 'danger':
        st = 'background:transparent; border:1.5px solid oklch(0.80 0.09 30); color:oklch(0.50 0.14 30);'
    else:
        st = 'background:transparent; border:none; color:%s;' % INK2
    ic = (icon(ico, 17, 2.1) if ico else '')
    inner = label
    if sub:
        inner = ('<div style="text-align:left;"><div style="font-size:%spx; font-weight:600;">%s</div>'
                 '<div style="font-size:11.5px; opacity:0.8; margin-top:3px; line-height:1.4;">%s</div></div>'
                 % (fs, label, sub))
        return ('<button style="%sdisplay:flex; align-items:center; gap:12px; padding:15px 16px; '
                'border-radius:15px; %s font-family:inherit; cursor:pointer; min-height:44px; text-align:left;">'
                '%s<div style="flex-grow:1;">%s</div>%s</button>'
                % (grow, st, ic, inner, icon('right', 17, 2.2)))
    return ('<button style="%smin-height:%spx; padding:0 18px; border-radius:14px; %s '
            'font-family:inherit; font-size:%spx; font-weight:600; display:flex; align-items:center; '
            'justify-content:center; gap:9px; cursor:pointer;">%s%s</button>'
            % (grow, h, st, fs, ic, label))

def chip(label, tone='neutral', ico=None, fs=11):
    m = {'neutral': (SUNK, INK2, LINE),
         'sage':    (SAGE_SOFT, SAGE_DEEP, 'transparent'),
         'terra':   (TERRA_SOFT, TERRA_DEEP, 'transparent'),
         'plum':    (PLUM_SOFT, PLUM, 'transparent'),
         'amber':   (AMBER_SOFT, AMBER_DEEP, 'transparent')}
    bg, fg, bd = m[tone]
    ic = (icon(ico, 12, 2.2) if ico else '')
    return ('<span style="display:inline-flex; align-items:center; gap:5px; font-size:%spx; '
            'font-weight:600; color:%s; background:%s; border:1px solid %s; padding:5px 10px; '
            'border-radius:999px;">%s%s</span>' % (fs, fg, bg, bd, ic, label))

def toggle(on=True):
    if on:
        return ('<div style="width:48px; height:28px; border-radius:999px; background:%s; display:flex; '
                'align-items:center; justify-content:flex-end; padding:3px; flex-shrink:0;">'
                '<div style="width:22px; height:22px; border-radius:999px; background:%s;"></div></div>'
                % (SAGE, 'oklch(0.999 0.004 155)'))
    return ('<div style="width:48px; height:28px; border-radius:999px; background:%s; display:flex; '
            'align-items:center; padding:3px; flex-shrink:0;">'
            '<div style="width:22px; height:22px; border-radius:999px; background:%s;"></div></div>'
            % ('oklch(0.90 0.008 80)', CARD))

def field(label, value, ico=None, placeholder=False, caret=False):
    v = ('<span style="color:%s;">%s</span>' % (INK4, value)) if placeholder else value
    cr = ('<span style="display:inline-block; width:2px; height:17px; background:%s; '
          'vertical-align:-3px; margin-left:1px;"></span>' % TERRA) if caret else ''
    ic = ('%s' % icon(ico, 17, 1.9)) if ico else ''
    bd = TERRA if caret else LINE
    return ('<div style="padding:13px 15px; background:%s; border:1.5px solid %s; border-radius:14px;">'
            '<div class="cap">%s</div>'
            '<div style="display:flex; align-items:center; gap:10px; margin-top:7px; color:%s;">%s'
            '<span style="font-size:15px; color:%s;">%s%s</span></div></div>'
            % (CARD, bd, label, INK3, ic, INK, v, cr))

def nav(active='today', badge_group=True):
    items = [('today', 'Today', 'calendar'), ('habits', 'Habits', 'list'),
             ('group', 'Group', 'users'), ('you', 'You', 'user')]
    out = []
    for key, lab, ic in items:
        on = (key == active)
        col = TERRA_DEEP if on else INK4
        fw = '600' if on else '400'
        dot = ''
        if key == 'group' and badge_group:
            dot = ('<div style="position:absolute; top:2px; right:14px; width:7px; height:7px; '
                   'border-radius:999px; background:%s;"></div>' % TERRA)
        out.append('<div style="min-width:64px; min-height:44px; display:flex; flex-direction:column; '
                   'align-items:center; justify-content:center; gap:4px; color:%s; position:relative;">'
                   '%s<span style="font-size:10px; font-weight:%s;">%s</span>%s</div>'
                   % (col, icon(ic, 21, 1.9), fw, lab, dot))
    return ('<div style="margin-top:auto; border-top:1px solid %s; background:%s; padding:9px 14px 18px; '
            'display:flex; justify-content:space-between;">%s</div>' % (LINE, CARD, ''.join(out)))

def topbar(left='left', title='', right=''):
    l = ('<button style="width:40px; height:40px; margin-left:-9px; border:none; background:transparent; '
         'display:flex; align-items:center; justify-content:center; color:%s; cursor:pointer; padding:0;">%s</button>'
         % (INK, icon(left, 21, 2))) if left else '<div style="width:40px;"></div>'
    r = right or '<div style="width:40px;"></div>'
    t = ('<div style="font-size:13.5px; font-weight:600;">%s</div>' % title) if title else ''
    return ('<div style="display:flex; align-items:center; justify-content:space-between; '
            'padding:22px 20px 0;">%s%s%s</div>' % (l, t, r))

def header(capt, title, right=''):
    r = right or ''
    return ('<div style="display:flex; justify-content:space-between; align-items:flex-start; padding:26px 20px 0;">'
            '<div>%s<div class="serif" style="font-size:32px; line-height:1.04; margin-top:5px;">%s</div></div>'
            '%s</div>' % (cap(capt), title, r))

def daydots(pattern, size=19, gap=7, labels=True):
    L = ['M','T','W','T','F','S','S']
    out = []
    for i, c in enumerate(pattern):
        if c == 'x':   sty = 'background:%s;' % SAGE
        elif c == 'o': sty = 'background:%s;' % SAGE_MID
        elif c == 's': sty = 'border:1.5px dashed %s;' % LINE_STRONG
        elif c == 't': sty = 'border:2px solid %s;' % TERRA
        else:          sty = 'background:%s;' % EMPTY
        lab = ('<span style="font-size:9px; color:%s;">%s</span>' % (INK3, L[i])) if labels else ''
        out.append('<div style="display:flex; flex-direction:column; align-items:center; gap:5px;">%s'
                   '<div style="width:%spx; height:%spx; border-radius:6px; %s"></div></div>'
                   % (lab, size, size, sty))
    return '<div style="display:flex; gap:%spx;">%s</div>' % (gap, ''.join(out))

def habit_row(name, sub, state='todo', right='', tint=None, mark=''):
    if state == 'done':
        ctrl = ('<div style="width:44px; height:44px; border-radius:999px; background:%s; display:flex; '
                'align-items:center; justify-content:center; color:%s; flex-shrink:0;">%s</div>'
                % (SAGE, ON_SAGE, icon('check', 21, 2.6)))
    elif state == 'partial':
        ctrl = ('<div style="width:44px; height:44px; border-radius:999px; border:2.5px solid %s; '
                'display:flex; align-items:center; justify-content:center; flex-shrink:0; font-size:12px; '
                'font-weight:600; color:%s;">%s</div>' % (SAGE_MID, INK, mark))
    elif state == 'skipped':
        ctrl = ('<div style="width:44px; height:44px; border-radius:999px; border:2px dashed %s; '
                'display:flex; align-items:center; justify-content:center; flex-shrink:0; color:%s;">%s</div>'
                % (LINE_STRONG, INK4, icon('skip', 17, 2)))
    elif state == 'breaking':
        ctrl = ('<div style="width:44px; height:44px; border-radius:999px; background:%s; display:flex; '
                'align-items:center; justify-content:center; flex-shrink:0; color:%s;">%s</div>'
                % (PLUM_SOFT, PLUM, icon('moon', 19, 1.8)))
    elif state == 'missed':
        ctrl = ('<div style="width:44px; height:44px; border-radius:999px; border:2px solid %s; '
                'display:flex; align-items:center; justify-content:center; flex-shrink:0; color:%s;">%s</div>'
                % ('oklch(0.88 0.03 30)', 'oklch(0.66 0.07 30)', icon('x', 17, 2.2)))
    else:
        ctrl = ('<button style="width:44px; height:44px; border-radius:999px; border:2px dashed %s; '
                'background:transparent; flex-shrink:0; cursor:pointer; padding:0;"></button>' % LINE_STRONG)
    op = ' opacity:0.72;' if state == 'skipped' else ''
    bg = tint or CARD
    return ('<div style="display:flex; align-items:center; gap:13px; padding:14px; background:%s; '
            'border:1px solid %s; border-radius:16px;%s">%s'
            '<div style="flex-grow:1; min-width:0;">'
            '<div style="font-size:15px; font-weight:500;">%s</div>'
            '<div style="font-size:11.5px; color:%s; margin-top:3px;">%s</div></div>%s</div>'
            % (bg, LINE, op, ctrl, name, INK3, sub, right))

def col(items, gap=10, pad='0 20px'):
    return ('<div style="display:flex; flex-direction:column; gap:%spx; padding:%s;">%s</div>'
            % (gap, pad, ''.join(items)))

def note(text, tone='terra', ico='info'):
    m = {'terra': (TERRA_SOFT, 'oklch(0.36 0.07 45)', 'oklch(0.48 0.05 45)'),
         'sage':  (SAGE_SOFT, SAGE_DEEP, 'oklch(0.46 0.06 155)'),
         'amber': (AMBER_SOFT, AMBER_DEEP, 'oklch(0.50 0.07 75)'),
         'grey':  (SUNK, INK2, INK2),
         'plum':  (PLUM_SOFT, PLUM, 'oklch(0.46 0.06 280)')}
    bg, fg, bd = m[tone]
    return ('<div style="padding:13px 15px; background:%s; border-radius:14px; display:flex; gap:10px; '
            'align-items:flex-start;"><span style="color:%s; flex-shrink:0; margin-top:1px;">%s</span>'
            '<div style="font-size:11.5px; line-height:1.5; color:%s; text-wrap:pretty;">%s</div></div>'
            % (bg, fg, icon(ico, 14, 2), bd, text))

def spacer(h):
    return '<div style="height:%spx;"></div>' % h

def write(name, body, script=None, bg=None):
    open(name, 'w', encoding='utf-8').write(doc(body, script, bg))
    return name
