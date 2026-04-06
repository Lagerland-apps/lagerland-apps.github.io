/* Lagerland Apps — Animations & Interactions */

(function () {
  'use strict';

  /* ===== Scroll Reveal (IntersectionObserver) ===== */
  function initScrollReveal() {
    const els = document.querySelectorAll('.reveal, .reveal-scale, .reveal-left, .reveal-right');
    if (!els.length) return;

    const observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

    els.forEach(function (el) { observer.observe(el); });
  }

  /* ===== Staggered Grid Children ===== */
  function initStagger() {
    document.querySelectorAll('.stagger-children').forEach(function (container) {
      Array.from(container.children).forEach(function (child, i) {
        child.style.setProperty('--stagger-index', i);
        if (!child.classList.contains('reveal') &&
            !child.classList.contains('reveal-scale') &&
            !child.classList.contains('reveal-left')) {
          child.classList.add('reveal');
        }
      });
    });
  }

  /* ===== Navbar Glass Transition ===== */
  function initNavbar() {
    var topbar = document.querySelector('.topbar');
    if (!topbar) return;
    var ticking = false;

    function onScroll() {
      if (!ticking) {
        requestAnimationFrame(function () {
          topbar.classList.toggle('scrolled', window.scrollY > 20);
          ticking = false;
        });
        ticking = true;
      }
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll(); // set initial state
  }

  /* ===== Hero Parallax ===== */
  function initParallax() {
    var media = document.querySelector('.hero-media');
    if (!media) return;
    var ticking = false;

    function onScroll() {
      if (!ticking) {
        requestAnimationFrame(function () {
          var offset = window.scrollY * 0.12;
          media.style.setProperty('--parallax-y', offset + 'px');
          ticking = false;
        });
        ticking = true;
      }
    }

    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ===== Screenshot Carousel Drag ===== */
  function initCarouselDrag() {
    document.querySelectorAll('.shots').forEach(function (track) {
      var isDown = false, startX, scrollLeft;

      track.addEventListener('mousedown', function (e) {
        isDown = true;
        track.classList.add('grabbing');
        startX = e.pageX - track.offsetLeft;
        scrollLeft = track.scrollLeft;
      });

      track.addEventListener('mouseleave', stop);
      track.addEventListener('mouseup', stop);

      function stop() {
        isDown = false;
        track.classList.remove('grabbing');
      }

      track.addEventListener('mousemove', function (e) {
        if (!isDown) return;
        e.preventDefault();
        var x = e.pageX - track.offsetLeft;
        track.scrollLeft = scrollLeft - (x - startX) * 1.5;
      });
    });
  }

  /* ===== Screenshot Indicator Dots ===== */
  function initCarouselIndicators() {
    document.querySelectorAll('.shots').forEach(function (track) {
      var dots = track.parentElement.querySelectorAll('.shots-dot');
      if (!dots.length) return;
      var shots = track.querySelectorAll('.shot');

      function updateDots() {
        var scrollCenter = track.scrollLeft + track.clientWidth / 2;
        var closest = 0;
        var closestDist = Infinity;

        shots.forEach(function (shot, i) {
          var center = shot.offsetLeft + shot.offsetWidth / 2;
          var dist = Math.abs(scrollCenter - center);
          if (dist < closestDist) {
            closestDist = dist;
            closest = i;
          }
        });

        dots.forEach(function (dot, i) {
          dot.classList.toggle('active', i === closest);
        });
      }

      track.addEventListener('scroll', updateDots, { passive: true });
      updateDots();
    });
  }

  /* ===== FAQ Smooth Accordion ===== */
  function initFaqAccordion() {
    document.querySelectorAll('.faq-item').forEach(function (details) {
      var summary = details.querySelector('summary');
      var content = details.querySelector('.faq-a');
      if (!summary || !content) return;

      summary.addEventListener('click', function (e) {
        e.preventDefault();

        if (details.open) {
          // Closing
          content.style.maxHeight = content.scrollHeight + 'px';
          content.style.opacity = '1';
          requestAnimationFrame(function () {
            content.style.maxHeight = '0';
            content.style.opacity = '0';
          });
          var onEnd = function () {
            details.open = false;
            content.removeEventListener('transitionend', onEnd);
          };
          content.addEventListener('transitionend', onEnd);
        } else {
          // Opening
          details.open = true;
          var h = content.scrollHeight;
          content.style.maxHeight = '0';
          content.style.opacity = '0';
          requestAnimationFrame(function () {
            content.style.maxHeight = h + 'px';
            content.style.opacity = '1';
          });
          var clearMax = function () {
            content.style.maxHeight = 'none';
            content.removeEventListener('transitionend', clearMax);
          };
          content.addEventListener('transitionend', clearMax);
        }
      });
    });
  }

  /* ===== Mobile Menu Toggle ===== */
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
      var isOpen = nav.classList.toggle('open');
      if (overlay) overlay.classList.toggle('open', isOpen);
    });

    if (overlay) overlay.addEventListener('click', close);

    // Close on nav link click (mobile)
    nav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', close);
    });
  }

  /* ===== Smooth Scroll for Hash Links ===== */
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

  /* ===== Init Everything ===== */
  function init() {
    initStagger();       // must run before reveal so stagger classes are set
    initScrollReveal();
    initNavbar();
    initParallax();
    initCarouselDrag();
    initCarouselIndicators();
    initFaqAccordion();
    initMobileMenu();
    initSmoothScroll();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
