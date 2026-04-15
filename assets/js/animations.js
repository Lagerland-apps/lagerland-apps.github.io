/* ================================================================
   Lagerland Apps — Premium Animations & Interactions
   Performance-first: IntersectionObserver, rAF, passive listeners
   ================================================================ */

(function () {
  'use strict';

  var REDUCED = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- Scroll Reveal (IntersectionObserver) ---- */
  function initScrollReveal() {
    var els = document.querySelectorAll('.reveal, .reveal-scale, .reveal-left, .reveal-right');
    if (!els.length) return;

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.06, rootMargin: '0px 0px -60px 0px' });

    els.forEach(function (el) { observer.observe(el); });
  }

  /* ---- Stagger Grid Children ---- */
  function initStagger() {
    document.querySelectorAll('.stagger').forEach(function (container) {
      Array.from(container.children).forEach(function (child, i) {
        child.style.setProperty('--i', i);
        if (!child.classList.contains('reveal') &&
            !child.classList.contains('reveal-scale')) {
          child.classList.add('reveal');
        }
      });
    });
  }

  /* ---- Glass Navbar Scroll ---- */
  function initNavbar() {
    var topbar = document.querySelector('.topbar');
    if (!topbar) return;
    var ticking = false;

    function update() {
      topbar.classList.toggle('scrolled', window.scrollY > 30);
      ticking = false;
    }

    window.addEventListener('scroll', function () {
      if (!ticking) { requestAnimationFrame(update); ticking = true; }
    }, { passive: true });

    update();
  }

  /* ---- Hero Parallax + Depth (calmed) ---- */
  function initParallax() {
    if (REDUCED) return;
    var media = document.querySelector('.hero-media');
    if (!media) return;
    var ticking = false;

    function update() {
      var y = window.scrollY;
      media.style.setProperty('--parallax-y', (y * 0.06) + 'px');
      var opacity = Math.max(0, 1 - y / 1000);
      media.style.opacity = opacity;
      ticking = false;
    }

    window.addEventListener('scroll', function () {
      if (!ticking) { requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
  }

  /* ---- Parallax Background Layers (calmed) ---- */
  function initBgParallax() {
    if (REDUCED) return;
    var orbs = document.querySelectorAll('.bg-orb');
    if (!orbs.length) return;
    var ticking = false;

    function update() {
      var y = window.scrollY;
      orbs.forEach(function (orb, i) {
        var speed = (i + 1) * 0.018;
        orb.style.transform = 'translateY(' + (y * speed) + 'px)';
      });
      ticking = false;
    }

    window.addEventListener('scroll', function () {
      if (!ticking) { requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
  }

  /* ---- Hero word-by-word reveal (one premium micro-moment) ---- */
  function initHeroWordReveal() {
    if (REDUCED) return;
    var heroH1 = document.querySelector('.hero--home .h1');
    if (!heroH1 || heroH1.dataset.split) return;
    heroH1.dataset.split = '1';

    function wrapNode(node, counter) {
      if (node.nodeType === 3) {
        var text = node.textContent;
        var frag = document.createDocumentFragment();
        var parts = text.split(/(\s+)/);
        parts.forEach(function (p) {
          if (/^\s+$/.test(p)) {
            frag.appendChild(document.createTextNode(p));
          } else if (p.length) {
            var span = document.createElement('span');
            span.className = 'word-reveal';
            span.style.setProperty('--d', (counter.i * 55) + 'ms');
            span.textContent = p;
            frag.appendChild(span);
            counter.i++;
          }
        });
        node.parentNode.replaceChild(frag, node);
      } else if (node.nodeType === 1 && node.tagName !== 'BR') {
        Array.from(node.childNodes).forEach(function (n) { wrapNode(n, counter); });
      }
    }
    wrapNode(heroH1, { i: 0 });
  }

  /* ---- Screenshot Carousel: Drag to Scroll ---- */
  function initCarouselDrag() {
    document.querySelectorAll('.shots').forEach(function (track) {
      var isDown = false, startX, scrollLeft, hasMoved;

      track.addEventListener('mousedown', function (e) {
        isDown = true;
        hasMoved = false;
        track.classList.add('grabbing');
        startX = e.pageX - track.offsetLeft;
        scrollLeft = track.scrollLeft;
      });

      function stop() {
        isDown = false;
        track.classList.remove('grabbing');
      }

      track.addEventListener('mouseleave', stop);
      track.addEventListener('mouseup', stop);

      track.addEventListener('mousemove', function (e) {
        if (!isDown) return;
        e.preventDefault();
        hasMoved = true;
        var x = e.pageX - track.offsetLeft;
        track.scrollLeft = scrollLeft - (x - startX) * 1.5;
      });

      // Prevent click on links after drag
      track.addEventListener('click', function (e) {
        if (hasMoved) e.preventDefault();
      }, true);
    });
  }

  /* ---- Carousel Indicator Dots ---- */
  function initCarouselDots() {
    document.querySelectorAll('.shots').forEach(function (track) {
      var wrapper = track.closest('.section') || track.parentElement;
      var dots = wrapper.querySelectorAll('.shots-dot');
      if (!dots.length) return;
      var shots = track.querySelectorAll('.shot');

      function update() {
        var center = track.scrollLeft + track.clientWidth / 2;
        var closest = 0, minDist = Infinity;

        shots.forEach(function (shot, i) {
          var d = Math.abs(center - (shot.offsetLeft + shot.offsetWidth / 2));
          if (d < minDist) { minDist = d; closest = i; }
        });

        dots.forEach(function (dot, i) {
          dot.classList.toggle('active', i === closest);
        });
      }

      track.addEventListener('scroll', update, { passive: true });
      update();
    });
  }

  /* ---- FAQ Smooth Accordion ---- */
  function initFaqAccordion() {
    document.querySelectorAll('.faq-item').forEach(function (details) {
      var summary = details.querySelector('summary');
      var content = details.querySelector('.faq-a');
      if (!summary || !content) return;

      summary.addEventListener('click', function (e) {
        e.preventDefault();

        if (details.open) {
          content.style.maxHeight = content.scrollHeight + 'px';
          content.style.opacity = '1';
          requestAnimationFrame(function () {
            content.style.maxHeight = '0';
            content.style.opacity = '0';
          });
          var onClose = function () {
            details.open = false;
            content.removeEventListener('transitionend', onClose);
          };
          content.addEventListener('transitionend', onClose);
        } else {
          details.open = true;
          var h = content.scrollHeight;
          content.style.maxHeight = '0';
          content.style.opacity = '0';
          requestAnimationFrame(function () {
            content.style.maxHeight = h + 'px';
            content.style.opacity = '1';
          });
          var onOpen = function () {
            content.style.maxHeight = 'none';
            content.removeEventListener('transitionend', onOpen);
          };
          content.addEventListener('transitionend', onOpen);
        }
      });
    });
  }

  /* ---- Mobile Menu ---- */
  function initMobileMenu() {
    var toggle = document.querySelector('.nav-toggle');
    var nav = document.querySelector('.nav');
    var overlay = document.querySelector('.nav-overlay');
    if (!toggle || !nav) return;

    function close() {
      nav.classList.remove('open');
      if (overlay) overlay.classList.remove('open');
    }

    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      if (overlay) overlay.classList.toggle('open', open);
    });

    if (overlay) overlay.addEventListener('click', close);
    nav.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', close); });
  }

  /* ---- Smooth Scroll for # links ---- */
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(function (a) {
      a.addEventListener('click', function (e) {
        var target = document.querySelector(a.getAttribute('href'));
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });
  }

  /* ---- Typing / Counter Animation for Trust Numbers ---- */
  function initCounters() {
    var els = document.querySelectorAll('[data-count]');
    if (!els.length) return;

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        observer.unobserve(entry.target);

        var el = entry.target;
        var target = parseInt(el.getAttribute('data-count'), 10);
        var suffix = el.getAttribute('data-suffix') || '';
        var duration = 1500;
        var start = performance.now();

        function tick(now) {
          var progress = Math.min((now - start) / duration, 1);
          // Ease out cubic
          var ease = 1 - Math.pow(1 - progress, 3);
          el.textContent = Math.round(target * ease) + suffix;
          if (progress < 1) requestAnimationFrame(tick);
        }

        requestAnimationFrame(tick);
      });
    }, { threshold: 0.3 });

    els.forEach(function (el) { observer.observe(el); });
  }

  /* ================================================================
     INIT
     ================================================================ */
  function init() {
    initStagger();
    initScrollReveal();
    initNavbar();
    initParallax();
    initBgParallax();
    initCarouselDrag();
    initCarouselDots();
    initFaqAccordion();
    initMobileMenu();
    initSmoothScroll();
    initHeroWordReveal();
    initCounters();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
