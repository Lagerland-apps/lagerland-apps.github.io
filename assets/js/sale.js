/* Black Friday 2026 (offer-code sale). Loaded only while _data/sale.json says the sale runs.
   head.html (bf-head.html) has already set html.bf-over / data-bf-phase / data-bf-end before first paint.
   Here: the ribbon's close button, the last-day countdown, the end of the sale while a page stays open,
   and the series filter on /black-friday/. Redeem clicks are counted by GoatCounter's data-goatcounter-click. */
(function () {
  'use strict';
  var h = document.documentElement;
  var end = parseInt(h.getAttribute('data-bf-end'), 10);
  var phase = h.getAttribute('data-bf-phase');

  function over() { h.classList.add('bf-over'); }

  /* Ribbon close: remembered per phase, so it comes back once for the weekend and the last day. */
  var close = document.querySelector('.bf-ribbon__close');
  if (close) close.addEventListener('click', function () {
    h.classList.add('bf-ribbon-off');
    try { localStorage.setItem('bf2026-ribbon-' + phase, 'off'); } catch (e) {}
  });

  /* Countdown on the last day, and hide everything when the end passes on an open page. */
  var cd = document.querySelector('.bf-countdown');
  function tick() {
    var left = end - Date.now();
    if (!(left > 0)) { over(); return false; }
    if (cd && phase === 'last') {
      var m = Math.floor(left / 60000);
      cd.textContent = (cd.getAttribute('data-tpl') || '{h} h {m} min')
        .replace('{h}', Math.floor(m / 60)).replace('{m}', m % 60);
    }
    return true;
  }
  if (end && tick()) setInterval(tick, 30000);

  /* Series filter on the deals page (every card shows without JS). */
  var tabs = Array.prototype.slice.call(document.querySelectorAll('[data-bf-filter]'));
  var cards = Array.prototype.slice.call(document.querySelectorAll('.bf-deal'));
  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      var key = tab.getAttribute('data-bf-filter');
      tabs.forEach(function (t) {
        var on = t === tab;
        t.classList.toggle('is-pressed', on);
        t.setAttribute('aria-pressed', on ? 'true' : 'false');
      });
      cards.forEach(function (c) {
        c.hidden = key !== 'all' && c.getAttribute('data-series') !== key;
      });
    });
  });
})();
