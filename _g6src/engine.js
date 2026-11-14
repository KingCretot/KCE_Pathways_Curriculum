/* KCE Pathways Grade 6 lesson engine. Reads window.LESSON and builds the interactive lesson.
   Question types: num, text, blanks, order, label, mc (sparingly), open (written, sent to KCE, not auto-scored).
   Scoring: first try = full points, second try = half points, then the answer and explanation are shown.
   Score = points earned / points possible x 100. Mastery = 85. */
(function(){
'use strict';
var L = window.LESSON, FORMSPREE_ID = 'mojgzadl', MASTERY = 85;
var NAME_KEY = 'kcePathwaysStudentName', PROG_KEY = 'kce_pathways_progress';
var state = { earned:0, possible:0, answered:{}, written:{}, slide:0, cpEarned:0, cpPossible:0, cpOpenPts:0 };
var $ = function(s,r){ return (r||document).querySelector(s); };
function esc(s){ return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];}); }

/* ---------- answer checking ---------- */
function norm(s){
  return String(s||'').normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/(\d),(\d)/g,'$1$2').toLowerCase().replace(/[‘’]/g,"'").replace(/[“”]/g,'"')
    .replace(/[^a-z0-9\s'\-\/\.]/g,' ').replace(/\b(the|a|an)\b/g,' ').replace(/\s+/g,' ').trim().replace(/\.$/,'');
}
function lightNorm(s){ return String(s||'').replace(/[\u201c\u201d]/g,'"').replace(/[\u2018\u2019]/g,"'").replace(/\s+/g,' ').trim().replace(/\s+([,.!?])/g,'$1'); }
function parseNum(s){
  s = String(s||'').trim().replace(/^(about|approximately|approx\.?|around|roughly|nearly|≈|~)\s*/i,'').replace(/[$,]/g,'').replace(/\s+/g,' ').replace(/\s*[a-z°%.²³×µ]*[a-z°%×µ][a-z°%.²³×µ\s]*$/i,'').trim();
  if(!s) return NaN;
  s = s.replace(/½/g,' 1/2').replace(/¼/g,' 1/4').replace(/¾/g,' 3/4').replace(/\s+/g,' ').trim();
  var m = s.match(/^(-?\d+)\s+(\d+)\/(\d+)$/);            // mixed number 2 1/2
  if(m){ var w=+m[1]; var f=+m[2]/+m[3]; return w<0? w-f : w+f; }
  m = s.match(/^(-?\d+(?:\.\d+)?)\/(\d+(?:\.\d+)?)$/);       // fraction 3/4
  if(m) return +m[1]/+m[2];
  s = s.replace(/\s/g,'');
  if(/^-?\d*\.?\d+$/.test(s)) return parseFloat(s);
  return NaN;
}
function textOk(val, accepts){
  var v = norm(val);
  if(!v) return false;
  for(var i=0;i<accepts.length;i++){
    var a = accepts[i];
    if(a && typeof a==='object' && a.all){            // every keyword group must appear
      var ok = a.all.every(function(group){ return group.some(function(k){ var nk = norm(k); if(!nk) return false; var re = new RegExp('(^|[^a-z0-9])' + nk.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')); return re.test(v); }); });
      if(ok && a.none && a.none.some(function(k){ var nk = norm(k); return nk && new RegExp('(^|[^a-z0-9])' + nk.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')).test(v); })) ok = false;
      if(ok) return true;
    } else if(typeof a==='string' && a.charAt(0)==='^'){   // answer must begin with this phrase
      var ns = norm(a.slice(1));
      if(ns && (v===ns || v.indexOf(ns+' ')===0)) return true;
    } else if(norm(a)===v) return true;
    else if(typeof a==='string' && a.length>1 && a!=='yes' && a!=='no'){
      var na = norm(a), words = v.split(' ').length, aw = na.split(' ').length;
      var bd = /[0-9]/.test(na) ? '[^a-z0-9./]' : '[^a-z0-9]';
      var re = new RegExp('(^|' + bd + ')' + na.replace(/[.*+?^${}()|[\]\\]/g,'\\$&') + '($|' + bd + ')');
      var mt = re.exec(v); if(words <= aw + 6 && mt && !/\b(not|isn't|isnt|never|no)\b/.test(v.slice(0, mt.index + 1))) return true;
    }
    else if((a==='yes'||a==='no') && new RegExp('^'+a+'\\b').test(v)) return true;
  }
  return false;
}
function checkQ(q, el){
  if(q.t==='num'){
    var n = parseNum($('input',el).value), tol = q.tol==null?0.0001:q.tol;
    var answers = [].concat(q.a);
    return !isNaN(n) && answers.some(function(a){ return Math.abs(n-a)<=tol; });
  }
  if(q.t==='text') return textOk($('input,textarea',el).value, q.a);
  if(q.t==='punct'){ var lv = lightNorm($('input',el).value); return q.a.some(function(a){ var la = lightNorm(a); return lv===la || lv.replace(/\.$/,'')===la.replace(/\.$/,''); }); }
  if(q.t==='blanks'){
    var ins = el.querySelectorAll('input.blank');
    var vals = Array.prototype.map.call(ins,function(inp){ return norm(inp.value); });
    if(q.distinct && vals.some(function(x,i){ return vals.indexOf(x)!==i; })) return false;
    return Array.prototype.every.call(ins,function(inp,i){ return textOk(inp.value, q.blanks[i]); });
  }
  if(q.t==='label'){
    var li = el.querySelectorAll('input.lab');
    return Array.prototype.every.call(li,function(inp,i){ return textOk(inp.value, q.labels[i][1]); });
  }
  if(q.t==='order'){
    var sels = el.querySelectorAll('select.ord'); var seen={};
    for(var i=0;i<sels.length;i++){ if(!sels[i].value||seen[sels[i].value]) return false; seen[sels[i].value]=1; }
    // items are listed shuffled; data-ix holds the correct position (1-based)
    return Array.prototype.every.call(sels,function(s){ return s.value===s.getAttribute('data-ix'); });
  }
  if(q.t==='mc'){ var c = el.querySelector('input[type=radio]:checked'); return !!c && +c.value===q.a; }
  return false;
}
function answerText(q){
  if(q.t==='num') return q.show || String([].concat(q.a)[0]) + (q.unit?' '+q.unit:'');
  if(q.t==='text'||q.t==='punct') return q.show || (typeof q.a[0]==='string'? q.a[0] : '');
  if(q.t==='blanks') return q.show || q.blanks.map(function(b){return typeof b[0]==='string'?b[0]:'';}).join(' / ');
  if(q.t==='label') return q.labels.map(function(l){ return l[0]+' = '+l[1][0]; }).join(', ');
  if(q.t==='order') return q.items.map(function(it,i){ return (i+1)+'. '+it; }).join('  ');
  if(q.t==='mc') return q.opts[q.a];
  return '';
}

/* ---------- rendering questions ---------- */
var qCount = 0, QS = {};
function shuffle(a,seed){ var b=a.slice(), s=seed||7; for(var i=b.length-1;i>0;i--){ s=(s*9301+49297)%233280; var j=Math.floor(s/233280*(i+1)); var t=b[i]; b[i]=b[j]; b[j]=t; } return b; }
function qHTML(q, group){
  var id = 'q'+(++qCount); QS[id] = {q:q, group:group, tries:0, done:false};
  var pts = q.t==='open' ? '' : '<span class="pts">'+(q.pts||2)+' pts</span>';
  var h = '<div class="q" id="'+id+'">'+pts+'<div class="qtext">'+q.q+'</div>';
  if(q.visual) h += '<div class="visual">'+q.visual+'</div>';
  if(q.t==='num') h += '<div class="row"><input type="text" inputmode="decimal" autocomplete="off" aria-label="answer">'+(q.unit?'<span class="unit">'+esc(q.unit)+'</span>':'')+'</div>';
  if(q.t==='text'||q.t==='punct') h += '<div class="row"><input type="text" autocomplete="off" aria-label="answer" class="wide"></div>';
  if(q.t==='blanks'){ var k=0; h += '<div class="sent">'+q.sent.replace(/___/g,function(){ return '<input type="text" class="blank" autocomplete="off" aria-label="blank '+(++k)+'">'; })+'</div>'; }
  if(q.t==='label'){ h += '<div class="labs">'+q.labels.map(function(l,i){ return '<label>'+esc(l[0])+' <input type="text" class="lab" autocomplete="off"></label>'; }).join('')+'</div>'; }
  if(q.t==='order'){
    var n=q.items.length, order=shuffle(q.items.map(function(it,i){return i;}), qCount+3);
    h += '<div class="ord-list">'+order.map(function(ix){
      var opts='<option value="">#</option>'; for(var i=1;i<=n;i++) opts+='<option>'+i+'</option>';
      return '<div class="ord-item"><select class="ord" data-ix="'+(ix+1)+'">'+opts+'</select> '+q.items[ix]+'</div>'; }).join('')+'</div>';
  }
  if(q.t==='mc') h += '<div class="mc">'+q.opts.map(function(o,i){ return '<label><input type="radio" name="'+id+'" value="'+i+'"> '+o+'</label>'; }).join('')+'</div>';
  if(q.t==='open'){
    h += '<textarea rows="'+(q.rows||5)+'" aria-label="your response"></textarea>';
    if(q.rubric) h += '<details class="rub"><summary>What a strong answer includes</summary><ul>'+q.rubric.map(function(r){return '<li>'+r+'</li>';}).join('')+'</ul></details>';
    h += '<div class="row"><button class="btn save">Save my response</button><span class="fb"></span></div></div>';
    return h;
  }
  if(q.hint) h += '<details class="hint"><summary>Need a hint?</summary>'+q.hint+'</details>';
  h += '<div class="row"><button class="btn check">Check</button><span class="fb"></span></div><div class="why"></div></div>';
  return h;
}
function wire(root){
  root.querySelectorAll('.q').forEach(function(el){
    var rec = QS[el.id]; if(!rec || el._wired) return; el._wired = 1;
    var isCP = rec.group==='checkpoint';
    if(isCP){ if(rec.q.t!=='open') state.cpPossible += (rec.q.pts||2); else state.cpOpenPts += (rec.q.pts||4); }
    else if(rec.q.t!=='open') state.possible += (rec.q.pts||2);
    var b = el.querySelector('.check'), s = el.querySelector('.save');
    if(isCP && b) b.textContent = 'Submit answer';
    if(s) s.addEventListener('click', function(){
      var v = el.querySelector('textarea').value.trim(), words = v? v.split(/\s+/).length : 0, min = rec.q.min||0;
      var fb = el.querySelector('.fb');
      if(words < min){ fb.className='fb bad'; fb.textContent='Write at least '+min+' words (you have '+words+').'; return; }
      state.written[rec.q.key || el.id] = { prompt: rec.q.q.replace(/<[^>]+>/g,''), response: v };
      fb.className='fb ok'; fb.textContent='Saved. It will be sent with your results.'; save();
    });
    if(b) b.addEventListener('click', function(){
      if(rec.done) return;
      var ok = checkQ(rec.q, el), fb = el.querySelector('.fb'), why = el.querySelector('.why'), p = rec.q.pts||2;
      rec.tries++;
      if(rec.group==='checkpoint'){   // one try, no answer shown: the checkpoint measures independent mastery
        if(ok) state.cpEarned += p; rec.done = true; rec.ok = ok;
        fb.className='fb'; fb.textContent='Answer recorded.'; lock(el);
        state.answered[el.id] = { ok: ok, tries: 1 }; hud(); save(); return;
      }
      if(ok){
        var got = rec.tries===1 ? p : p/2; state.earned += got; rec.done = true;
        fb.className='fb ok'; fb.textContent = rec.tries===1 ? 'Correct! +'+p : 'Correct on try 2. +'+got;
        if(rec.q.why) why.innerHTML = '<b>Why:</b> '+rec.q.why;
        lock(el);
      } else if(rec.tries<2){
        fb.className='fb bad'; fb.textContent='Not yet. Look again and try once more.';
      } else {
        rec.done = true; fb.className='fb bad'; fb.textContent='The answer: '+answerText(rec.q);
        why.innerHTML = rec.q.why ? '<b>Why:</b> '+rec.q.why : ''; lock(el);
      }
      state.answered[el.id] = { ok: ok, tries: rec.tries };
      hud(); save();
    });
  });
}
function lock(el){ el.querySelectorAll('input,select,button.check').forEach(function(x){ x.disabled = true; }); el.classList.add('locked'); }

/* ---------- slides ---------- */
var slides = [];
function addSlide(kind, title, inner){ slides.push({kind:kind, title:title, html:inner}); }
function build(){
  var V = L.vocab||[];
  addSlide('start','Start',
    '<p class="kicker">'+esc(L.unit)+' &middot; Week '+L.week+' &middot; '+esc(L.subjectName)+'</p><h1>'+esc(L.title)+'</h1>'+
    (L.subtitle?'<p class="sub">'+esc(L.subtitle)+'</p>':'')+
    '<div class="card"><h3>Before you start</h3><p>Type your first and last name so your work goes to KingCretot Experience and your parent or teacher.</p>'+
    '<div class="row"><input id="fn" placeholder="First name" autocomplete="given-name"> <input id="ln" placeholder="Last name" autocomplete="family-name"></div></div>'+
    '<div class="card"><h3>How this lesson works</h3><ul><li>Most questions ask you to <b>work out and type</b> the answer, not pick it. For number answers, type the number; the unit is shown for you.</li><li>You get <b>2 tries</b>. Full points on try 1, half points on try 2, then the answer and the reason appear.'+(L.checkpoint?' <b>Checkpoint questions are different: one try, and answers are not shown.</b>':'')+'</li><li>Written responses go to your teacher, who scores them with the rubric.</li><li>Mastery is <b>85</b> or higher.</li></ul></div>'+
    (L.objectives?'<div class="card"><h3>By the end of this lesson you can</h3><ul>'+L.objectives.map(function(o){return '<li>'+o+'</li>';}).join('')+'</ul></div>':''));
  if(L.reconnect) addSlide('reconnect','Reconnect',
    '<h2>Reconnect: '+esc(L.reconnect.title)+'</h2><p>'+L.reconnect.intro+'</p>'+L.reconnect.items.map(function(q){return qHTML(q,'reconnect');}).join(''));
  if(L.hook) addSlide('hook','The Situation','<h2>'+esc(L.hook.title)+'</h2>'+(L.hook.visual?'<div class="visual">'+L.hook.visual+'</div>':'')+L.hook.html);
  (L.learn||[]).forEach(function(b,i){
    addSlide('learn','Learn '+(i+1),'<h2>'+esc(b.title)+'</h2>'+(b.visual?'<div class="visual">'+b.visual+'</div>':'')+b.html+
      (b.checks||[]).map(function(q){return qHTML(q,'learn');}).join(''));
  });
  if(L.handson){ var H=L.handson; addSlide('handson','Hands-On','<h2>Hands-On: '+esc(H.title)+'</h2>'+(H.intro?'<p>'+H.intro+'</p>':'')+
    '<div class="card"><h3>You need</h3><ul>'+H.materials.map(function(m){return '<li>'+m+'</li>';}).join('')+'</ul></div>'+
    '<div class="card"><h3>Steps</h3><ol>'+H.steps.map(function(s){return '<li>'+s+'</li>';}).join('')+'</ol></div>'+
    (H.visual?'<div class="visual">'+H.visual+'</div>':'')+(H.record||[]).map(function(q){return qHTML(q,'handson');}).join('')); }
  if(L.think) addSlide('think','Think Deeper','<h2>Think Deeper</h2>'+(L.think.intro?'<p>'+L.think.intro+'</p>':'')+L.think.items.map(function(q){return qHTML(q,'think');}).join(''));
  if(L.checkpoint){ var C=L.checkpoint; addSlide('checkpoint','Checkpoint','<h2>'+esc(C.title)+'</h2>'+(C.intro?'<p>'+C.intro+'</p>':'')+
    (C.parts||[{items:C.items}]).map(function(pt){ return (pt.title?'<h3 class="cp-part">'+esc(pt.title)+'</h3>':'')+pt.items.map(function(q){return qHTML(q,'checkpoint');}).join(''); }).join('')); }
  if(L.exit) addSlide('exit','Exit Check','<h2>Exit Check</h2><p>Show what you learned today. Work it out, then type your answer.</p>'+L.exit.map(function(q){return qHTML(q,'exit');}).join(''));
  addSlide('done','Results','<h2>Your Results</h2><div id="result"></div>'+
    (V.length?'<div class="card"><h3>Vocabulary from this lesson</h3><dl class="vocab">'+V.map(function(v){return '<dt>'+esc(v[0])+'</dt><dd>'+v[1]+'</dd>';}).join('')+'</dl></div>':'')+
    (L.next?'<div class="card"><h3>Coming next</h3><p>'+L.next+'</p></div>':''));
  var nav = $('#nav'), stage = $('#stage');
  nav.innerHTML = slides.map(function(s,i){ return '<button data-i="'+i+'">'+esc(s.title)+'</button>'; }).join('');
  stage.innerHTML = slides.map(function(s,i){ return '<section class="slide" data-i="'+i+'">'+s.html+
    '<div class="pager">'+(i>0?'<button class="btn ghost prev">&larr; Back</button>':'<span></span>')+
    (i<slides.length-1?'<button class="btn next">Next &rarr;</button>':'')+'</div></section>'; }).join('');
  wire(stage);
  nav.addEventListener('click', function(e){ var b=e.target.closest('button'); if(b) go(+b.getAttribute('data-i')); });
  stage.addEventListener('click', function(e){ if(e.target.closest('.next')) go(state.slide+1); if(e.target.closest('.prev')) go(state.slide-1); });
  var fn=$('#fn'), ln=$('#ln');
  fn.value = localStorage.getItem('kcePathwaysStudentFirstName')||''; ln.value = localStorage.getItem('kcePathwaysStudentLastName')||'';
  function saveName(){ var f=fn.value.trim(), l=ln.value.trim(); if(f) localStorage.setItem('kcePathwaysStudentFirstName',f); if(l) localStorage.setItem('kcePathwaysStudentLastName',l); if(f||l) localStorage.setItem(NAME_KEY,(f+' '+l).trim()); }
  fn.addEventListener('blur',saveName); ln.addEventListener('blur',saveName);
  if(V.length){ $('#vocabBtn').hidden=false; $('#vocabPanel').innerHTML='<h3>Vocabulary</h3><dl class="vocab">'+V.map(function(v){return '<dt>'+esc(v[0])+'</dt><dd>'+v[1]+'</dd>';}).join('')+'</dl>';
    $('#vocabBtn').addEventListener('click',function(){ $('#vocabPanel').classList.toggle('on'); }); }
  restore(); go(0); hud();
}
function go(i){
  if(i<0||i>=slides.length) return; state.slide=i;
  document.querySelectorAll('.slide').forEach(function(s){ s.classList.toggle('on', +s.getAttribute('data-i')===i); });
  document.querySelectorAll('#nav button').forEach(function(b){ b.classList.toggle('on', +b.getAttribute('data-i')===i); });
  if(slides[i].kind==='done') finish();
  window.scrollTo(0,0);
}
function score(){ return state.possible ? Math.round(state.earned/state.possible*100) : 0; }
function cpScore(){ return state.cpPossible ? Math.round(state.cpEarned/state.cpPossible*100) : 0; }
function hud(){
  var done = Object.keys(state.answered).length, total = Object.keys(QS).filter(function(k){return QS[k].q.t!=='open';}).length;
  $('#hudScore').textContent = score(); $('#hudDone').textContent = done+'/'+total;
}
/* ---------- saving and reporting ---------- */
var SKEY = 'kce_g6_'+L.id;
function save(){ try{ localStorage.setItem(SKEY, JSON.stringify({written:state.written})); }catch(e){} }
function restore(){
  try{ var d = JSON.parse(localStorage.getItem(SKEY)||'{}'); state.written = d.written||{};
    Object.keys(QS).forEach(function(id){ var q=QS[id].q; if(q.t==='open'){ var k=q.key||id; if(state.written[k]) document.querySelector('#'+id+' textarea').value = state.written[k].response; } });
  }catch(e){}
}
function finish(){
  var total = Object.keys(QS).filter(function(k){return QS[k].q.t!=='open';}).length, done = Object.keys(state.answered).length;
  var opens = Object.keys(QS).filter(function(k){return QS[k].q.t==='open';}).length, savedW = Object.keys(state.written).length;
  var s = score(), r = $('#result');
  if(done < total){
    r.innerHTML = '<div class="card warn"><p>You have answered <b>'+done+' of '+total+'</b> scored questions. Go back and finish them, then return here to send your results.</p></div>';
    return;
  }
  var mastered = s>=MASTERY, cp = L.checkpoint ? cpScore() : null;
  r.innerHTML = '<h3 class="center">Lesson score</h3><div class="bigscore '+(mastered?'ok':'bad')+'">'+s+'<span>/100</span></div>'+
    '<p class="center">'+(mastered?'Mastered! You are ready for the next lesson.':'Not mastered yet. Review the parts you missed, then replay this lesson to reach 85.')+'</p>'+
    (cp!==null?'<div class="card"><h3>Checkpoint</h3><p>Your checkpoint answers are recorded: <b>'+state.cpEarned+' of '+state.cpPossible+'</b> auto-scored points ('+cp+'%). Your teacher adds the points for your written answers'+(state.cpOpenPts?' (worth '+state.cpOpenPts+' points)':'')+' and tells you your checkpoint score. Mastery is 85. Below 85, your teacher reviews with you first, then you retake the checkpoint.</p></div>':'')+
    (savedW<opens?'<div class="card warn"><p>You saved '+savedW+' of '+opens+' written responses. Save them before sending so your teacher can score them.</p></div>':'')+
    '<div class="center"><button class="btn" id="sendBtn">Send my results to KingCretot Experience</button><p id="sendStatus" class="muted"></p></div>';
  $('#sendBtn').addEventListener('click', function(){ report(s, mastered); });
}
function cpDetail(){
  return Object.keys(QS).filter(function(k){ return QS[k].group==='checkpoint' && QS[k].q.t!=='open'; }).map(function(k,i){ var r=QS[k]; return (i+1)+'. '+(r.ok?'correct':'MISSED')+' ('+(r.q.pts||2)+' pts): '+r.q.q.replace(/<div class=.cp-text.>[\s\S]*?<\/div><\/div>/,'').replace(/<[^>]+>/g,'').slice(0,90); }).join('\n');
}
function report(s, mastered){
  var name = (localStorage.getItem(NAME_KEY)||'').trim() || 'Unnamed Student', all = {};
  try{ all = JSON.parse(localStorage.getItem(PROG_KEY)||'{}'); }catch(e){}
  var prev = all[L.id]||{}; var rec = { score: Math.max(s, prev.score||0), passed: Math.max(s, prev.score||0)>=MASTERY, date: new Date().toISOString(), attempts: (prev.attempts||0)+1 };
  all[L.id] = rec; try{ localStorage.setItem(PROG_KEY, JSON.stringify(all)); }catch(e){}
  var written = Object.keys(state.written).map(function(k,i){ return (i+1)+'. '+state.written[k].prompt+'\n>> '+state.written[k].response; }).join('\n\n');
  var payload = { _subject: 'Grade 6 '+L.subjectName+' W'+L.week+' — '+name+' — '+s, student:name, module:L.id, lesson:L.title, score:s, mastered:mastered, attempts:rec.attempts, written_responses: written || '(none)', timestamp:new Date().toISOString() };
  if(L.checkpoint){ payload.checkpoint_auto = state.cpEarned+' of '+state.cpPossible+' points ('+cpScore()+'%)'; payload.checkpoint_written_points_to_add = state.cpOpenPts; payload.checkpoint_total_possible = state.cpPossible + state.cpOpenPts; payload.checkpoint_rule = 'Checkpoint score = (auto points + rubric points for written items) / total possible x 100. Mastery 85.'; payload.checkpoint_items = cpDetail(); payload._subject += ' | Checkpoint auto '+state.cpEarned+'/'+state.cpPossible; }
  var st = $('#sendStatus'); st.textContent = 'Sending...';
  fetch('https://formspree.io/f/'+FORMSPREE_ID,{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(payload)})
    .then(function(r){ st.textContent = r.ok ? 'Sent to KingCretot Experience.' : 'Could not send. Tell your parent or teacher your score: '+s; })
    .catch(function(){ st.textContent = 'Could not send. Tell your parent or teacher your score: '+s; });
}
document.addEventListener('DOMContentLoaded', build);
})();
