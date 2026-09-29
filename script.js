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

  // Project viewer: opens a project's images from its <template>
  var viewer = document.getElementById('viewer');
  if (viewer) {
    var title = viewer.querySelector('.viewer-title');
    var body = viewer.querySelector('.viewer-body');
    var lastFocus = null;

    function open(tile) {
      lastFocus = document.activeElement;
      title.innerHTML = tile.querySelector('.cap-title').innerHTML;
      body.innerHTML = '';
      body.appendChild(tile.querySelector('template').content.cloneNode(true));
      viewer.hidden = false;
      viewer.scrollTop = 0;
      document.body.style.overflow = 'hidden';
      viewer.querySelector('.viewer-close').focus();
    }
    function close() {
      viewer.hidden = true;
      document.body.style.overflow = '';
      if (lastFocus) lastFocus.focus();
    }
    document.querySelectorAll('[data-project]').forEach(function (tile) {
      tile.querySelector('.tile-btn').addEventListener('click', function () { open(tile); });
    });
    viewer.querySelector('.viewer-close').addEventListener('click', close);
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !viewer.hidden) close();
    });
  }

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
