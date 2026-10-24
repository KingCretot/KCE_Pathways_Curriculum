/* KCE Pathways: show "Print your certificate" on a unit checkpoint's final screen once the student passes (85+). */
(function(){
  var me = document.currentScript, band = me.getAttribute('data-band'), unit = me.getAttribute('data-unit'), subject = me.getAttribute('data-subject');
  var root = me.src.slice(0, me.src.lastIndexOf('/') + 1);
  var url = root + 'certificate.html?band=' + encodeURIComponent(band) + '&unit=' + encodeURIComponent(unit) + '&subject=' + encodeURIComponent(subject);
  function check(){
    var sc = document.getElementById('finalScore'), body = document.getElementById('finalMessageBody');
    if (!sc || !body) return;
    var n = parseInt((sc.textContent || '').replace(/[^0-9]/g, ''), 10), have = document.getElementById('kceCertBtn');
    if (!isNaN(n) && n >= 85 && sc.offsetParent !== null){
      if (!have){
        var w = document.createElement('div'); w.id = 'kceCertBtn'; w.style.cssText = 'text-align:center;margin:18px 0 6px';
        w.innerHTML = '<a href="' + url + '" target="_blank" rel="noopener" style="display:inline-block;background:#C9A84C;color:#0A1F3D;font:800 19px Arial,Helvetica,sans-serif;text-decoration:none;padding:15px 28px;border-radius:999px;box-shadow:0 6px 18px rgba(10,31,61,.25);border:3px solid #0A1F3D">&#127891; Print your certificate &mdash; you earned it!</a>';
        body.parentNode.insertBefore(w, body.nextSibling);
      }
    } else if (have){ have.remove(); }
  }
  setInterval(check, 800);
})();
