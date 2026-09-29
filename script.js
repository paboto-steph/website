(function () {
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Reveal on scroll
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduced) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0.05 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('in'); });
  }

  // Opening stage: one image at a time, moving between three positions.
  // Hovering pauses it; clicking opens the project.
  var stage = document.getElementById('stage');
  if (stage) {
    var items = stage.querySelectorAll('.stage-item');
    var cap = document.getElementById('stage-cap');
    var i = 0, slot = 1, paused = false;
    function show(n) {
      items.forEach(function (el) { el.classList.remove('is-active'); });
      var el = items[n];
      el.dataset.slot = slot;
      el.classList.add('is-active');
      cap.textContent = el.dataset.caption;
    }
    show(0);
    if (!reduced) {
      setInterval(function () {
        if (paused || document.hidden) return;
        i = (i + 1) % items.length;
        slot = (slot + 1 + Math.floor(Math.random() * 2)) % 3;
        show(i);
      }, 1400);
    }
    stage.addEventListener('mouseenter', function () { paused = true; });
    stage.addEventListener('mouseleave', function () { paused = false; });
    stage.addEventListener('focusin', function () { paused = true; });
    stage.addEventListener('focusout', function () { paused = false; });
  }

  // Work index: filter by sector
  var filters = document.querySelectorAll('.filter');
  filters.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var f = btn.dataset.filter;
      filters.forEach(function (b) { b.classList.toggle('is-on', b === btn); });
      document.querySelectorAll('#grid .tile').forEach(function (t) {
        t.hidden = f !== 'all' && t.dataset.sectors.split(' ').indexOf(f) === -1;
        if (!t.hidden) t.classList.add('in');
      });
    });
  });

  // Contact form: build an email so it works without a backend
  var form = document.getElementById('contact-form');
  if (form) {
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
  }

  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
  document.documentElement.classList.remove('no-js');
})();
