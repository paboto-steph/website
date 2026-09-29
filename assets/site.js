/* PABOTO · shared behaviour. Each block only runs when its elements are on the page. */
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var root = document.documentElement;
  root.classList.add('js');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function store(k, v) { try { if (v === undefined) return sessionStorage.getItem(k); sessionStorage.setItem(k, v); } catch (e) { return null; } }

  /* Mark the current page in the menu */
  var page = document.body.dataset.page;
  $$('.hdr nav a').forEach(function (a) { if (a.dataset.page === page) a.classList.add('on'); });

  /* Mobile menu */
  var hdr = $('.hdr'), menuBtn = $('#menu-btn');
  function setMenu(open) {
    hdr.classList.toggle('open', open);
    menuBtn.setAttribute('aria-expanded', open);
    menuBtn.textContent = open ? 'Close' : 'Menu';
    root.classList.toggle('lock', open);
  }
  if (menuBtn) {
    menuBtn.addEventListener('click', function () { setMenu(!hdr.classList.contains('open')); });
    $$('.hdr a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
  }

  /* Film: calm version for people who prefer less motion */
  var film = $('#film');
  if (film && reduce) { film.removeAttribute('autoplay'); film.pause(); }

  /* Doors on the home page: each one cuts to a new photo in turn */
  var doors = $$('.door[data-photos]');
  if (doors.length && !reduce) {
    var turn = 0, state = doors.map(function () { return 0; });
    var sets = doors.map(function (d) { return JSON.parse(d.dataset.photos); });
    setInterval(function () {
      if (document.hidden) return;
      var i = turn++ % doors.length, d = doors[i], set = sets[i];
      var r = d.getBoundingClientRect(); if (r.bottom < 0 || r.top > window.innerHeight) return;
      state[i] = (state[i] + 1) % set.length;
      var item = set[state[i]], img = new Image();
      img.src = 'images/' + item[0]; img.alt = '';
      var go = function () {
        img.className = 'in'; d.insertBefore(img, $('.door-cap', d));
        var imgs = $$('img', d); if (imgs.length > 2) d.removeChild(imgs[0]);
        $('.door-cap', d).textContent = item[1];
        var nx = set[(state[i] + 1) % set.length]; var p = new Image(); p.src = 'images/' + nx[0];
      };
      img.decode ? img.decode().then(go, go) : go();
    }, 1400);
  }

  /* Case sheets */
  var cards = $$('.card');
  var sheet = $('#sheet');
  if (cards.length && sheet) {
    var cases = cards.map(function (c) {
      return { id: c.id, title: c.dataset.title, services: c.dataset.services, body: $('.case-body', c), imgs: $$('.case-body img', c) };
    });
    var caseIndex = function (id) { for (var i = 0; i < cases.length; i++) if (cases[i].id === id) return i; return -1; };
    var sheetBody = $('#sheet-body'), sheetTitle = $('#sheet-title');
    var openCase = function (i) {
      var c = cases[i];
      sheetBody.innerHTML = '';
      var copy = c.body.cloneNode(true);
      while (copy.firstChild) sheetBody.appendChild(copy.firstChild);
      var n = (i + 1) % cases.length;
      var next = document.createElement('button');
      next.type = 'button'; next.className = 'case-next';
      next.innerHTML = '<span>Next project</span><strong></strong>';
      next.lastChild.textContent = cases[n].title + ' ⟶';
      next.addEventListener('click', function () { openCase(n); });
      $('.case-photos', sheetBody).appendChild(next);
      sheetTitle.textContent = c.services;
      if (!sheet.open) { sheet.showModal(); root.classList.add('lock'); sheet.focus(); }
      sheet.scrollTop = 0;
      history.replaceState(null, '', '#' + c.id);
    };
    var closeCase = function () { if (sheet.open) sheet.close(); };
    sheet.addEventListener('close', function () {
      root.classList.remove('lock');
      if (location.hash.indexOf('#case-') === 0) history.replaceState(null, '', location.pathname + location.search);
    });
    $('#sheet-close').addEventListener('click', closeCase);
    sheet.addEventListener('click', function (e) { if (e.target === sheet) closeCase(); });
    document.addEventListener('click', function (e) {
      var link = e.target.closest('.card-link');
      if (!link) return;
      var i = caseIndex(link.getAttribute('href').slice(1));
      if (i > -1) { e.preventDefault(); openCase(i); }
    });
    if (location.hash.indexOf('#case-') === 0) { var hi = caseIndex(location.hash.slice(1)); if (hi > -1) openCase(hi); }

    if (window.matchMedia('(hover: hover)').matches && !reduce) {
      cards.forEach(function (card, ci) {
        var media = $('.card-media', card), srcs = cases[ci].imgs.map(function (im) { return im.getAttribute('src'); });
        if (srcs.length < 2 || $('.duo', media)) return;
        var layer = null, t = null, k = 0;
        card.addEventListener('mouseenter', function () {
          srcs.forEach(function (s) { var p = new Image(); p.src = s; });
          if (!layer) { layer = document.createElement('img'); layer.className = 'cycle'; layer.alt = ''; media.appendChild(layer); }
          t = setInterval(function () { k = (k + 1) % srcs.length; layer.src = srcs[k]; layer.classList.add('on'); }, 800);
        });
        card.addEventListener('mouseleave', function () { clearInterval(t); k = 0; if (layer) layer.classList.remove('on'); });
      });
    }
  }

  /* Leaving for the contact page: remember what the visitor was looking at */
  document.addEventListener('click', function (e) {
    var a = e.target.closest('[data-about]');
    if (a) store('pbt-about', a.dataset.about);
  });

  /* Photography: filter by kind, open a photo large */
  var shots = $$('.shot'), filters = $$('.filters button');
  if (shots.length) {
    var counts = { all: shots.length };
    shots.forEach(function (s) { s.dataset.kind.split(' ').forEach(function (k) { counts[k] = (counts[k] || 0) + 1; }); });
    filters.forEach(function (b) {
      var sup = document.createElement('sup'); sup.textContent = counts[b.dataset.kind] || 0; b.appendChild(sup);
      b.addEventListener('click', function () {
        filters.forEach(function (x) { x.setAttribute('aria-pressed', x === b); });
        shots.forEach(function (s) {
          var show = b.dataset.kind === 'all' || s.dataset.kind.split(' ').indexOf(b.dataset.kind) > -1;
          s.hidden = !show;
          if (show && !reduce) { s.classList.remove('fade'); void s.offsetWidth; s.classList.add('fade'); }
        });
      });
    });
    var lb = $('#lightbox'), lbImg = $('#lb-img'), lbCap = $('#lb-cap'), cur = 0;
    var visible = function () { return shots.filter(function (s) { return !s.hidden; }); };
    var show = function (s) {
      var im = $('img', s); lbImg.src = im.getAttribute('src'); lbImg.alt = im.alt;
      lbCap.innerHTML = $('figcaption', s).innerHTML;
      cur = visible().indexOf(s);
    };
    var step = function (d) { var v = visible(); show(v[(cur + d + v.length) % v.length]); };
    shots.forEach(function (s) {
      s.tabIndex = 0;
      var open = function () { show(s); if (!lb.open) { lb.showModal(); lb.focus(); root.classList.add('lock'); } };
      s.addEventListener('click', open);
      s.addEventListener('keydown', function (e) { if (e.key === 'Enter') open(); });
    });
    lb.addEventListener('close', function () { root.classList.remove('lock'); });
    $('#lb-prev').addEventListener('click', function () { step(-1); });
    $('#lb-next').addEventListener('click', function () { step(1); });
    $('#lb-close').addEventListener('click', function () { lb.close(); });
    lb.addEventListener('keydown', function (e) { if (e.key === 'ArrowRight') step(1); if (e.key === 'ArrowLeft') step(-1); });
    lbImg.addEventListener('click', function () { step(1); });
  }

  /* Prices: tabs */
  var tabs = $$('.tabs [role="tab"]');
  if (tabs.length) {
    var pick = function (t) {
      tabs.forEach(function (x) { x.setAttribute('aria-selected', x === t); x.tabIndex = x === t ? 0 : -1; $('#' + x.getAttribute('aria-controls')).hidden = x !== t; });
    };
    tabs.forEach(function (t) { t.addEventListener('click', function () { pick(t); }); });
    var want = location.hash.slice(1);
    tabs.forEach(function (t) { if (t.dataset.key === want) pick(t); });
  }

  /* Contact: pre-select from the link the visitor came from, then open their email with it all filled in */
  var form = $('#contact-form');
  if (form) {
    var key = location.hash.slice(1);
    var chip = key && $('input[name="interested_in"][data-key="' + key + '"]');
    if (chip) chip.checked = true;
    var seen = store('pbt-about'), msg = $('#f-message');
    if (seen && !msg.value) msg.value = 'Hi Steph, I saw ' + seen + ' and I am planning something similar: ';
    var status = $('#form-status');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var d = new FormData(form);
      var body = 'Name: ' + d.get('name') + '\nEmail: ' + d.get('email') + '\nBrand: ' + (d.get('company') || '-') +
        '\nInterested in: ' + (d.get('interested_in') || '-') + '\n\n' + d.get('message');
      if (form.hasAttribute('data-preview')) { status.textContent = 'Preview only. On paboto.com this opens an email to Steph with your message filled in.'; return; }
      location.href = 'mailto:stephanie@paboto.com?subject=' + encodeURIComponent('New enquiry from ' + d.get('name')) + '&body=' + encodeURIComponent(body);
      status.textContent = 'Your email app should open with the message ready. If it does not, write to stephanie@paboto.com.';
    });
  }

  /* Gentle rise on scroll, from a visible resting state */
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -6% 0px' });
    $$('.rv').forEach(function (el, i) { el.style.transitionDelay = (i % 3) * 60 + 'ms'; io.observe(el); });
  }
})();
