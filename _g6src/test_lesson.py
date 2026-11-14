"""Automated check of a Grade 6 lesson: no JS errors, every question answers correctly with the key, wrong answers are rejected,
score reaches 100, payload builds. Usage: python3 test_lesson.py path/to/lesson.html [screenshot_dir]"""
import sys, asyncio, json, os
from playwright.async_api import async_playwright

FILL = r'''
() => {
  const L = window.LESSON, qs = [];
  if (L.reconnect) qs.push(...L.reconnect.items);
  (L.learn||[]).forEach(b => qs.push(...(b.checks||[])));
  if (L.handson) qs.push(...(L.handson.record||[]));
  if (L.think) qs.push(...L.think.items);
  if (L.checkpoint) (L.checkpoint.parts || [{items: L.checkpoint.items}]).forEach(p => qs.push(...p.items));
  if (L.exit) qs.push(...L.exit);
  const els = [...document.querySelectorAll('.q')];
  if (els.length !== qs.length) return {err: 'count mismatch ' + els.length + ' vs ' + qs.length};
  const first = a => { for (const x of a) { if (typeof x === 'string') return x; if (x && x.all) return x.all.map(g => g[0]).join(' '); } return ''; };
  const issues = [];
  els.forEach((el, i) => {
    const q = qs[i];
    if (q.t === 'open') { el.querySelector('textarea').value = 'This is a test response with enough words to pass the minimum length check for the lesson engine and confirm saving works correctly every time it is used today in this automated run of the lesson.'; el.querySelector('.save').click(); return; }
    // wrong answer first on one in three questions
    if (i % 3 === 0 && (q.t === 'num' || q.t === 'text')) {
      el.querySelector('input').value = q.t === 'num' ? '-99999' : 'zzzz'; el.querySelector('.check').click();
      if (!/Not yet/.test(el.querySelector('.fb').textContent)) issues.push('wrong answer accepted at q' + (i+1));
    }
    if (q.t === 'num') el.querySelector('input').value = String([].concat(q.a)[0]);
    if (q.t === 'text' || q.t === 'punct') el.querySelector('input').value = first(q.a);
    if (q.t === 'blanks') el.querySelectorAll('input.blank').forEach((inp, k) => { let v = first(q.blanks[k]); if (q.distinct) { const b = q.blanks[k]; v = typeof b[0] === 'string' ? (b[k] || b[0]) : b[0].all[0][k]; } inp.value = v; });
    if (q.t === 'label') el.querySelectorAll('input.lab').forEach((inp, k) => inp.value = first(q.labels[k][1]));
    if (q.t === 'order') el.querySelectorAll('select.ord').forEach(s => s.value = s.getAttribute('data-ix'));
    if (q.t === 'mc') el.querySelector('input[value="' + q.a + '"]').checked = true;
    el.querySelector('.check').click();
    const fb = el.querySelector('.fb').textContent;
    if (!/Correct/.test(fb)) issues.push('q' + (i+1) + ' (' + q.t + ') not accepted: ' + fb + ' | ' + q.q.slice(0, 60));
  });
  return {n: els.length, issues, score: document.getElementById('hudScore').textContent};
}'''


async def run(path, shots=None):
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        pg = await b.new_page(viewport={'width': 1200, 'height': 900})
        errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        await pg.route('**/formspree.io/**', lambda r: r.fulfill(status=200, body='{"ok":true}'))
        await pg.route('**/kce-progress/**', lambda r: r.fulfill(status=200, body='', content_type='application/javascript'))
        await pg.goto('file://' + os.path.abspath(path)); await pg.wait_for_timeout(300)
        res = await pg.evaluate(FILL)
        n = await pg.evaluate('document.querySelectorAll("#nav button").length')
        await pg.evaluate(f'document.querySelectorAll("#nav button")[{n-1}].click()'); await pg.wait_for_timeout(200)
        has_send = await pg.evaluate('!!document.getElementById("sendBtn")')
        if has_send:
            await pg.click('#sendBtn'); await pg.wait_for_timeout(300)
        status = await pg.evaluate('(document.getElementById("sendStatus")||{}).textContent')
        if shots:
            os.makedirs(shots, exist_ok=True)
            for i in range(n):
                await pg.evaluate(f'document.querySelectorAll("#nav button")[{i}].click()'); await pg.wait_for_timeout(100)
                await pg.screenshot(path=f'{shots}/s{i:02d}.png', full_page=True)
        await b.close()
        res.update({'errors': errs, 'slides': n, 'send': has_send, 'status': status})
        return res

if __name__ == '__main__':
    r = asyncio.run(run(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None))
    print(json.dumps(r, indent=1))
