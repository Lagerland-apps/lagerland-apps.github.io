/* ==================================================================
   Lagerland Apps — behavior layer v3
   ------------------------------------------------------------------
   Motion is garnish, never a gate: every element is visible without
   this file (the reveal CSS only applies under html.js, which
   head.html sets). prefers-reduced-motion disables all decoration.

   Class/ID contract with style.css and the layouts:
     .reveal / .reveal-scale / .stagger  → scroll reveal
     .topbar.scrolled                    → slim navbar
     .nav / .nav-toggle / .nav-overlay   → mobile drawer
     .shots / .shots-dot                 → screenshot carousel
     .faq-item / .faq-a                  → FAQ accordion
     [data-count]                        → stat count-up (server-rendered
                                           real value; animation only)
     #sticky-cta[data-hidden]            → app-page download bar
   ================================================================== */
(function () {
  'use strict';

  var REDUCED = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- Scroll reveal -------------------------------------------- */
  function initScrollReveal() {
    var els = document.querySelectorAll('.reveal, .reveal-scale, .stagger > *');
    if (!els.length) return;
    if (REDUCED || !('IntersectionObserver' in window)) {
      els.forEach(function (el) { el.classList.add('visible'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.05, rootMargin: '0px 0px -40px 0px' });
    els.forEach(function (el) { io.observe(el); });

    /* Safety net: anything still hidden after 2.5s becomes visible.
       A missed observer callback must never leave content invisible. */
    setTimeout(function () {
      els.forEach(function (el) { el.classList.add('visible'); });
    }, 2500);
  }

  /* ---- Stagger indices ------------------------------------------ */
  function initStagger() {
    document.querySelectorAll('.stagger').forEach(function (group) {
      Array.prototype.forEach.call(group.children, function (child, i) {
        child.style.setProperty('--i', i);
      });
    });
  }

  /* ---- Navbar scrolled state ------------------------------------ */
  function initNavbar() {
    var bar = document.querySelector('.topbar');
    if (!bar) return;
    var ticking = false;
    function update() {
      bar.classList.toggle('scrolled', window.scrollY > 30);
      ticking = false;
    }
    window.addEventListener('scroll', function () {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    }, { passive: true });
    update();
  }

  /* ---- Mobile drawer -------------------------------------------- */
  function initMobileMenu() {
    var toggle = document.querySelector('.nav-toggle');
    var nav = document.querySelector('.nav');
    var overlay = document.querySelector('.nav-overlay');
    if (!toggle || !nav) return;
    function setOpen(open) {
      nav.classList.toggle('open', open);
      if (overlay) overlay.classList.toggle('open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    }
    toggle.setAttribute('aria-expanded', 'false');
    toggle.addEventListener('click', function () {
      setOpen(!nav.classList.contains('open'));
    });
    if (overlay) overlay.addEventListener('click', function () { setOpen(false); });
    nav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { setOpen(false); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') setOpen(false);
    });
  }

  /* ---- Screenshot carousel: drag + dots -------------------------- */
  function initCarousel() {
    document.querySelectorAll('.shots').forEach(function (track) {
      // Drag-to-scroll (mouse only; touch scrolls natively)
      var isDown = false, startX = 0, startLeft = 0, moved = false;
      track.addEventListener('mousedown', function (e) {
        isDown = true; moved = false;
        startX = e.pageX; startLeft = track.scrollLeft;
        e.preventDefault();
      });
      window.addEventListener('mousemove', function (e) {
        if (!isDown) return;
        var dx = e.pageX - startX;
        if (Math.abs(dx) > 4) moved = true;
        track.scrollLeft = startLeft - dx;
      });
      window.addEventListener('mouseup', function () { isDown = false; });
      track.addEventListener('click', function (e) {
        if (moved) { e.preventDefault(); e.stopPropagation(); moved = false; }
      }, true);

      // Dot indicators
      var section = track.closest('section') || document;
      var dots = section.querySelectorAll('.shots-dot');
      if (!dots.length) return;
      var shots = track.querySelectorAll('.shot');
      var ticking = false;
      function updateDots() {
        var center = track.scrollLeft + track.clientWidth / 2;
        var best = 0, bestDist = Infinity;
        shots.forEach(function (shot, i) {
          var mid = shot.offsetLeft + shot.offsetWidth / 2;
          var d = Math.abs(mid - center);
          if (d < bestDist) { bestDist = d; best = i; }
        });
        dots.forEach(function (dot, i) { dot.classList.toggle('active', i === best); });
        ticking = false;
      }
      track.addEventListener('scroll', function () {
        if (!ticking) { ticking = true; requestAnimationFrame(updateDots); }
      }, { passive: true });
    });
  }

  /* ---- FAQ accordion (animated close/open) ------------------------ */
  function initFaqAccordion() {
    document.querySelectorAll('.faq-item').forEach(function (item) {
      var summary = item.querySelector('summary');
      var body = item.querySelector('.faq-a');
      if (!summary || !body) return;
      summary.addEventListener('click', function (e) {
        if (REDUCED) return; // native <details> toggle, no animation
        e.preventDefault();
        if (item.open) {
          body.style.maxHeight = body.scrollHeight + 'px';
          body.style.opacity = '1';
          requestAnimationFrame(function () {
            body.style.maxHeight = '0';
            body.style.opacity = '0';
          });
          body.addEventListener('transitionend', function onEnd() {
            body.removeEventListener('transitionend', onEnd);
            item.open = false;
            body.style.maxHeight = '';
            body.style.opacity = '';
          });
        } else {
          item.open = true;
          var h = body.scrollHeight;
          body.style.maxHeight = '0';
          body.style.opacity = '0';
          requestAnimationFrame(function () {
            body.style.maxHeight = h + 'px';
            body.style.opacity = '1';
          });
          body.addEventListener('transitionend', function onEnd() {
            body.removeEventListener('transitionend', onEnd);
            body.style.maxHeight = '';
            body.style.opacity = '';
          });
        }
      });
    });
  }

  /* ---- Smooth in-page anchors ------------------------------------ */
  function initSmoothScroll() {
    if (REDUCED) return;
    document.querySelectorAll('a[href^="#"]').forEach(function (a) {
      a.addEventListener('click', function (e) {
        var id = a.getAttribute('href').slice(1);
        if (!id) return;
        var target = document.getElementById(id);
        if (!target) return;
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        history.pushState(null, '', '#' + id);
      });
    });
  }

  /* ---- Stat count-up ----------------------------------------------
     The real value is server-rendered in the HTML; this only replays
     the number as a count-up when the stat scrolls into view. */
  function initCounters() {
    var els = document.querySelectorAll('[data-count]');
    if (!els.length || REDUCED || !('IntersectionObserver' in window)) return;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        io.unobserve(entry.target);
        var el = entry.target;
        var target = parseInt(el.getAttribute('data-count'), 10);
        var suffix = el.getAttribute('data-suffix') || '';
        if (isNaN(target)) return;
        var start = null, DURATION = 1200;
        function step(ts) {
          if (!start) start = ts;
          var p = Math.min((ts - start) / DURATION, 1);
          var eased = 1 - Math.pow(1 - p, 3);
          el.textContent = Math.round(eased * target) + suffix;
          if (p < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
      });
    }, { threshold: 0.3 });
    els.forEach(function (el) { io.observe(el); });
  }

  /* ---- Sticky download bar (app pages) ---------------------------- */
  function initStickyCta() {
    var bar = document.getElementById('sticky-cta');
    var heroCta = document.querySelector('.hero .actions');
    if (!bar) return;
    if (!heroCta || !('IntersectionObserver' in window)) {
      bar.setAttribute('data-hidden', 'false');
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        bar.setAttribute('data-hidden', entry.isIntersecting ? 'true' : 'false');
      });
    }, { rootMargin: '0px 0px -40px 0px' });
    io.observe(heroCta);
  }

  /* ---- Boot ------------------------------------------------------ */
  function init() {
    initStagger();
    initScrollReveal();
    initNavbar();
    initMobileMenu();
    initCarousel();
    initFaqAccordion();
    initSmoothScroll();
    initCounters();
    initStickyCta();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
