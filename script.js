(function () {
  var doc = document.documentElement;
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Nav background once the page scrolls
  var nav = document.getElementById('nav');
  function onScroll() { nav.classList.toggle('scrolled', window.scrollY > 40); }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Reveal on scroll
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduced) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('in'); });
  }

  // Count up the proof numbers
  var counters = document.querySelectorAll('[data-count]');
  if ('IntersectionObserver' in window && !reduced) {
    var co = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target, end = +el.dataset.count, suffix = el.dataset.suffix || '', t0 = null;
        co.unobserve(el);
        function tick(t) {
          if (!t0) t0 = t;
          var p = Math.min((t - t0) / 1400, 1);
          el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3))) + suffix;
          if (p < 1) requestAnimationFrame(tick);
        }
        requestAnimationFrame(tick);
      });
    }, { threshold: 0.6 });
    counters.forEach(function (el) { co.observe(el); });
  }

  // Gallery lightbox
  var lb = document.getElementById('lightbox');
  var lbImg = lb.querySelector('img');
  var lbCap = lb.querySelector('figcaption');
  var items = Array.prototype.slice.call(document.querySelectorAll('.gallery .g'));
  var current = 0, lastFocus = null;

  function show(i) {
    current = (i + items.length) % items.length;
    var img = items[current].querySelector('img');
    lbImg.src = img.src;
    lbImg.alt = img.alt;
    lbCap.innerHTML = items[current].querySelector('figcaption').innerHTML;
  }
  function open(i) {
    lastFocus = document.activeElement;
    show(i);
    lb.hidden = false;
    document.body.style.overflow = 'hidden';
    lb.querySelector('.lb-close').focus();
  }
  function close() {
    lb.hidden = true;
    document.body.style.overflow = '';
    if (lastFocus) lastFocus.focus();
  }
  items.forEach(function (fig, i) {
    fig.tabIndex = 0;
    fig.setAttribute('role', 'button');
    fig.addEventListener('click', function () { open(i); });
    fig.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(i); }
    });
  });
  lb.querySelector('.lb-close').addEventListener('click', close);
  lb.querySelector('.lb-prev').addEventListener('click', function () { show(current - 1); });
  lb.querySelector('.lb-next').addEventListener('click', function () { show(current + 1); });
  lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
  document.addEventListener('keydown', function (e) {
    if (lb.hidden) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowLeft') show(current - 1);
    if (e.key === 'ArrowRight') show(current + 1);
  });

  // Contact form: build an email so it works without a backend
  var form = document.getElementById('contact-form');
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var d = new FormData(form);
    var interests = d.getAll('interest').join(', ') || 'Not specified';
    var subject = 'New enquiry from ' + d.get('name') + (d.get('company') ? ' (' + d.get('company') + ')' : '');
    var body =
      'Name: ' + d.get('name') + '\n' +
      'Email: ' + d.get('email') + '\n' +
      'Company or venue: ' + (d.get('company') || '-') + '\n' +
      'Interested in: ' + interests + '\n\n' +
      d.get('message');
    window.location.href = 'mailto:stephanie@paboto.com?subject=' +
      encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
  });

  document.getElementById('year').textContent = new Date().getFullYear();
  doc.classList.remove('no-js');
})();
