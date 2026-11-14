#!/usr/bin/env python3
"""Build KCE Pathways Grade 6 pages from content/*.py into the repo's grade6/ folder."""
import importlib.util, json, os, re, sys, glob, html
from scope import UNITS, SUBJECT_NAMES, weeks

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('--') else '/home/claude/repos/KCE_Pathways_Curriculum/grade6'
CSS = open(os.path.join(HERE, 'style.css')).read()
ENGINE = open(os.path.join(HERE, 'engine.js')).read()
PB = "<div class='pbrand'><span>KingCretot Experience</span><span style='font-size:11px;letter-spacing:2px'><span style='color:#0047BA'>EDUCATE.</span> <span style='color:#C9A84C'>EMPOWER.</span> <span style='color:#DB2F30'>EXCEL.</span></span></div>"
SUBJ_ORDER = ['ela', 'math', 'science', 'socialstudies']
LEGAL = ('<div id="kce-legal" style="background:#0A1F3D;color:#C9A84C;font:12px/1.4 Arial,sans-serif;text-align:center;padding:8px 16px">'
         '&copy; 2026 KingCretot Experience. All rights reserved. Licensed for KCE students only. Do not copy, share or distribute.</div>')
FOOT = ('<footer class="f">KingCretot Experience, LLC &middot; Approved Provider: <span class="g">Step Up For Students</span> &middot; '
        '<span class="g">Arizona ESA</span> &middot; <span class="g">West Virginia Hope Scholarship</span> &middot; kingcretot.com</footer>')
TOP = ('<header class="top"><div class="bar"><a class="brand" href="{home}"><span class="kc">KC</span><span><span class="nm">KingCretot Experience</span>'
       '<span class="tg"><span style="color:#5b8def">EDUCATE.</span> <span style="color:#C9A84C">EMPOWER.</span> <span style="color:#DB2F30">EXCEL.</span></span></span></a>{right}</div>'
       '<div class="rule"><i style="background:#0047BA"></i><i style="background:#C9A84C"></i><i style="background:#DB2F30"></i></div></header>')
HEAD = ('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta name="robots" content="noindex,nofollow"><title>{title} | KingCretot Experience</title><style>{css}</style>{extra}</head><body>')


def load(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def strip(s):
    return html.unescape(re.sub(r'<[^>]+>', ' ', s or '')).replace('  ', ' ').strip()


import subprocess
def pdf_pages(path):
    out = '/tmp/_fit.pdf'
    subprocess.run(['google-chrome', '--headless', '--no-sandbox', '--disable-gpu', f'--print-to-pdf={out}', '--no-pdf-header-footer', 'file://' + path],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
    info = subprocess.run(['pdfinfo', out], capture_output=True, text=True).stdout
    return int(re.search(r'Pages:\s+(\d+)', info).group(1))


def write(rel, text, fit=False):
    p = os.path.join(OUT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w').write(text)
    if fit and '--nofit' not in sys.argv:
        for c in ('c1', 'c2', 'c3'):
            if pdf_pages(p) <= 1: return
            open(p, 'w').write(text.replace('<body>', f'<body class="{c}">', 1))
        if pdf_pages(p) > 1: print('WARNING: does not fit one page:', rel)


def answer_text(q):
    t = q['t']
    if t == 'num': return q.get('show') or (str(q['a'][0] if isinstance(q['a'], list) else q['a']) + (' ' + q['unit'] if q.get('unit') else ''))
    if t == 'text': return q.get('show') or next((a for a in q['a'] if isinstance(a, str)), 'see rubric')
    if t == 'blanks': return q.get('show') or ' / '.join(next((a for a in b if isinstance(a, str)), '') for b in q['blanks'])
    if t == 'label': return ', '.join(f"{l[0]} = {l[1][0]}" for l in q['labels'])
    if t == 'order': return ' → '.join(q['items'])
    if t == 'mc': return q['opts'][q['a']]
    return 'Written response: score with the rubric.'


def all_questions(L):
    groups = []
    if L.get('reconnect'): groups.append(('Reconnect', L['reconnect']['items']))
    for i, b in enumerate(L.get('learn', [])): groups.append((f"Learn {i+1}: {b['title']}", b.get('checks', [])))
    if L.get('handson'): groups.append(('Hands-On', L['handson'].get('record', [])))
    if L.get('think'): groups.append(('Think Deeper', L['think']['items']))
    if L.get('exit'): groups.append(('Exit Check', L['exit']))
    return groups


HANDS_RUBRIC = ["Completes every step of the activity", "Includes specific details, numbers or observations from the activity", "Explains thinking in complete sentences"]


def lesson_page(L, week, subj):
    L = dict(L)
    if L.get('handson'):
        for q in L['handson'].get('record', []):
            q.setdefault('rubric', HANDS_RUBRIC)
    L['id'] = f'pathways-g6-{subj}-w{week}'; L['week'] = week; L['subjectName'] = SUBJECT_NAMES[subj]
    right = ('<div class="stats"><span class="s">Score <b id="hudScore">0</b>/100</span><span class="s">Answered <b id="hudDone">0/0</b></span>'
             '<button id="vocabBtn" hidden>Vocabulary</button></div>')
    extra = '<script type="module" src="/kce-progress/kce-progress.js" data-course="pathways-g6"></script>'
    return (HEAD.format(title=f"Grade 6 Week {week} {SUBJECT_NAMES[subj]}: {L['title']}", css=CSS, extra=extra) +
            TOP.format(home='../index.html', right=right) + '<div id="vocabPanel"></div><nav id="nav"></nav><main id="stage"></main>' + FOOT + LEGAL +
            '<script>window.LESSON=' + json.dumps(L, ensure_ascii=False) + ';</script><script>' + ENGINE + '</script></body></html>')


LOCK = '''<div id="lock" style="max-width:420px;margin:60px auto;text-align:center"><h2>Teacher Plan</h2><p>Enter the instructor code to open this plan and answer key.</p>
<input id="code" type="password" style="font-size:18px;padding:8px;width:160px"> <button class="btn" onclick="var c=document.getElementById('code').value;if(c==='9110'){document.getElementById('lock').style.display='none';document.getElementById('plan').style.display='block';try{sessionStorage.setItem('kceT','1')}catch(e){}}else{alert('That code is not correct.')}">Open</button></div>
<script>try{if(sessionStorage.getItem('kceT')==='1'){document.addEventListener('DOMContentLoaded',function(){document.getElementById('lock').style.display='none';document.getElementById('plan').style.display='block';});}}catch(e){}</script>'''
PRINT_CSS = '''@page{size:letter;margin:.5in}@media print{.top,.noprint,footer.f{display:none!important}body{background:#fff;font-size:12px;line-height:1.35}.blk{margin:6px 0 8px}.sheet h2{margin:2px 0 4px}.sheet p{margin:3px 0}main{padding:0}.sheet{border:0;padding:0}#kce-legal{display:none}h2{break-after:avoid}.blk{break-inside:avoid}}
.sheet{background:#fff;border:1px solid var(--line);border-radius:8px;padding:22px 26px}.blk{margin:10px 0 14px}.lines{border-bottom:1px solid #999;height:24px}
.pbrand{display:none}@media print{.pbrand{display:flex;justify-content:space-between;align-items:center;border-bottom:3px solid #C9A84C;padding-bottom:4px;margin-bottom:6px;font-family:Georgia,serif;color:#0A1F3D;font-weight:bold}}
@media print{body.c1{font-size:11.2px;line-height:1.28}body.c1 .lines{height:20px}body.c1 .blk{margin:3px 0 5px}body.c1 .sheet h3{margin:2px 0}
body.c2{font-size:10.6px;line-height:1.22}body.c2 .lines{height:17px}body.c2 .blk{margin:2px 0 4px}body.c2 h2{font-size:18px}body.c2 .sheet p{margin:2px 0}
body.c3{font-size:10px;line-height:1.18}body.c3 .lines{height:15px}body.c3 .blk{margin:1px 0 3px}body.c3 h2{font-size:17px}body.c3 .sheet p{margin:1px 0}body.c3 .visual svg{max-width:420px}}
.plan h3{margin-top:18px;border-bottom:2px solid var(--gold);padding-bottom:3px}.plan table.t td{vertical-align:top}.key li{margin:6px 0}'''


def teacher_page(L, T, P, week, subj):
    rows = ''.join(f"<tr><td style='white-space:nowrap'>{m} min</td><td><b>{h}</b><br>{d}</td></tr>" for m, h, d in T['flow'])
    keys = ''
    for g, qs in all_questions(L):
        if not qs: continue
        keys += f"<h4>{g}</h4><ol class='key'>" + ''.join(
            f"<li>{strip(q['q'])}<br><b>Answer:</b> {html.escape(answer_text(q))}" + (f"<br><span class='muted'>{strip(q.get('why',''))}</span>" if q.get('why') else '') +
            (f"<br><b>Rubric:</b> {'; '.join(q['rubric'])}" if q.get('rubric') else '') + (f"<br><b>Model answer:</b> {q['model']}" if q.get('model') else '') + '</li>' for q in qs) + '</ol>'
    pkey = ''.join(f"<li>{strip(i['q'])}<br><b>Answer:</b> {i['a']}</li>" for i in P['items'])
    voc = ''.join(f"<li><b>{v[0]}</b>: {strip(v[1])}</li>" for v in L.get('vocab', []))
    lst = lambda xs: '<ul>' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul>'
    body = f'''<div id="plan" class="plan sheet" style="display:none">{PB}
<p class="kicker">{L['unit']} &middot; Week {week} &middot; {SUBJECT_NAMES[subj]} &middot; Teacher Plan</p><h1>{L['title']}</h1>
<p><b>Lesson length:</b> {T.get('length','60 minutes live, plus the after-class interactive lesson')}</p>
<h3>Objectives</h3>{lst(L['objectives'])}
<h3>Standards</h3>{lst(T['standards'])}
<h3>Materials</h3>{lst(T['materials'])}
<h3>Vocabulary</h3><ul>{voc}</ul>
<h3>Lesson flow</h3><table class="t">{rows}</table>
<h3>Key questions to ask</h3>{lst(T['key_questions'])}
<h3>Common mistakes to watch for</h3>{lst(T['misconceptions'])}
<h3>Support (if the student is struggling)</h3>{lst(T['support'])}
<h3>Challenge (if the student is ready for more)</h3>{lst(T['challenge'])}
{('<h3>Background for the teacher</h3>' + T['background']) if T.get('background') else ''}
{('<h3>Sources</h3>' + lst(T['sources'])) if T.get('sources') else ''}
<h3>How the lesson runs</h3><p>During the live lesson, the student shares their screen and answers the Reconnect questions and the Learn checks live while you teach. The Hands-On activity, Think Deeper and Exit Check are completed after class.</p>
<h3>Scoring</h3><p>The interactive lesson scores itself: full points on the first try, half points on the second try, then the answer and explanation appear. Mastery is 85. Written responses arrive in your Formspree email with the score; score them with the rubric below before the student moves on.</p>
<h3>Answer key: interactive lesson</h3>{keys}
<h3>Answer key: printable page</h3><ol class="key">{pkey}</ol>
</div>'''
    return (HEAD.format(title=f"Teacher Plan G6 W{week} {SUBJECT_NAMES[subj]}", css=CSS + PRINT_CSS, extra='') +
            TOP.format(home='../index.html', right='<button class="btn ghost noprint" onclick="window.print()">Print</button>') +
            '<main>' + LOCK + body + '</main>' + FOOT + LEGAL + '</body></html>')


def print_page(L, P, week, subj):
    items = ''
    for n, i in enumerate(P['items'], 1):
        lines = ''.join('<div class="lines"></div>' for _ in range(i.get('lines', 2)))
        vis = f"<div class='visual'>{i['visual']}</div>" if i.get('visual') else ''
        items += f"<div class='blk'><b>{n}.</b> {i['q']}{vis}{lines}</div>"
    body = (f"<div class='sheet'>{PB}<p class='kicker'>Grade 6 &middot; Week {week} &middot; {SUBJECT_NAMES[subj]} &middot; Printable Practice</p>"
            f"<h2>{L['title']}</h2><p>Name: ______________________ &nbsp; Date: ____________</p><p><i>{P.get('directions','Show your work or explain your thinking in complete sentences.')}</i></p>{items}</div>")
    return (HEAD.format(title=f"Printable G6 W{week} {SUBJECT_NAMES[subj]}", css=CSS + PRINT_CSS, extra='') +
            TOP.format(home='../index.html', right='<button class="btn ghost noprint" onclick="window.print()">Print</button>') +
            '<main>' + body + '</main>' + FOOT + LEGAL + '</body></html>')


def parent_page(G, week):
    secs = ''.join(f"<div class='blk'><h3>{SUBJECT_NAMES[s]}: {G[s]['topic']}</h3><p>{G[s]['what']}</p>"
                   f"<p><b>Ask at dinner:</b> {G[s]['ask']}</p><p><b>Try it together:</b> {G[s]['try']}</p>"
                   f"<p><b>Signs it's clicking:</b> {G[s]['clicking']} <b>Signs they need help:</b> {G[s]['help']}</p></div>" for s in SUBJ_ORDER if s in G)
    extra = ''
    extra += "<p><b>How scoring works:</b> each lesson scores itself. Your child gets two tries per question: full points on the first try, half points on the second, then the answer and explanation appear. A score of 85 or higher means the lesson is mastered. Written answers go to Jonathan, who scores them with a rubric.</p>"
    if G.get('time'): extra += f"<p><b>Time this week:</b> {G['time']}</p>"
    if G.get('gather'): extra += f"<p><b>Gather this week:</b> {G['gather']}</p>"
    if G.get('heads_up'): extra += f"<p><b>Heads up:</b> {G['heads_up']}</p>"
    body = (f"<div class='sheet'>{PB}<p class='kicker'>Grade 6 &middot; Week {week} &middot; Parent Guide</p><h2>{G['headline']}</h2><p>{G['intro']}</p>{extra}{secs}"
            f"<p class='muted'>Questions? Email kce@kingcretot.com.</p></div>")
    return (HEAD.format(title=f"Parent Guide G6 W{week}", css=CSS + PRINT_CSS + '.sheet h3{margin-top:4px}.blk p{margin:4px 0}@media print{body{font-size:11.3px;line-height:1.3}.blk{margin:4px 0 6px}}', extra='') +
            TOP.format(home='../index.html', right='<button class="btn ghost noprint" onclick="window.print()">Print</button>') +
            '<main>' + body + '</main>' + FOOT + LEGAL + '</body></html>')


def simple_page(title, kicker, inner, home='../index.html'):
    return (HEAD.format(title=title, css=CSS + PRINT_CSS, extra='') +
            TOP.format(home=home, right='<button class="btn ghost noprint" onclick="window.print()">Print</button>') +
            f"<main><div class='sheet'>{PB}<p class='kicker'>{kicker}</p>{inner}</div></main>" + FOOT + LEGAL + '</body></html>')


def hub(built, unit_pages):
    cards = ''
    for (n, unit, _) in weeks('math'):
        if (n - 1) % 5 == 0:
            u = (n - 1) // 5 + 1
            extras = ''.join(f"<a href='{p}'>{t}</a>" for p, t in unit_pages.get(u, []))
            cards += f"<h2 class='uh'>{UNITS['math'][u-1][0].split(':')[0]}</h2>" + (f"<div class='uextra'>{extras}</div>" if extras else '')
        links = ''
        for s in SUBJ_ORDER:
            t = dict((w, tt) for w, _, tt in weeks(s))[n]
            if (n, s) in built:
                links += (f"<div class='sub'><b>{SUBJECT_NAMES[s]}</b><a class='go' href='week{n}/{s}.html'>{t}</a>"
                          f"<span class='mini'><a href='week{n}/{s}-print.html'>Printable</a> &middot; <a href='week{n}/{s}-teacher.html'>Teacher plan</a></span></div>")
            else:
                links += f"<div class='sub soon'><b>{SUBJECT_NAMES[s]}</b><span>{t}</span><span class='mini'>Being built</span></div>"
        pg = f"<a class='pg' href='week{n}/parent-guide.html'>Parent guide</a>" if os.path.exists(os.path.join(OUT, f'week{n}/parent-guide.html')) else ''
        cards += f"<div class='wk'><div class='wh'>Week {n}{pg}</div>{links}</div>"
    css = CSS + '''.uh{margin:26px 0 8px}.uextra a{margin-right:14px;font-weight:bold}.wk{background:#fff;border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin:12px 0}
.wh{font-family:Georgia,serif;font-size:19px;color:var(--navy);display:flex;justify-content:space-between}.pg{font-family:Arial;font-size:14px}
.sub{display:grid;grid-template-columns:170px 1fr auto;gap:10px;padding:7px 0;border-top:1px solid #f0ebdf;align-items:center}.sub.soon{color:var(--muted)}
.go{font-weight:bold;color:var(--blue)}.mini{font-size:13px}@media(max-width:700px){.sub{grid-template-columns:1fr}}'''
    intro = ('<h1>KCE Pathways: Grade 6</h1><p class="sub">A full school year in ELA, Math, Life Science, and World and American History. '
             'Thirty weeks, six units, built for homeschool families and global thinkers.</p>'
             '<div class="card"><b>How it works:</b> each week has an interactive lesson for every subject, a printable practice page, a detailed teacher plan, '
             'and a parent guide. Every unit ends with a checkpoint, and ELA, Science and Social Studies end each unit with a project scored by rubric. '
             'Mastery is 85.</div>')
    return (HEAD.format(title='KCE Pathways Grade 6', css=css, extra='') + TOP.format(home='index.html', right='') +
            f'<main>{intro}{cards}</main>' + FOOT + LEGAL + '</body></html>')


def main():
    built = set()
    for f in sorted(glob.glob(os.path.join(HERE, 'content', 'w*_*.py'))):
        m = re.match(r'w(\d+)_(\w+)\.py', os.path.basename(f)); week, subj = int(m.group(1)), m.group(2)
        if subj == 'parent':
            write(f'week{week}/parent-guide.html', parent_page(load(f).GUIDE, week), fit=True); continue
        mod = load(f)
        write(f'week{week}/{subj}.html', lesson_page(mod.LESSON, week, subj))
        write(f'week{week}/{subj}-teacher.html', teacher_page(mod.LESSON, mod.TEACHER, mod.PRINT, week, subj))
        write(f'week{week}/{subj}-print.html', print_page(mod.LESSON, mod.PRINT, week, subj), fit=True)
        built.add((week, subj))
    unit_pages = {}
    for f in sorted(glob.glob(os.path.join(HERE, 'content', 'u*_*.py'))):
        m = re.match(r'u(\d+)_(\w+)\.py', os.path.basename(f)); u, name = int(m.group(1)), m.group(2)
        mod = load(f)
        write(f'unit{u}/{name}.html', simple_page(mod.TITLE, mod.KICKER, mod.HTML))
        unit_pages.setdefault(u, []).append((f'unit{u}/{name}.html', mod.LINK))
    write('index.html', hub(built, unit_pages))
    print('built', len(built), 'lessons;', sum(len(v) for v in unit_pages.values()), 'unit pages')


if __name__ == '__main__':
    main()
