/* PABOTO · small helpers used by every page. You don't need to touch this file. */
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var root = document.documentElement;
  var preview = !!window.PABOTO_PREVIEW;

  /* Underline the current page in the menu */
  var page = document.body.dataset.page;
  $$('.hdr .nav').forEach(function (a) { if (a.dataset.page === page) a.classList.add('on'); });

  /* The film: keep it still for people who prefer less motion */
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    $$('video[autoplay]').forEach(function (v) { v.removeAttribute('autoplay'); v.pause(); });
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

  /* Photos open large: tap any photo on a project page */
  var lb = $('#lightbox');
  if (lb) {
    var lbImg = $('#lb-img'), lbCap = $('#lb-cap'), group = $$('.media img').filter(function (im) { return !im.closest('a'); }), cur = 0;
    var show = function (i) {
      cur = (i + group.length) % group.length;
      var im = group[cur];
      lbImg.src = im.currentSrc || im.src; lbImg.alt = im.alt;
      lbCap.textContent = im.alt;
    };
    group.forEach(function (im, i) {
      var holder = im.closest('figure') || im;
      holder.tabIndex = 0;
      var open = function () { show(i); if (!lb.open) { lb.showModal(); lb.focus(); root.classList.add('lock'); } };
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
})();
