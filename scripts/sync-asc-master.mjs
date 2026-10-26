#!/usr/bin/env node
// Builds the master table (platforms + prices for every app) from the App Store Connect API ONLY.
// Nothing here is read from the site's front matter except the slug used to join on the App Store ID.
//
//   node scripts/sync-asc-master.mjs [--env ~/Downloads/HealthLogger/.env] [--out ..]
//
// Writes:  _data/asc_master.json              (site data, committed)
//          ../MASTER-prices.csv, ../MASTER.md (human views, outside the repo, never published)
//
// Credentials: APP_STORE_CONNECT_ISSUER_ID / _KEY_ID / _API_KEY_PATH from the env file (never printed or stored).
import crypto from "node:crypto";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const args = process.argv.slice(2);
const arg = (n, d) => (args.includes(n) ? args[args.indexOf(n) + 1] : d);
const ENV_FILE = arg("--env", process.env.ASC_ENV_FILE || path.join(os.homedir(), "Downloads/HealthLogger/.env"));
const ONLY = arg("--app", null); // slug, App Store ID or name fragment: refetch just that app and merge it into the existing JSON
const OUT_DIR = path.resolve(ROOT, arg("--out", ".."));

// Display order of the master table's territory columns. Codes are App Store Connect territory IDs.
const TERRITORIES = [
  ["USA", "usa"], ["DEU", "germany"], ["FRA", "france"], ["ITA", "italy"], ["ESP", "spain"],
  ["PRT", "portugal"], ["CHN", "china"], ["JPN", "japan"], ["KOR", "korea"], ["IDN", "indonesia"],
  ["MEX", "mexico"], ["BRA", "brazil"], ["POL", "poland"], ["TUR", "turkey"], ["NLD", "netherlands"],
  ["RUS", "russia"], ["SAU", "saudi_arabia"],
];
const CODES = TERRITORIES.map((t) => t[0]);
const PERIODS = { ONE_WEEK: "weekly", ONE_MONTH: "monthly", TWO_MONTHS: "2-month", THREE_MONTHS: "3-month", SIX_MONTHS: "6-month", ONE_YEAR: "yearly" };
const PLATFORM_KEY = { IOS: "iphone", MAC_OS: "macos", TV_OS: "tvos", VISION_OS: "visionos" };
const LIVE = "READY_FOR_SALE";

const env = Object.fromEntries(
  fs.readFileSync(ENV_FILE, "utf8").split("\n").filter((l) => /^[A-Z_]+=/.test(l))
    .map((l) => [l.split("=")[0], l.slice(l.indexOf("=") + 1).trim().replace(/^["']|["']$/g, "")]),
);
for (const k of ["APP_STORE_CONNECT_ISSUER_ID", "APP_STORE_CONNECT_KEY_ID", "APP_STORE_CONNECT_API_KEY_PATH"])
  if (!env[k]) throw new Error(`${k} missing in ${ENV_FILE}`);
const key = crypto.createPrivateKey(fs.readFileSync(env.APP_STORE_CONNECT_API_KEY_PATH));
const b64 = (x) => Buffer.from(x).toString("base64url");

let token = null, tokenAt = 0;
function jwt() {
  const now = Math.floor(Date.now() / 1000);
  if (token && now - tokenAt < 600) return token;
  const input = `${b64(JSON.stringify({ alg: "ES256", kid: env.APP_STORE_CONNECT_KEY_ID, typ: "JWT" }))}.${b64(JSON.stringify({ iss: env.APP_STORE_CONNECT_ISSUER_ID, iat: now, exp: now + 1200, aud: "appstoreconnect-v1" }))}`;
  token = `${input}.${b64(crypto.sign("sha256", Buffer.from(input), { key, dsaEncoding: "ieee-p1363" }))}`;
  tokenAt = now;
  return token;
}

let calls = 0;
async function get(p, tries = 5) {
  const url = p.startsWith("http") ? p : `https://api.appstoreconnect.apple.com${p}`;
  for (let i = 0; i < tries; i++) {
    calls++;
    const r = await fetch(url, { headers: { Authorization: `Bearer ${jwt()}` } });
    if (r.status === 429 || r.status >= 500) { await new Promise((s) => setTimeout(s, 1500 * (i + 1))); continue; }
    const t = await r.text();
    if (!r.ok) { const e = new Error(`${r.status} ${p}\n${t.slice(0, 400)}`); e.status = r.status; throw e; }
    return JSON.parse(t);
  }
  throw new Error(`gave up on ${p}`);
}
// Follows links.next so nothing is silently truncated.
async function getAll(p) {
  let res = await get(p);
  const data = [...res.data], included = [...(res.included || [])];
  while (res.links?.next) { res = await get(res.links.next); data.push(...res.data); included.push(...(res.included || [])); }
  return { data, included };
}
async function pool(items, n, fn) {
  const out = new Array(items.length); let i = 0;
  await Promise.all(Array.from({ length: n }, async () => { while (i < items.length) { const k = i++; out[k] = await fn(items[k], k); } }));
  return out;
}

const today = new Date().toISOString().slice(0, 10);
const TERR = `filter[territory]=${CODES.join(",")}`;
const currencies = {};

// Rows (price entries) -> {current, upcoming} per territory. A null startDate means "since the beginning".
function resolve(entries) {
  const byT = {};
  for (const e of entries) (byT[e.territory] ||= []).push(e);
  const out = {};
  for (const c of CODES) {
    const es = (byT[c] || []).filter((e) => !e.endDate || e.endDate > today).sort((a, b) => (a.startDate || "").localeCompare(b.startDate || ""));
    const cur = es.filter((e) => !e.startDate || e.startDate <= today).pop();
    const next = es.find((e) => e.startDate && e.startDate > today);
    out[c] = cur ? { amount: cur.amount, currency: currencies[c] || null, since: cur.startDate || null, ...(next ? { next: { amount: next.amount, from: next.startDate } } : {}) } : null;
  }
  return out;
}

async function subscriptionPrices(subId) {
  const { data, included } = await getAll(`/v1/subscriptions/${subId}/prices?${TERR}&include=subscriptionPricePoint,territory&limit=200`);
  const pp = {};
  for (const i of included) {
    if (i.type === "subscriptionPricePoints") pp[i.id] = i.attributes.customerPrice;
    if (i.type === "territories") currencies[i.id] = i.attributes.currency;
  }
  return resolve(data.map((d) => ({
    territory: d.relationships.territory.data.id,
    amount: pp[d.relationships.subscriptionPricePoint.data?.id] ?? null,
    startDate: d.attributes.startDate,
  })).filter((e) => e.amount != null));
}

const DURATION = { THREE_DAYS: "3 days", ONE_WEEK: "1 week", TWO_WEEKS: "2 weeks", ONE_MONTH: "1 month", TWO_MONTHS: "2 months", THREE_MONTHS: "3 months", SIX_MONTHS: "6 months", ONE_YEAR: "1 year" };
const MODE = { FREE_TRIAL: "free trial", PAY_AS_YOU_GO: "pay as you go", PAY_UP_FRONT: "pay up front" };

// Introductory offers (free trials etc.) active today, per territory, plus a one-line summary.
async function introOffers(subId) {
  const { data } = await getAll(`/v1/subscriptions/${subId}/introductoryOffers?limit=200&include=territory`);
  const per = Object.fromEntries(CODES.map((c) => [c, null]));
  for (const d of data) {
    const c = d.relationships?.territory?.data?.id, a = d.attributes;
    if (!CODES.includes(c) || (a.startDate && a.startDate > today) || (a.endDate && a.endDate <= today)) continue;
    per[c] = { mode: MODE[a.offerMode] || a.offerMode, duration: DURATION[a.duration] || a.duration, periods: a.numberOfPeriods };
  }
  const label = (o) => (o ? `${o.mode}: ${o.periods > 1 ? o.periods + " x " : ""}${o.duration}` : null);
  const labels = new Set(CODES.map((c) => label(per[c])));
  const summary = labels.size === 1 ? label(per[CODES[0]]) : "varies by territory";
  return { summary, per_territory: per };
}

async function iapPrices(iapId) {
  let sch;
  try { sch = await get(`/v2/inAppPurchases/${iapId}/iapPriceSchedule?include=baseTerritory`); } catch (e) { if (e.status === 404) return { base: null, prices: Object.fromEntries(CODES.map((c) => [c, null])) }; throw e; }
  const entries = [];
  for (const kind of ["manualPrices", "automaticPrices"]) {
    const { data, included } = await getAll(`/v1/inAppPurchasePriceSchedules/${sch.data.id}/${kind}?${TERR}&include=inAppPurchasePricePoint,territory&limit=200`);
    const pp = {};
    for (const i of included) {
      if (i.type === "inAppPurchasePricePoints") pp[i.id] = i.attributes.customerPrice;
      if (i.type === "territories") currencies[i.id] = i.attributes.currency;
    }
    for (const d of data) entries.push({
      territory: d.relationships.territory.data.id,
      amount: pp[d.relationships.inAppPurchasePricePoint.data?.id] ?? null,
      startDate: d.attributes.startDate, endDate: d.attributes.endDate,
    });
  }
  return { base: sch.data.relationships.baseTerritory?.data?.id || null, prices: resolve(entries.filter((e) => e.amount != null)) };
}

// iPad and Apple Watch support have no API field of their own. Signals used:
//  - iPad:  the version carries iPad screenshot sets (Apple requires them for iPad-capable apps)
//  - Watch: (a) the version's build bundle contains an embedded "/Watch/<name>.app" (entitlement paths), and
//           (b) the version carries Apple Watch screenshot sets. Either one counts; both are kept as evidence.
async function screenshotSignals(versionId) {
  const locs = await getAll(`/v1/appStoreVersions/${versionId}/appStoreVersionLocalizations?limit=200`);
  const sig = { ipad: false, watch: false };
  await pool(locs.data, 6, async (l) => {
    if (sig.ipad && sig.watch) return;
    const s = await get(`/v1/appStoreVersionLocalizations/${l.id}/appScreenshotSets?limit=50&fields[appScreenshotSets]=screenshotDisplayType`);
    for (const x of s.data) {
      const t = x.attributes.screenshotDisplayType;
      if (t.startsWith("APP_IPAD") || t.startsWith("IMESSAGE_APP_IPAD")) sig.ipad = true;
      if (t.startsWith("APP_WATCH")) sig.watch = true;
    }
  });
  return sig;
}

async function buildHasWatchApp(versionId) {
  let b;
  try { b = await get(`/v1/appStoreVersions/${versionId}/build`); } catch (e) { if (e.status === 404) return null; throw e; }
  if (!b.data) return null; // no build attached to this version
  const r = await get(`/v1/builds/${b.data.id}?include=buildBundles`);
  return (r.included || []).some((x) => Object.keys(x.attributes.entitlements || {}).some((k) => /\.app\/Watch\/[^/]+\.app/.test(k)));
}

// The app's own (upfront) price from the app price schedule: 0 = free app. Manual + automatic prices cover all storefronts.
async function appPrice(appId) {
  let sch;
  try { sch = await get(`/v1/apps/${appId}/appPriceSchedule`); } catch (e) { if (e.status === 404) return null; throw e; }
  if (!sch.data) return null;
  const entries = [];
  for (const kind of ["manualPrices", "automaticPrices"]) {
    let r;
    try { r = await getAll(`/v1/appPriceSchedules/${sch.data.id}/${kind}?${TERR}&include=appPricePoint,territory&limit=200`); } catch (e) { if (e.status === 404) return null; throw e; } // unreleased app: no schedule yet
    const { data, included } = r;
    const pp = {};
    for (const i of included) {
      if (i.type === "appPricePoints") pp[i.id] = i.attributes.customerPrice;
      if (i.type === "territories") currencies[i.id] = i.attributes.currency;
    }
    for (const d of data) entries.push({
      territory: d.relationships.territory.data.id,
      amount: pp[d.relationships.appPricePoint.data?.id] ?? null,
      startDate: d.attributes.startDate, endDate: d.attributes.endDate,
    });
  }
  const prices = resolve(entries.filter((e) => e.amount != null));
  return { free: Number(prices.USA?.amount ?? NaN) === 0, prices };
}

async function platforms(appId) {
  const { data } = await getAll(`/v1/apps/${appId}/appStoreVersions?limit=200&fields[appStoreVersions]=platform,appStoreState,versionString,createdDate`);
  const by = {};
  for (const v of data) (by[v.attributes.platform] ||= []).push({ id: v.id, ...v.attributes });
  const out = {}, detail = {};
  for (const [plat, vs] of Object.entries(by)) {
    vs.sort((a, b) => b.createdDate.localeCompare(a.createdDate));
    const live = vs.find((v) => v.appStoreState === LIVE);
    const latest = live || vs[0];
    const k = PLATFORM_KEY[plat] || plat.toLowerCase();
    out[k] = live ? "live" : "pending";
    detail[k] = { live_version: live?.versionString || null, latest_version: vs[0].versionString, latest_state: vs[0].appStoreState };
    if (plat === "IOS") {
      const sig = await screenshotSignals(latest.id);
      const build = await buildHasWatchApp(latest.id);
      out.ipad = sig.ipad ? out[k] : null;
      const watch = sig.watch || build === true;
      out.watchos = watch ? out[k] : null;
      detail.watchos = { in_build: build, watch_screenshots: sig.watch, checked_version: latest.versionString };
    }
  }
  return { platforms: out, detail };
}

function slugMap() {
  const m = {};
  const dir = path.join(ROOT, "_apps");
  for (const f of fs.readdirSync(dir).filter((f) => f.endsWith(".md"))) {
    const t = fs.readFileSync(path.join(dir, f), "utf8");
    const id = t.match(/^app_store_url:\s*"?https:\/\/apps\.apple\.com\/[^"\n]*\/?id(\d+)/m)?.[1];
    const slug = t.match(/^slug:\s*"?([\w-]+)/m)?.[1];
    if (id && slug) m[id] = slug;
  }
  return m;
}

const OVERRIDES_PATH = path.join(ROOT, "_data/asc_master_overrides.json");
const overrides = fs.existsSync(OVERRIDES_PATH) ? JSON.parse(fs.readFileSync(OVERRIDES_PATH, "utf8")).products || {} : {};
const slugs = slugMap();
const JSON_PATH = path.join(ROOT, "_data/asc_master.json");
const previous = ONLY && fs.existsSync(JSON_PATH) ? JSON.parse(fs.readFileSync(JSON_PATH, "utf8")) : null;
if (ONLY && !previous) throw new Error("--app needs an existing _data/asc_master.json; run a full sync first");
for (const t of previous?.territories || []) if (t.currency) currencies[t.code] = t.currency;
let apps = (await getAll("/v1/apps?limit=200&fields[apps]=name,bundleId")).data;
if (ONLY) {
  const n = ONLY.toLowerCase();
  apps = apps.filter((a) => a.id === ONLY || slugs[a.id] === n || a.attributes.name.toLowerCase().includes(n));
  if (!apps.length) throw new Error(`no app matches --app ${ONLY}`);
}
const result = [];
for (const a of apps) {
  process.stderr.write(`${a.attributes.name}\n`);
  const { platforms: plat, detail } = await platforms(a.id);
  const groups = (await getAll(`/v1/apps/${a.id}/subscriptionGroups?limit=200`)).data;
  const subs = [];
  for (const g of groups) {
    const ss = (await getAll(`/v1/subscriptionGroups/${g.id}/subscriptions?limit=200`)).data;
    for (const s of ss) subs.push({
      kind: "subscription", period: PERIODS[s.attributes.subscriptionPeriod] || s.attributes.subscriptionPeriod,
      product_id: s.attributes.productId, name: s.attributes.name, state: s.attributes.state, group: g.attributes.referenceName,
      family_sharable: s.attributes.familySharable,
      intro_offer: await introOffers(s.id),
      prices: await subscriptionPrices(s.id),
    });
  }
  const iaps = (await getAll(`/v1/apps/${a.id}/inAppPurchasesV2?limit=200&fields[inAppPurchases]=productId,name,inAppPurchaseType,state,familySharable`)).data;
  const iapRows = await pool(iaps, 4, async (i) => {
    const { base, prices } = await iapPrices(i.id);
    return { kind: i.attributes.inAppPurchaseType === "NON_CONSUMABLE" && /lifetime/i.test(i.attributes.productId) ? "lifetime" : "iap",
      iap_type: i.attributes.inAppPurchaseType.toLowerCase(), product_id: i.attributes.productId, name: i.attributes.name,
      state: i.attributes.state, family_sharable: i.attributes.familySharable, base_territory: base, prices };
  });
  result.push({
    id: a.id, slug: slugs[a.id] || null, name: a.attributes.name, bundle_id: a.attributes.bundleId,
    app_store_url: `https://apps.apple.com/app/id${a.id}`, app_price: await appPrice(a.id), platforms: plat, platform_detail: detail,
    products: [...subs.sort((x, y) => x.product_id.localeCompare(y.product_id)), ...iapRows.sort((x, y) => (x.kind === "lifetime" ? -1 : 0) - (y.kind === "lifetime" ? -1 : 0) || x.product_id.localeCompare(y.product_id))],
  });
}
if (previous) {
  const ids = new Set(result.map((a) => a.id));
  result.push(...previous.apps.filter((a) => !ids.has(a.id)));
}
result.sort((a, b) => a.name.localeCompare(b.name));
// Manual overlay: whether a product is shown in the app's own UI (not knowable from the API).
for (const a of result) for (const p of a.products) {
  delete p.offered_in_app; delete p.offered_note;
  const o = overrides[p.product_id];
  if (o) { p.offered_in_app = o.offered_in_app; p.offered_note = o.note || null; }
}

const master = {
  generated_at: new Date().toISOString(), source: "App Store Connect API (api.appstoreconnect.apple.com)",
  note: "Generated by scripts/sync-asc-master.mjs. Do not edit by hand; change prices in App Store Connect and re-run the script.",
  territories: TERRITORIES.map(([code, key]) => ({ code, key, currency: currencies[code] || null })),
  apps: result,
};
fs.writeFileSync(path.join(ROOT, "_data/asc_master.json"), JSON.stringify(master, null, 2) + "\n");

// ---- site export: _data/catalog.json (committed; read by Jekyll) ----
// Keyed by app slug. No product IDs, bundle IDs, App Store IDs of products or names: the master JSON is gitignored
// because those contain the owner's name, so this file must never carry them (guard below throws if one slips in).
const SITE_PLATFORMS = [["iphone", "iOS"], ["ipad", "iPadOS"], ["macos", "macOS"], ["watchos", "watchOS"]];
const TRIAL_LABEL = { "3 days": "3-day", "1 week": "7-day", "2 weeks": "14-day", "1 month": "1-month", "2 months": "2-month", "3 months": "3-month", "6 months": "6-month", "1 year": "1-year" };
const slimPrices = (prices) => Object.fromEntries(CODES.map((c) => [c, prices[c] ? { amount: prices[c].amount, currency: prices[c].currency } : null]));
function trialOf(intro) {
  if (!intro) return null;
  const per = Object.values(intro.per_territory).filter(Boolean);
  const first = intro.per_territory.USA || per[0];
  if (!first || first.mode !== "free trial" || first.periods !== 1) return null;
  const word = TRIAL_LABEL[first.duration];
  return { label: word ? `${word} free trial` : `${first.duration} free trial`, duration: first.duration, varies: intro.summary === "varies by territory" };
}
const catalogApps = {};
for (const a of result) {
  if (!a.slug) continue;
  const live = Object.entries(a.platforms).some(([k, v]) => v === "live" && ["iphone", "ipad", "macos", "watchos"].includes(k));
  const plans = {};
  const others = [];
  for (const p of a.products) {
    if (p.state !== "APPROVED" || p.offered_in_app === false) continue; // only products actually on sale and shown
    if (p.kind === "subscription") {
      plans[p.period] = { family_sharing: !!p.family_sharable, free_trial: trialOf(p.intro_offer), prices: slimPrices(p.prices) };
    } else if (p.kind === "lifetime") {
      plans.lifetime ||= { family_sharing: !!p.family_sharable, free_trial: null, prices: slimPrices(p.prices) };
    } else {
      others.push({ type: p.iap_type, label: p.name, family_sharing: !!p.family_sharable, prices: slimPrices(p.prices) });
    }
  }
  catalogApps[a.slug] = {
    live,
    platforms: SITE_PLATFORMS.filter(([k]) => a.platforms[k] === "live").map(([, label]) => label),
    app_price: a.app_price ? { free: a.app_price.free, prices: slimPrices(a.app_price.prices) } : null,
    plans, other_iaps: others,
  };
}
const catalog = {
  meta: { generated_at: master.generated_at, source: "App Store Connect API", live_app_count: Object.values(catalogApps).filter((x) => x.live).length,
    territories: TERRITORIES.map(([code, key]) => ({ code, key, currency: currencies[code] || null })) },
  apps: catalogApps,
};
const catalogJson = JSON.stringify(catalog, null, 2) + "\n";
if (/carlos|deketkuli/i.test(catalogJson)) throw new Error("catalog.json would contain the owner name; refusing to write it (check product labels)");
fs.writeFileSync(path.join(ROOT, "_data/catalog.json"), catalogJson);

// ---- human views ----
const fmt = (p) => (p ? `${p.amount} ${p.currency}${p.next ? ` (→ ${p.next.amount} from ${p.next.from})` : ""}` : "");
const yn = (b) => (b === true ? "yes" : b === false ? "no" : "");
const q = (s) => `"${String(s ?? "").replace(/"/g, '""')}"`;
const head = ["app", "app_id", "slug", "iphone", "ipad", "macos", "watchos", "kind", "period/type", "product_id", "name", "state", "family_sharing", "free_trial", "shown_in_app", ...CODES.map((c) => `${c} (${currencies[c]})`)];
const rows = [head.map(q).join(",")];
for (const a of result) {
  const plat = [a.name, a.id, a.slug, a.platforms.iphone || "", a.platforms.ipad || "", a.platforms.macos || "", a.platforms.watchos || ""];
  if (a.app_price) rows.push([...plat, "app_price", a.app_price.free ? "free app" : "paid app", "", "App download price", "", "", "", "", ...CODES.map((c) => fmt(a.app_price.prices[c]))].map(q).join(","));
}
for (const a of result) for (const p of a.products)
  rows.push([a.name, a.id, a.slug, a.platforms.iphone || "", a.platforms.ipad || "", a.platforms.macos || "", a.platforms.watchos || "", p.kind, p.period || p.iap_type, p.product_id, p.name, p.state, yn(p.family_sharable), p.intro_offer?.summary || "", p.offered_in_app === false ? "NO (not for sale)" : "", ...CODES.map((c) => fmt(p.prices[c]))].map(q).join(","));
fs.writeFileSync(path.join(OUT_DIR, "MASTER-prices.csv"), rows.join("\n") + "\n");

const mark = (s) => (s === "live" ? "✅" : s === "pending" ? "⏳" : "–");
let md = `# Master table (App Store Connect API)\n\nGenerated ${master.generated_at}. ✅ live · ⏳ not live yet · – not supported.\n\n## Platforms\n\n| App | iPhone | iPad | macOS | Watch | App price (USA) | Other |\n|---|---|---|---|---|---|---|\n`;
for (const a of result) md += `| ${a.name} | ${mark(a.platforms.iphone)} | ${mark(a.platforms.ipad)} | ${mark(a.platforms.macos)} | ${mark(a.platforms.watchos)} | ${a.app_price ? (a.app_price.free ? "Free" : fmt(a.app_price.prices.USA)) : "?"} | ${Object.keys(a.platforms).filter((k) => !["iphone", "ipad", "macos", "watchos"].includes(k)).join(", ")} |\n`;
for (const a of result) {
  md += `\n## ${a.name}\n\n| Product | Type | State | Family sharing | Free trial | In app UI | ${CODES.join(" | ")} |\n|---|---|---|---|---|---|${CODES.map(() => "---").join("|")}|\n`;
  for (const p of a.products) md += `| ${p.product_id} | ${p.period || p.kind === "lifetime" ? p.period || "lifetime" : p.iap_type} | ${p.state} | ${yn(p.family_sharable) || "–"} | ${p.intro_offer?.summary || "–"} | ${p.offered_in_app === false ? "NOT FOR SALE (hidden)" : "–"} | ${CODES.map((c) => fmt(p.prices[c]) || "n/a").join(" | ")} |\n`;
}
fs.writeFileSync(path.join(OUT_DIR, "MASTER.md"), md);
console.error(`done: ${result.length} apps, ${result.reduce((n, a) => n + a.products.length, 0)} products, ${calls} API calls`);
