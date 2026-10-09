/* PABOTO · small helpers used by every page. You don't need to touch this file. */
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var root = document.documentElement;
  root.classList.add('js');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var preview = !!window.PABOTO_PREVIEW;

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
  if (hdr && menuBtn) {
    menuBtn.addEventListener('click', function () { setMenu(!hdr.classList.contains('open')); });
    $$('.hdr nav a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
  }

  /* Film trailers: the card becomes the player when clicked (nothing loads from YouTube or Vimeo before that) */
  $$('a.embed[data-embed]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      if (preview) return; // previews can't show players: open the film in a new tab instead
      e.preventDefault();
      var box = document.createElement('div'), f = document.createElement('iframe');
      box.className = 'embed';
      f.src = a.dataset.embed;
      f.title = a.textContent.trim();
      f.allow = 'autoplay; fullscreen; picture-in-picture; encrypted-media';
      f.allowFullscreen = true;
      box.appendChild(f);
      a.replaceWith(box);
    });
  });

  /* Photos open large: click any photo on the Photography or Projects page */
  var lb = $('#lightbox');
  if (lb) {
    var lbImg = $('#lb-img'), lbCap = $('#lb-cap'), group = [], cur = 0;
    var photos = $$('.shots img, .media img').filter(function (im) { return !im.closest('a'); });
    var show = function (i) {
      cur = (i + group.length) % group.length;
      var im = group[cur], fig = im.closest('figure'), cap = fig && $('figcaption', fig);
      lbImg.src = im.currentSrc || im.src; lbImg.alt = im.alt;
      lbCap.textContent = cap ? cap.textContent : '';
    };
    photos.forEach(function (im) {
      var holder = im.closest('figure') || im;
      holder.tabIndex = 0;
      var open = function () {
        var box = im.closest('.shots, .media');
        group = photos.filter(function (p) { return p.closest('.shots, .media') === box; });
        show(group.indexOf(im));
        if (!lb.open) { lb.showModal(); lb.focus(); root.classList.add('lock'); }
      };
      holder.addEventListener('click', open);
      holder.addEventListener('keydown', function (e) { if (e.key === 'Enter') open(); });
    });
    lb.addEventListener('close', function () { root.classList.remove('lock'); });
    $('#lb-prev').addEventListener('click', function () { show(cur - 1); });
    $('#lb-next').addEventListener('click', function () { show(cur + 1); });
    $('#lb-close').addEventListener('click', function () { lb.close(); });
    lbImg.addEventListener('click', function () { show(cur + 1); });
    lb.addEventListener('keydown', function (e) { if (e.key === 'ArrowRight') show(cur + 1); if (e.key === 'ArrowLeft') show(cur - 1); });
  }

  /* Contact: pick the right option from the link people came from, then open their email with it all filled in */
  var form = $('#contact-form');
  if (form) {
    var key = location.hash.slice(1);
    var chip = key && $('input[name="interested_in"][data-key="' + key + '"]');
    if (chip) chip.checked = true;
    var status = $('#form-status');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var d = new FormData(form);
      var body = 'Name: ' + d.get('name') + '\nEmail: ' + d.get('email') + '\nInterested in: ' + (d.get('interested_in') || '-') + '\n\n' + d.get('message');
      if (preview) { status.textContent = 'Preview only. On paboto.com this opens an email to Steph with your message filled in.'; return; }
      location.href = 'mailto:stephanie@paboto.com?subject=' + encodeURIComponent('New enquiry from ' + d.get('name')) + '&body=' + encodeURIComponent(body);
      status.textContent = 'Your email app should open with the message ready. If it does not, write to stephanie@paboto.com.';
    });
  }

  /* Gentle rise on scroll */
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -6% 0px' });
    $$('.rv').forEach(function (el, i) { el.style.transitionDelay = (i % 4) * 60 + 'ms'; io.observe(el); });
  }
})();
