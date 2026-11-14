# French glossary per app (fr)

Part of the language sheet `_i18n/fr.md`. Extracted 2026-11-07 from each app's string catalog (read-only) and its French App Store listing (apps.apple.com/fr). French UI strings are verbatim from the catalogs: use them exactly on the site, except where a note says the app string is defective (missing accents, English left in) or uses tu: the site writes vous, so a tu sentence is never quoted, only its feature names are. Store prices here are reference only: the site prints prices from the catalog.

## French glossary, batch 1: aftershift, allpaid, appmeta, appmeta-pulse, chessful

Method (checked 2026-11-07). Read-only extraction from each app's source catalogs under `~/Downloads/` (xcstrings parsed as JSON with `python3 -I`; AfterShift's legacy `.lproj/*.strings` converted with `plutil`). "total" = translatable keys (`shouldTranslate: false` and blank keys excluded); "fr" = keys whose `fr` value has state `translated` (or plural/substitution variations, or a translated stringSet). French values are copied verbatim from the catalogs (apostrophes, NBSP before `:` and typographic quotes kept as in source; note that Pulse uses curly `’` and NBSP before `:`/`;`, the other apps use straight `'`). Every catalog also carries `fr-CA` values (same key counts); only `fr` is used here. App Store data was fetched with curl (Safari UA, `Accept-Language: fr-FR` / `en-US`), saved into `scratchpad/dl1/` and parsed with `python3 -I`; prices keep the NBSP (U+00A0) before `€` and are reference only. Tu/vous counts are rough regex counts on French values (vous = "vous/votre/vos"; tu = "tu/ton/ta/tes/toi/t'"). The App Store listing page also prints the seller's personal name and address; deliberately not copied.

Formality across catalogs (rough): AfterShift **58 vous / ~200 tu (mixed, mostly tu)**, AllPaid 39 / 4 (vous, 4 tu stragglers), AppMeta 187 / 0 (vous, consistent), AppMeta Pulse 123 / 2 (vous), Chessful **158 vous / 168 tu in Localizable (mixed), Lessons 0 / 1083 (tu)**. Brief says the site uses vous, so every app's tu strings are a quote-with-care issue: a French term copied from a tu string must be restated in vous on the site.

---

### 1. AfterShift (`aftershift`, source `shiftworkersleep/`, ID 6757163182)

### French coverage
- Main app, legacy `.lproj` (no xcstrings): `en.lproj/Localizable.strings` 1443 keys, `fr.lproj/Localizable.strings` 1443 keys, 0 missing, 28 values identical to English (e.g. "Premium", "Pro", "REM"-style names). `Localizable.stringsdict` en and fr both present (4 keys each). → **100 %**
- `fr.lproj/AppShortcuts.strings`: 16 Siri/Shortcuts phrases in French (e.g. "Quand commence mon prochain poste dans ${applicationName}", "Enregistre mon sommeil dans ${applicationName}"). Siri phrases ARE in French (unlike German's note for other apps).
- Widget `shiftworkersleepWidget/Localizable.xcstrings`: 15 / 15 → 100 % (widget gallery names live in the main catalog `widget.gallery.*`).
- InfoPlist: `fr.lproj/InfoPlist.strings` has 2 keys: `CFBundleDisplayName` ("AfterShift") and `NSHealthShareUsageDescription` ("AfterShift lit tes données de sommeil depuis Apple Santé pour calculer la dette de sommeil et la récupération entre les quarts." — tu form, and "quarts" where the app body says "postes"). **Not localized:** `NSCalendarsUsageDescription` / `NSCalendarsFullAccessUsageDescription` (build settings only, English: "AfterShift reads your calendar events to automatically detect work shifts…"), so the calendar permission prompt is English on a French device.
- Paywall strings (`paywall.*`) translated.
- **Verdict: app is in French: yes** (one English permission prompt: calendar access).
- Flags: (1) **tu/vous mixed**: most strings tu ("Touche + pour ajouter un poste", paywall "Annule quand tu veux"), but about 58 are vous ("Connectez votre calendrier…", "Partagez avec votre famille — jusqu’à 5 membres", Siri results). (2) **"shift" has two French words**: "poste" (about 148 values: "Prochain poste", "Ajouter un poste", "Changement de poste") vs "quart" (about 37: "Vos quarts", "Quart modifié de…", InfoPlist, `export`/timeline strings). Pick "poste" (main-screen form). (3) "Sleep Score" and "Shift Recovery Score" share one French value (see table). (4) Readiness has 3 forms (see table). (5) `settings.lifetimeActive` is translated ("Premium à vie") unlike German.

### Glossary
| English term on site | English UI string (key) | French UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Today (screen / tab) | Today (`tab.today`) | Aujourd'hui | |
| Coach (screen) | Coach (`tab.coach`, `coach.title`) | Conseils | Not "Coach": the tab is "Conseils" |
| Roster (shift calendar) | Roster (`tab.roster`) | Planning | Widget `widget.gallery.roster.name` also "Planning" |
| Settings | Settings (`tab.settings`, `settings.title`) | Réglages | |
| Shift Recovery Score | Shift Recovery Score (`recovery.shiftRecoveryScore`) | Score de récupération par postes | **Flag:** `sleepScore.title` "Sleep Score" has the identical value, so the site must not present them as two French terms; `sleepScore.unlock` "Unlock sleep score" = "Débloquer le score" |
| Sleep Score | Sleep Score (`sleepScore.title`) | Score de récupération par postes | see above |
| Readiness | Readiness (`readiness.title`; widget `widget.gallery.readiness.name`) | État de récupération | **Flag:** `shiftChange.readiness` "Readiness" = "Niveau de récupération"; `readiness.locked` = "Récupération verrouillée"; `swap.headline.improved` "Readiness should improve" = "La préparation devrait s'améliorer" (préparation). Use "État de récupération" |
| On-call | On-call (`readiness.onCall`, `shift.onCall`) | En astreinte / Astreinte | `schedule.irregular` "Irregular/On-Call" = "Irrégulier/Astreinte"; `coach.onCall.title` "On-call recovery mode" = "Mode récupération d'astreinte" |
| Naps | Naps (`naps.title`) / Nap (`nap.label`) | Siestes / Sieste | `today.logNap` "Log Nap" = "Enregistrer une sieste" |
| Nap window | Optional nap window (`notification.napWindow.title`) | Fenêtre de sieste optionnelle | `insight.notification.napWindow.title` "Nap window" = "Fenêtre de sieste" |
| Sleep window | Sleep window (`notification.sleepWindow.title`) | Fenêtre de sommeil | `intent.sleepWindow.title` "Next Sleep Window" = "Prochaine fenêtre de sommeil" |
| Sleep Timing | Sleep Timing (`timing.title`) | Horaires de sommeil | |
| Sleep debt | Sleep debt trend (`debtTrend.title`); widget Sleep debt | Tendance de la dette de sommeil; Dette de sommeil | |
| Sleep stages Awake / Core / Deep / REM | `stages.awake/core/deep/rem` | Éveillé / Léger / Profond / Paradoxal | Core → "Léger" and REM → "Paradoxal" (Apple Santé's French uses "Cœur" and "REM"); flag for review, don't fix |
| Time in bed | Time in bed (`timing.timeInBed`) | Temps au lit | |
| Fragmentation | Fragmentation (`continuity.fragmentation`) | Fragmentation | `paywall.premium.fragmentation` = "Analyses de fragmentation et continuité" |
| Caffeine timing | Caffeine timing (`coach.caffeine.title`) | Moment de la caféine | **Flag:** `caffeine.header` "Caffeine Timing" = "Consommation de caféine" (means consumption); `caffeine.trend.excellent` uses "timing" ("Excellent timing de caféine…") |
| Caffeine cut-off | Caffeine cutoff (`notification.caffeineCutoff.title`) | Limite de caféine | |
| Wind-down reminder | Wind down (`notification.windDown.title`) | Détente | **Flag:** `insight.notification.windDown.title` "Wind-down time" = "Temps de décompression" |
| Calendar shift import | Import from calendar (`roster.calendarImport`) | Importer depuis le calendrier | `onboarding.calendar.title` = "Importez votre planning" |
| Calendar sync (Premium) | Calendar Sync (`calendar.sectionTitle`) | Synchronisation du calendrier | `calendar.upgradeAutoSync` = "Mise à niveau : synchro automatique, plusieurs calendriers et heures supplémentaires" |
| Overtime | Overtime: (`nextShift.overtime`) | Heures sup : | elsewhere "heures supplémentaires" (`paywall.premium.calendarSync`) |
| Add a shift | Add shift (`roster.addShift`, `today.addShift`) | Ajouter un poste | |
| Shift types | Day / Evening / Night / Off (`shift.day/evening/night/off`) | Jour / Soir / Nuit / Repos | |
| Shift change | Shift change impact (`shiftChange.title`) | Impact du changement de poste | `overtime.extended` uses "Quart modifié de…" (quart) |
| Repeating rotation | Repeating rotation (`roster.rotation`) | Rotation récurrente | `rotation.presets` "Common rotations" = "Rotations courantes". **Flag:** `roster.tapToAdd` French drops "or set up a repeating rotation": "Touche + pour ajouter un poste" |
| Three-shift (day → evening → night) | `rotation.preset.threeShift` (+ `.sub`) | Rotation 3×8 (sub: Jour → soir → nuit, 2 de chaque) | Name says "3×8" (French trade term); sub keeps the arrows, lowercase "soir/nuit" |
| 4-on-4-off | `rotation.preset.fourOnFourOff` | 4 postes / 4 repos | sub: "Quatre nuits, puis quatre jours de repos" |
| 4-on-3-off | `rotation.preset.fourOnThreeOff` | 4 postes / 3 repos | sub: "Quatre jours, puis trois de repos" |
| 2 days / 2 nights | `rotation.preset.ddnn` | 2 jours / 2 nuits | sub: "Deux jours, deux nuits, quatre repos" |
| Panama/Pitman (2-2-3) | `rotation.preset.panama` | Panama (2-2-3) | sub: "2-2-3 en rotation, un week-end sur deux de repos" |
| Fixed nights | `rotation.preset.fixedNights` | Nuits fixes | sub: "Cinq nuits, week-ends de repos" |
| Fixed days | `rotation.preset.fixedDays` | Jours fixes | sub: "Cinq jours, week-ends de repos" |
| Trends | Trends (`trends.title`) | Tendances | `today.section.trends` "Trends & Insights" = "Tendances et perspectives" |
| Do this now (playbook) | Do this now (`playbook.cardKicker`) | Fais ça maintenant | tu form; widget `widget.label.doThisNow` = "À faire maintenant" (infinitive, formality-neutral) |
| Techniques | Techniques (`library.title`) | Techniques | |
| Export / PDF report | Export Sleep Report (`settings.exportReport`) | Exporter le rapport de sommeil | `premium.export.title` "Export report" = "Exporter le rapport" |
| Live Activity / Lock Screen | Shift countdown on Lock Screen (`liveactivity.settings.title`) | Compte à rebours du poste sur l'écran verrouillé | |
| Widgets: Next Shift, Shift Plan, Rhythm, Sleep Debt, Roster, Readiness | `widget.gallery.*.name` | Prochain poste, Plan du poste, Rythme, Dette de sommeil, Planning, État de récupération | German list had "Sleep Graph"; the French catalog's widget names are these six |
| Family Sharing | Share with your family — up to 5 members (`paywall.premium.familySharing`) | Partagez avec votre famille — jusqu’à 5 membres | vous form with curly apostrophe (mixed with straight elsewhere) |

### Paid tier names in the French UI (AfterShift)
- Title: **AfterShift Premium** (`paywall.premiumTitle`); `paywall.continuePremium` "Continuer avec Premium"; `paywall.tryPremium` "Essayer AfterShift Premium"; `paywall.unlockForever` "Débloquer Premium à vie".
- **Flag:** the app also says "Pro" ("Pro", `pro.chipLabel`; `widget.insight.unlockPro` "Débloquer avec Pro"; `paywall.lock.techniqueHistory` "Pro te montre…"; `paywall.lifetimeDisclosure` "Toutes les fonctions Pro, pour toujours"). Site term: Premium.
- Periods: Mensuel / Annuel / À vie (`paywall.monthly/yearly/lifetime`); `paywall.month` mois, `paywall.year` an; `settings.lifetimeActive` "Premium à vie"; `paywall.payOnce` "Paiement unique".
- Trial: `paywall.startTrial` "Commencer l'essai gratuit de 7 jours"; `paywall.7dayTrial` "Essai gratuit de 7 jours"; `paywall.freeFor7Days` "gratuit pendant 7 jours".
- Restore: `paywall.restorePurchases` "Restaurer les achats".

### French App Store listing (checked 2026-11-07)
- Name: **AfterShift: Sommeil & Travail** (differs from English "AfterShift: Sleep & Shift Work"); no space before `:`.
- Subtitle: **Récupération et fatigue** (differs from English "Recovery, naps & fatigue").
- Category: **Forme et santé** (English: Health & Fitness). Price: "Gratuit · Achats intégrés". "Uniquement pour iPhone".
- IAPs: `Premium annuel 29,99 €` · `Premium achat unique 44,99 €` · `Soutenir le développeur 1,00 €` · `Premium mensuel 3,99 €` (US: Premium Monthly/Yearly/Lifetime, Support the Developer).
- Langues: "Français et 33 de plus" (Français, Allemand, Anglais, Arabe, Catalan, Chinois simplifié, Chinois traditionnel, Coréen, Croate, Danois, Espagnol, Finnois, Grec, Hindi, Hongrois, Hébreu, Indonésien, Italien, Japonais, Malais, Norvégien, Néerlandais, Polonais, Portugais, Roumain, Russe, Slovaque, Slovène, Suédois, Tchèque, Thaï, Turc, Ukrainien, Vietnamien).

---

### 2. AllPaid (`allpaid`, source `billreminder/`, ID 6757253009)

### French coverage
- Main `Localizable.xcstrings`: 494 / 494 → **100 %** (22 values identical to English: "Pro", "Streaming", brand names).
- `InfoPlist.xcstrings`: 3 / 3 → 100 % (display name "AllPaid"; `NSFaceIDUsageDescription` "Exiger Face ID ou Touch ID pour ouvrir l'app.").
- Widget `billreminderWidget/Localizable.xcstrings`: 57 / 58 → 98.3 % (only `%lld` untranslated, format-only). `billreminderWidgetShared/Widget.xcstrings`: 130 / 130 → 100 %.
- **Not localized:** Siri App Shortcut phrases (`Services/AppIntents/BillsDueIntent.swift`, `AllPaidShortcuts`): no `AppShortcuts.xcstrings` or `.strings` exists, so the phrases are English only. The intent title ("Bills Due This Week" → "Factures cette semaine") and description are translated, the spoken phrases are not. Do not promise French Siri phrases on the page.
- **Verdict: app is in French: yes** (Siri phrases English only).
- Flags: (1) vous throughout except 4 tu strings: "Did you renew?" = "As-tu renouvelé ?", "Pay once, yours forever" = "Paie une fois, c'est à toi pour toujours" (paywall line), "Purchase pending approval…" = "Tu auras accès une fois approuvé.", the "You have %lld bills due this week" notification = "Tu as … factures dues cette semaine". (2) "due" is left English in places: "Due today" = "Due aujourd'hui", "Due tomorrow" = "Due demain", "%@ is due in %lld days." = "%@ est due dans %lld jours." (bad calque; French would be "à échéance"/"à payer"). (3) "Undo" and "Cancel" both = "Annuler". (4) Gender mismatch: "Mark as paid" = "Marquer comme payé" (masc.) but "Mark paid" = "Marquer comme payée" and status "Paid" = "Payée" (fem.). (5) "Utilities" = "Services publics" (bill category; "charges" or "factures de services" would be more common in France).

### Glossary
| English term on site | English UI string (key) | French UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Bills | Bills | Factures | app uses "facture" throughout |
| Add a bill | Add Bill | Ajouter une facture | |
| Mark paid | Mark as paid / Mark paid / Mark %@ as paid | Marquer comme payé / Marquer comme payée / Marquer %@ comme payée | gender inconsistency, see flags; notification action uses one of these |
| Paid | Paid | Payée | |
| Undo | Undo | Annuler | same as Cancel |
| Snooze (notification) | Remind in 2 hours / Remind tomorrow | Rappeler dans 2 heures / Rappeler demain | no single "Snooze" string |
| Monthly calendar | Monthly Calendar | Calendrier mensuel | |
| Total due | Total due | Total dû | |
| Upcoming | Upcoming / Coming Up | À venir | "No upcoming bills" = "Aucune facture à venir" |
| Reminders | Reminders | Rappels | |
| Multiple reminders per bill (Pro) | Multiple reminders per bill | Plusieurs rappels par facture | |
| Due-day reminder | Due-day reminders | Rappels le jour J | |
| Spending analytics (Pro) | Spending Analytics | Analyse des dépenses | "Analytics" alone = "Analyse"; "Spending overview" = "Aperçu des dépenses" |
| Category breakdown | By category | Par catégorie | |
| Monthly trends | Monthly trend | Tendance mensuelle | |
| Full payment history | Full payment history / Payment History | Historique complet des paiements / Historique des paiements | |
| Unlimited bills | Unlimited bills | Factures illimitées | |
| iCloud Sync | iCloud Sync | Synchronisation iCloud | |
| Search / Sort / Notes / Share | Search bills / Sort by / Notes / Share bill | Rechercher des factures / Trier par / Notes / Partager la facture | |
| Billing cycles | Weekly / Bi-weekly / Monthly / Quarterly / Semi-annual / Yearly / Custom | Hebdomadaire / Toutes les deux semaines / Mensuel / Trimestriel / Semestriel / Annuel / Personnalisé | |
| Categories (examples) | Streaming / Subscriptions / Utilities / Housing / Insurance | Streaming / Abonnements / Services publics / Logement / Assurance | |
| Contracts | Contract / Contracts / Contract ends | Contrat / Contrats / Fin du contrat | `Mark as renewed` = "Marquer comme renouvelé"; `Contract ending soon` = "Contrat bientôt terminé" |
| Auto-pay | Auto-pay | Paiement automatique | |
| Documents attached to the bill | Attachment… / DataVault | (pièces jointes) / DataVault | `DataVault` left as English product name; messages say "pièces jointes" |
| App lock (Face ID) | App Lock | Verrouillage de l'app | |
| Family Sharing | Share with up to 5 family members | Partagez avec jusqu’à 5 membres de la famille | |
| Widgets: Next Bill, Horizon, Paid Rhythm (+ Monthly Calendar, Recurring Bills, Week Ahead, Month Progress, Contracts) | widget names | Prochaine facture, Horizon, Rythme des paiements (+ Calendrier mensuel, Factures récurrentes, Semaine à venir, Progression du mois, Contrats) | |
| Free tier | Free plan | Offre gratuite | `Free plan allows up to 3 bills…` = "L'offre gratuite permet jusqu'à 3 factures…". **Note:** `Free: 1` = "Gratuit : 1" refers to contract reminders, not bills |
| Pro | Pro / AllPaid Pro / Upgrade to Pro | Pro / AllPaid Pro / Passer à Pro | `Unlock AllPaid Pro` = "Débloquer AllPaid Pro" |
| Lifetime | Lifetime / Buy Lifetime Access | À vie / Acheter l'accès à vie | App Store IAP calls it "achat unique" (wording differs from in-app "À vie") |
| 7-day free trial | Try Pro free for 7 days | Essayez Pro gratuitement pendant 7 jours | `Start free trial` = "Essai gratuit" |
| Restore Purchases | Restore Purchases | Restaurer les achats | |

### Paid tier names in the French UI (AllPaid)
Pro (`Pro`, `AllPaid Pro`); Mensuel / Annuel / À vie (`Lifetime`); `Start Pro` and `Upgrade to Pro` = "Passer à Pro"; `Unlock` = "Déverrouiller" vs `Unlock AllPaid` = "Débloquer AllPaid" (two verbs); trial "Essayez Pro gratuitement pendant 7 jours" / `Try Pro free for %@` = "Essayez Pro gratuitement pendant %@"; "Annulez à tout moment"; restore "Restaurer les achats". Pro disclosures use "votre identifiant Apple".

### French App Store listing (checked 2026-11-07)
- Name: **AllPaid – Suivi de factures** (en dash, differs from English "AllPaid – Bill Tracker").
- Subtitle: **Payez à temps, sans stress** (differs from English "Pay on time, stress-free"); vous imperative.
- Category: **Utilitaires** (English: Utilities). "Uniquement pour iPhone" (page shows iPhone only even though blueprint says iPhone/iPad/Mac).
- IAPs: `AllPaid Pro mensuel 1,99 €` · `AllPaid Pro achat unique 29,99 €` · `AllPaid Pro annuel 14,99 €` (US: AllPaid Pro Monthly/Yearly/Lifetime).
- Langues: "Français et 33 de plus" (same 34-language list as AfterShift).

---

### 3. AppMeta (`appmeta`, source `metabuilder/`, ID 6758547802, macOS)

### French coverage
- `metabuilder/Localizable.xcstrings`: 2280 / 2298 translatable keys → **99.2 %**. The 18 keys without `fr` are all format-only or symbol strings (` "%@"`, `(%lld %@)`, `%`, `%@ — %@`, `$`, `0%`, `1D`, `7D`, `30D`, `60D`, `90D` and similar). 103 values identical to English (product names, "Pro", "TestFlight", "Issuer ID").
- No InfoPlist.xcstrings, no widgets, no extensions, no permission prompts. Display name "AppMeta" is a brand name.
- **Verdict: app is in French: yes** (only format-only keys lack French).
- Flags: (1) formality is consistent vous (187 / 0). (2) "Locales" = "Langues" but lowercase `locales` = "langues régionales" and `Copy to %lld Locale%@` = "Copier vers %1$lld langue%2$@". (3) Ratings and Reviews collapse: "Reviews" = "Avis" and "Ratings" = "Avis", while "Rating" = "Note". (4) "Unlock Pro" = "Déverrouiller Pro" but `Unlock Lifetime — %@` = "Débloquer l'accès à vie" (two verbs). (5) "Keywords" is consistently "Mots-clés". (6) Analytics = "Analyses", Dashboard = "Tableau de bord" (Pulse uses other words, see below).

### Glossary
| English term on site | English UI string | French UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Locales | Locales | Langues | lowercase `locales` = "langues régionales" |
| Metadata | Metadata | Métadonnées | |
| Name / Subtitle / Promotional Text / Description / What's New | same | Nom / Sous-titre / Texte promotionnel / Description / Nouveautés | |
| Keywords | Keywords | Mots-clés | consistent |
| Keyword Optimizer | Keyword Optimizer | Optimiseur de mots-clés | also "Keyword Opportunities" = "Opportunités de mots-clés", "Keyword Efficiency Dashboard" = "Tableau de bord d'efficacité des mots-clés" |
| Difficulty / Demand / Opportunity | Difficulty / Demand / Opportunity | Difficulté / Demande / Opportunité | |
| Search coverage | App Store Search Coverage / Coverage | Couverture de recherche App Store / Couverture | |
| Preview changes (diff) | Preview Changes | Aperçu des modifications | `Diff previews and sync simulation` = "Aperçus des différences et simulation de synchronisation"; `Diff-first safety` = "Sécurité par les différences" |
| Push | Push / Push All / Push Changes | Envoyer / Tout envoyer / Envoyer les modifications | not "Pousser" |
| Refresh | Refresh | Actualiser | |
| Bulk actions | Bulk Actions / Bulk Copy | Actions groupées / Copie groupée | |
| AI translation | AI Translation / Translate | Traduction par IA / Traduire | |
| AI provider | Provider / Default Provider | Fournisseur / Fournisseur par défaut | |
| AI credits | AI Credits / Buy Credits / Starter Pack / Pro Pack | Crédits IA / Acheter des crédits / Pack Starter / Pack Pro | `AppMeta AI Credits` = "Crédits AppMeta AI" |
| Apple Intelligence | Apple Intelligence | Apple Intelligence | |
| Submit for review | Submit for Review | Soumettre à la vérification | |
| App Review Information | App Review Information | Informations pour la vérification de l'app | |
| Phased release / Age rating / Availability / Pricing | same | Diffusion progressive / Classification d'âge / Disponibilité / Tarification | `Release to All` = "Diffuser à tous" |
| Reviews | Reviews | Avis | also Ratings = "Avis" (collision); Rating = "Note" |
| TestFlight / What to Test | same | TestFlight / Éléments à tester | |
| In-App Purchases / Subscription Groups | same | Achats intégrés / Groupes d'abonnements | |
| Game Center Achievements / Leaderboards | Achievements / Leaderboards | Succès / Classements | |
| Sales and Analytics | Sales / Analytics | Ventes / Analyses | `Open Sales & Trends` = "Ouvrir Ventes et tendances"; `Click Sales and Trends` = "Cliquez sur Ventes et tendances" (consistent) |
| Diagnostics | Diagnostics | Diagnostics | |
| Screenshots | Screenshots | Captures d'écran | |
| Issuer ID / Key ID | same | Issuer ID / ID de clé | Key ID translated, Issuer ID left in English |
| Territories | Territories | Territoires | |
| Dashboard | Dashboard | Tableau de bord | |
| Demo mode | Demo Mode | Mode démo | "Demo (Free)" = "Démo (gratuit)" |
| Pro | Pro / AppMeta Pro / Unlock Pro | Pro / AppMeta Pro / Déverrouiller Pro | `Upgrade to Pro` = "Passer à Pro"; `Unlock AppMeta Pro` = "Déverrouiller AppMeta Pro" |
| Annual / Lifetime | Yearly / Lifetime | Annuel / À vie | `Auto-renews yearly` = "Renouvellement annuel automatique"; `Most popular` = "Le plus populaire"; `Best Value` = "Meilleur rapport"; `Pays off after ~%lld years` = "Rentabilisé après environ %lld ans" |
| Restore Purchases | Restore Purchases | Restaurer les achats | `Manage Subscription` = "Gérer l'abonnement" |

### Paid tier names in the French UI (AppMeta)
**AppMeta Pro** (`Pro`, `AppMeta Pro`); periods "Annuel" (`Yearly`) and "À vie" (`Lifetime`); no monthly plan; no free trial in the app (the `Free Trial` / `Free Trials` strings are analytics labels). Paywall: "Déverrouiller AppMeta Pro", "Passer à l'annuel — %@", "Débloquer l'accès à vie — %@"; `Pay once, own forever` = "Payez une fois, à vous pour toujours". Demo mode is free: "Démo (gratuit)", "Explorer le mode démo" (`Explore Demo Mode` = "Découvrir le mode démo").

### French App Store listing (checked 2026-11-07)
- Name: **AppMeta for App Store Connect** (identical to English, not translated).
- Subtitle: **ASO, métadonnées et avis** (differs from English "Metadata & ASO Tools").
- Category: **Utilitaires** (English: Utilities). "Uniquement pour Mac".
- IAPs: `AppMeta Yearly 19,99 €` · `AppMeta Achat unique 34,99 €` (flag: "Yearly" display name not localized in the store; "Achat unique" has a capital A, unlike the other apps' lowercase "achat unique"). US: AppMeta Lifetime / AppMeta Yearly.
- Langues: "Français et 10 de plus" (Français, Allemand, Anglais, Arabe, Coréen, Espagnol, Italien, Japonais, Portugais, Russe, Turc). Fewer languages than the iPhone apps (no Chinese, Dutch, Swedish, Ukrainian).

---

### 4. AppMeta Pulse (`appmeta-pulse`, source `metabuilder_phone/`, ID 6758788164)

### French coverage
- Main `metabuilder_phone/Localizable.xcstrings`: 999 / 999 → **100 %** (19 values identical to English).
- `AppShortcuts.xcstrings` (Siri phrases): 3 / 3 keys carry a translated stringSet in `fr`: "Ouvrir ${applicationName}", "Afficher les revenus du jour dans ${applicationName}", "Les ventes du jour dans ${applicationName}", "Afficher l’analyse d’apps dans ${applicationName}", "Conversion App Store dans ${applicationName}", "Afficher les abonnés dans ${applicationName}", "Abonnements actifs dans ${applicationName}". (My coverage script counts stringSets separately; checked by hand.)
- Widget `AppMetaPulseWidget/Localizable.xcstrings`: 254 / 254 → **100 %**.
- No InfoPlist.xcstrings; display names "AppMeta Pulse" / "AppMeta Pulse Widget" are brand names.
- **Verdict: app is in French: yes.**
- Flags: (1) vous consistent (123 / 2 tu). (2) Typography is the most careful of the batch: NBSP before `:` and `;`, curly `’`. (3) **Pulse's French uses different terms than AppMeta for the same App Store Connect words**: Analytics = "Analyse d’apps" (AppMeta "Analyses"), Dashboard tab = "Accueil" (widgets say "Tableau de bord 7 j"; AppMeta "Tableau de bord"), Proceeds = "Bénéfices", Reviews = "Avis" (same), Cancelled = "Annulés" but metrics use "Résil./mois" and "Résiliation mensuelle". Check Proceeds ("Bénéfices") against Apple's own French wording in App Store Connect before using it as a site term. (4) "Dashboard" tab "Accueil" is not a literal translation; the site page headline "Dashboard" will need a choice.

### Glossary
| English term on site | English UI string | French UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Dashboard | Dashboard | Accueil | tab; widget locked text "Tableau de bord 7 j verrouillé" |
| Apps | Apps | Apps | |
| Analytics | Analytics | Analyse d’apps | |
| Reviews | Reviews | Avis | `Reply` = "Réponse"; `Reply to this review` = "Répondre à cet avis" |
| Settings | Settings | Réglages | |
| Proceeds | Proceeds | Bénéfices | widget "PROCEEDS" = "BÉNÉFICES"; `Latest Proceeds` = "Derniers bénéfices" |
| Sales | Sales | Ventes | |
| Units | Units | Unités | |
| Revenue | Revenue | Revenus | |
| MRR | MRR | MRR | |
| Active subscriptions | Active Subscriptions / Active Subs | Abonnements actifs / Abos actifs | `Subscription Status` = "État de l’abonnement" |
| Trials | Trials / Active Trials | Essais / Essais actifs | |
| Trial-to-paid conversion | Trial → Paid / Conversion | Essai → abo / Conversion | |
| Churn | Monthly Churn / Churn /mo | Résiliation mensuelle / Résil./mois | |
| Cancellations | Cancels / Cancelled | Annulations / Annulés | |
| New subscriptions | New Subs | Nouv. abos | |
| Downloads / Impressions / Product page views | Downloads / Impressions / Product Page Views | Téléchargements / Impressions / Vues de la page produit | |
| Top territories | Top Territories | Principaux pays et régions | |
| Trend comparison | Compare / Previous period / Last year / Custom Range | Comparer / Période précédente / L’an dernier / Plage personnalisée | |
| Goals | Goals / Monthly Goal | Objectifs / Objectif mensuel | |
| iCloud sync | iCloud Sync | Synchronisation iCloud | same as AllPaid |
| AI review reply drafts | Draft suggestions / AI draft per review | Brouillons suggérés / Brouillon IA par avis | `AI reply drafts, written on your device by Apple Intelligence.` = "Des brouillons de réponse par IA, rédigés sur votre appareil par Apple Intelligence." |
| Display currency | Convert to your preferred currency | Convertir dans la devise de votre choix | |
| Funnel | Funnel | Tunnel | |
| Demo mode | Try with sample data | Essayer avec des données d’exemple | demo is called "Mode démo" (`Demo Mode`) elsewhere |
| Widgets | Home Screen widgets | Widgets de l’écran d’accueil | |
| Paywall bullets | Full access to revenue & subscription metrics / Per-app performance breakdowns / Trends and historical insights / All future updates included | Accès complet aux mesures de revenus et d’abonnements / Performances détaillées par app / Tendances et analyses historiques / Toutes les futures mises à jour incluses | |
| Pro (site plan name) | no UI string | n/a | app never says "Pro" (the `Pro` lookup returns nothing); gating is "Débloquer AppMeta Pulse" |
| Monthly / Yearly / Lifetime | Monthly / Yearly / Lifetime | Mensuel / Annuel / À vie | `One-time purchase · Use forever` = "Achat unique · Utilisation à vie"; `Best Value` = "Meilleure offre"; `Billed monthly` = "Facturation mensuelle" |
| Free trial | Start Free Trial | Essayer gratuitement | `Billed yearly · Free trial included` = "Facturation annuelle · Essai gratuit inclus" |
| Restore Purchases | Restore Purchases / Restore Purchase | Restaurer les achats | |

### Paid tier names in the French UI (Pulse)
No tier name: the whole app is gated. Strings: "Débloquer AppMeta Pulse", "Débloquer l’accès à vie" (`Unlock Lifetime Access`), `Subscribe` = "S’abonner"; periods Mensuel / Annuel / À vie; trial "Essayer gratuitement" and "Essai gratuit, puis %@ par période de facturation."; restore "Restaurer les achats" (both Paywall and Settings, whereas the English paywall says "Restore Purchase").

### French App Store listing (checked 2026-11-07)
- Name: **AppMeta Pulse : Ventes et avis** (NBSP before the colon; differs from English "AppMeta Pulse: Reviews & MRR").
- Subtitle: **Réponses IA, revenus, abonnés** (differs from English "AI Replies, Revenue & Sales").
- Category: **Économie et entreprise** (English: Business). "Uniquement pour iPhone".
- IAPs: `AppMeta Pulse : accès à vie 2,99 €` · `AppMeta Pulse : accès annuel 1,99 €` · `AppMeta Pulse : accès mensuel 0,99 €` (US: AppMeta Pulse Access Lifetime/Yearly/Monthly at the same numbers in $, confirming the low prices are real, not a fetcher error).
- Langues: "Français et 14 de plus" (Français, Allemand, Anglais, Chinois simplifié, Chinois traditionnel, Coréen, Espagnol, Italien, Japonais, Néerlandais, Portugais, Russe, Suédois, Turc, Ukrainien).

---

### 5. Chessful (`chessful`, source `Chessful/`, ID 6761336870)

### French coverage
- `Localizable.xcstrings`: 2124 / 2124 → **100 %** (85 values identical to English: "Stockfish", "Expert", notation).
- `Lessons.xcstrings`: 3649 / 3649 → 100 % (16 identical).
- `InfoPlist.xcstrings`: 2 / 2 → 100 % (display name "Chessful").
- No widget, watch, App Intents or AppShortcuts catalogs; no permission prompts in InfoPlist.
- **Verdict: app is in French: yes.**
- Flags: (1) **tu/vous mixed within the same catalog**: Localizable has about 158 vous vs 168 tu values (zero overlap), and `Lessons.xcstrings` is entirely tu (1083 values). Vous side: paywall and coaching hints ("Annulez à tout moment", "Demandez-vous…"). Tu side: stats and some lessons ("Tu as utilisé tes puzzles gratuits du jour", "Ton classement"). The site (vous) cannot copy phrases verbatim from the tu half. (2) "Back-Rank Weakness" = "Mat sur la dernière rangée manqué" (a descriptive calque; the chess terms are "mat du couloir" and "rangée de base"); don't reuse. (3) "Rating" = "Classement" (meaning "ranking"; for Elo "cote Elo" or "classement Elo"). (4) "Progress" = "Progrès", "Game Review" = "Revue de partie" but "Game Analysis…" = "Analyse de la partie…", and "Review" = "Réviser" (spaced review). (5) "Premium" in app vs "Pro" in store (see tiers). (6) `3-day free trial` strings still in the catalog are stale leftovers (blueprint: trial is 1 week); "3 jours d'essai" is never shown.

### Glossary
| English term on site | English UI string | French UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Dashboard (tab) | Dashboard | Tableau de bord | |
| Play (tab) | Play | Jouer | |
| Analysis (tab) | Analysis | Analyse | |
| Training (tab) | Training | Entraînement | |
| Learn (tab) | Learn | Apprendre | |
| Progress | Progress | Progrès | |
| Game review | Game Review | Revue de partie | `Game Analysis…` = "Analyse de la partie…"; `Analyze Game` = "Analyser" |
| Accuracy | Accuracy | Précision | |
| Key moments | Key Moments | Moments clés | |
| Blunder / Mistake / Inaccuracy | same | Gaffe / Erreur / Imprécision | `Mistake Detail` = "Détail erreur"; `Mistake Hunter` = "Chasseur d'erreurs" |
| Better move | See the better move / Best move | Voir le meilleur coup / Meilleur coup | |
| Today's training | Today's Training | Entraînement du jour | |
| Train your weaknesses | Train Your Weaknesses | Entraînez vos faiblesses | vous |
| Skills (5 dimensions) | Skills | Compétences | |
| Tactics / Defense / Positional / Openings / Endgames | same | Tactique / Défense / Positionnel / Ouvertures / Finales | |
| Opening repertoire | Opening Repertoire | Répertoire d'ouvertures | |
| 40 AI opponents | 40 Unique Opponents | 40 adversaires uniques | levels: Beginner / Intermediate / Advanced / Master = Débutant / Intermédiaire / Avancé / Maître |
| Import games | Import Games / Import from PGN | Importer des parties / Importer depuis un PGN | |
| Analyze all | Analyze All | Tout analyser | |
| Weekly comparison / Weakness trends | same | Comparaison hebdomadaire / Tendances des faiblesses | |
| Rating | Rating | Classement | see flags |
| Achievements | Achievements | Succès | |
| 3D board | 3D Board | Plateau 3D | not "échiquier" |
| Free | Free Plan | Plan gratuit | |
| Pro (site) | Chessful Premium / Upgrade to Premium | site: **Pro** (« Chessful Pro », « Pro · Mensuel ») | owner decision 2026-11-08: the site says **Pro**, like the store IAPs « Chessful Pro … »; the app UI still says Premium until the app fix (Kanban) |
| Monthly / Yearly / Lifetime | same | Mensuel / Annuel / À vie | `Purchase Lifetime` = "Acheter à vie" |
| Free trial | Start Free Trial | Essai gratuit | `%@ free trial` = "%@ d'essai gratuit"; paywall line "Essai gratuit de 3 jours, puis renouvellement automatique" is the stale 3-day string (unused); the trial is 1 week (master): site uses the {TRIAL} token |
| Restore Purchases | Restore Purchases | Restaurer les achats | `Already subscribed? Restore Purchases` = "Déjà abonné ? Restaurer les achats" |
| Hint / Resign / New game | Hint / Resign / New Game | Indice / Abandonner / Nouvelle partie | |

### Paid tier names in the French UI (Chessful)
App: **Premium** ("Chessful Premium", "Passer à Premium", "Premium restauré…"); periods Mensuel / Annuel / À vie; "Essai gratuit" (trial length via StoreKit at runtime, blueprint: 1 week on Monthly and Yearly). Store IAP names: **Chessful Pro mensuel / annuel / achat unique** plus tips "Offrir un café" / "Soutien" / "Grand soutien". Owner decision 2026-11-08: the paid tier is **Pro**. The site says Pro everywhere (« Pro · Mensuel », « Pro · Annuel », « Combien coûte Chessful Pro ? »); the app UI still says Premium until its fix ships (Kanban).

### French App Store listing (checked 2026-11-07)
- Name: **Chessful: Entraîne & Analyse** (differs from English "Chessful: Train & Analyze"). **Flag:** "Entraîne" is a tu imperative (and breaks the vous convention), no space before `:` (Pulse's store name uses NBSP before the colon); flag for the owner.
- Subtitle: **Tactiques d'échecs et puzzles** (differs from English "Chess tactics, puzzles, coach").
- Category: **Jeux de société** (English: Board). Price: "Gratuit · Achats intégrés".
- IAPs: `Chessful Pro annuel 17,99 €` · `Grand soutien 9,99 €` · `Soutien 5,99 €` · `Offrir un café 1,99 €` · `Chessful Pro achat unique 29,99 €` · `Chessful Pro mensuel 2,99 €` (matches `Chessful-IAP-Localizations.md` fr-FR names; US: Chessful Pro Monthly/Lifetime/Yearly, Support the Developer Huge Support/Supporter/Coffee).
- Langues: "Français et 32 de plus" (Français, Allemand, Anglais, Arabe, Catalan, Chinois simplifié, Chinois traditionnel, Coréen, Croate, Danois, Espagnol, Finnois, Grec, Hindi, Hongrois, Hébreu, Indonésien, Italien, Japonais, Malais, Norvégien, Néerlandais, Polonais, Portugais, Roumain, Russe, Slovaque, Suédois, Tchèque, Thaï, Turc, Ukrainien, Vietnamien; no Slovène, which AfterShift/AllPaid have).

---

### Cross-app terms for the French sheet (this batch)
| Concept | Values seen | Recommendation |
|---|---|---|
| Restore Purchases | Restaurer les achats (all five apps) | consistent |
| Lifetime | À vie (all) | consistent; store IAPs say "achat unique" |
| Monthly / Yearly | Mensuel / Annuel (all) | consistent |
| Reviews | Avis (AppMeta, Pulse); AppMeta also uses Avis for Ratings | consistent for Reviews |
| Analytics | Analyses (AppMeta), Analyse d’apps (Pulse), Analyse (AllPaid, Chessful: other meanings) | no single value; choose per app |
| Dashboard | Tableau de bord (AppMeta, Chessful), Accueil (Pulse tab) | choose per app |
| iCloud Sync | Synchronisation iCloud (AllPaid, Pulse) | consistent |
| Free tier | Offre gratuite (AllPaid), Plan gratuit (Chessful) | differ, per app |
| Unlock | Débloquer / Déverrouiller mixed inside AllPaid and AppMeta | note only |
| Formality | AfterShift mixed (mostly tu), Chessful mixed, AllPaid/AppMeta/Pulse vous | site is vous; do not copy tu strings verbatim |


## French glossary, batch 2: earnlock, gymlogger-x, liftlog, mediakit, millrace

Method (checked 2026-11-07, nothing modified outside this file): coverage was counted with a python3 script over each app's `.xcstrings` catalogs (`strings` → key → `localizations.fr` → `stringUnit` / `variations` / `stringSet`, keys with `shouldTranslate: false` excluded) and, for GymLogger X, over the JSON files `GymLogger/Localizations/fr.json`, `GymLoggerWidget/Localizations/fr.json` and `GymLoggerWatch Watch App/Localizations/fr.json` compared with their `en.json`. French UI strings are copied verbatim from the catalogs (plural variations shown as `one:` / `other:`); where a string is quoted from the catalog with a straight or curly apostrophe, the catalog's own character is kept. Tu/vous counts are rough regex counts of strings containing vous/votre/vos versus tu/ton/ta/tes/toi/te/t'. App Store data was fetched raw with curl (Safari User-Agent, `Accept-Language: fr-FR`) from `https://apps.apple.com/fr/app/id<ID>` and compared with `/us/app/id<ID>`; prices there use U+00A0 before the euro sign, and the French names use a normal space before the colon where a space exists (EarnLock and Millrace have "Name : subtitle", the other three have "Name: subtitle", exactly as Apple prints them). The German glossary `_i18n/de-glossary.md` was the checklist. Prices below are reference only. The master file wasn't consulted (out of scope).

Headline flags for the whole batch:
- **No app in this batch is consistent in tu/vous.** EarnLock (about 65 vous vs 59 tu strings in the main catalog, widget/Live Activity/shield/Watch mixed too), GymLogger X (233 vous vs 95 tu), LiftLog (28 vous vs 70 tu; widgets all tu). MediaKit (63 vous, 0 tu) and Millrace (35 vous, 0 tu) are clean vous. The site uses vous (TRANSLATION.md section 13), so site copy must not echo the tu strings when quoting the UI.
- **App Store name/subtitle differ from English for all five apps** (details per app).
- LiftLog's French App Store IAP names (`Équitable`, `Correct`, `Généreux`, `Mécène`) differ from the in-app tier labels (`Juste`, `Bien`, `Généreux`, `Mécène`).
- GymLogger X has 36+ French strings with every accent missing (the Program Creator: `Decharge`, `Createur de programmes`, `Selectionnez`...). That's an app-side bug, so don't copy those values.
- LiftLog has 8 user-visible English fallbacks (`Average`, `Best`, `Best run`, `By month`, `By weekday`, `min`, `Sessions in run`, `Weekly avg`: keys with no `fr` value) and its hint text tells French users to say the English Siri phrases.

---

### 1. EarnLock (earnlock, source `EarnScreen`, ID 6771099230)

#### French coverage

| Catalog | Keys | `fr` present | `fr` translated | % |
|---|---|---|---|---|
| EarnScreen/Localizable.xcstrings (main app) | 621 | 620 | 620 | 99.8% (the one gap is the empty-string key `""`) |
| EarnScreen/AppShortcuts.xcstrings | 9 | 9 | 9 | 100% |
| EarnScreen/InfoPlist.xcstrings | 5 | 3 | 0 (all 3 `needs_review`) | 0% translated, 60% present |
| EarnScreenLiveActivity/Localizable | 148 | 148 | 148 | 100% |
| EarnScreenShield/Localizable | 6 | 6 | 6 | 100% |
| EarnScreenWatchComplications/Localizable | 13 | 13 | 13 | 100% |
| watchkitapp Watch App/Localizable | 28 | 28 | 28 | 100% |
| watchkitapp Watch App/InfoPlist | 4 | 2 | 0 (both `needs_review`) | 0% translated |
| EarnScreenDeviceActivity, EarnScreenShieldAction | 0 | n/a | n/a | empty catalogs |

Not in French or unreviewed: the three permission prompts (HealthKit read, HealthKit write, Photo Library add) have French values but are marked `needs_review`. `CFBundleDisplayName` / `CFBundleName` have no `fr` entry, so the name stays "EarnLock" (the plain brand name; fine). Siri phrases are French and `translated`: e.g. `Quel est mon objectif dans ${applicationName}`, `Démarrer une séance de concentration dans ${applicationName}`. One of them says `déblocage` where the UI says `déverrouillage` (`Progression du déblocage dans ${applicationName}`).

**Verdict: app is in French: yes** (99.8% main app; widgets, Live Activity, shield, Watch and Siri phrases at 100%; only the permission prompts are `needs_review`).

Tone and wording flags:
- tu/vous mixed inside the same screens: main catalog 65 vous-strings vs 59 tu-strings (e.g. `Qu'espérais-tu y trouver ?`, `Touche pour passer à Premium.`, `Bloque autant d'applis que tu veux.` against `Autorisez l'accès à Santé et Temps d'écran pour continuer.`). Live Activity 7 vous / 6 tu, shield 0 / 2 (`Mérite ton accès`, `Ouvre EarnLock pour voir ta progression la plus récente`), Watch mixes `Ouvrez EarnLock sur iPhone` with `Ouvre l'app sur l'iPhone pour passer à Premium.` The Photo Library permission is tu (`Te permet d'enregistrer une carte d'étape dans ta photothèque.`), the two Health permissions are vous.
- "app" vs "appli" mixed: about 43 strings with `appli(s)` and 40 with `app(s)`.

#### Glossary

| English term on site | English UI string (key) | French UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Free (tier) | `Free forever for one app. Go further with Premium.`; `Free plan locks 1 app. Tap to upgrade.`; `Free locks one app. Premium has no limit.` | `Gratuit pour toujours sur une app. Plus loin avec Premium.`; `Le plan gratuit verrouille 1 appli. Touche pour passer à Premium.`; `La version gratuite verrouille une appli. Premium n'a pas de limite.` | No standalone "Free" string. Flag: `plan gratuit` and `version gratuite` both used. |
| Premium | `Premium` | `Premium` | |
| Monthly | `Monthly` | `Mensuel` | `Premium · Monthly` → `Premium · Mensuel` |
| Yearly | `Yearly` | `Annuel` | `Premium · Yearly` → `Premium · Annuel` |
| Lifetime | `Lifetime` | `À vie` | `Premium · Lifetime` → `Premium · À vie`; `Get Lifetime` → `Choisir À vie`; store IAP is `achat unique`. |
| Get Premium (button) | `Get Premium` | `Passer à Premium` | |
| Start free trial (button) | `Start free trial` | `Commencer l'essai gratuit` | |
| 7-day free trial | `7-day free trial, then %@/year`; `7-day free trial, then %@/month` | `Essai gratuit de 7 jours, puis %@/an`; `Essai gratuit de 7 jours, puis %@/mois` | |
| Restore Purchases | `Restore Purchases` | `Restaurer les achats` | |
| Today tab (site says "Home screen") | `Today`; `Go to Today` | `Aujourd'hui`; `Aller à Aujourd'hui` | Same site-vs-app flag as German: the tab is "Today" → "Aujourd'hui". |
| Insights tab | `Insights` | `Analyses` | |
| Insights Day / Week / Month | `Day` / `Week` / `Month` | `Jour` / `Semaine` / `Mois` | |
| Settings tab | `Settings` | `Réglages` | Apple's iOS term. |
| Shadow Week | `Start Shadow Week`; `Shadow Week history`; `Run another Shadow Week` | `Lancer la semaine d'observation`; `Historique des semaines d'observation`; `Refaire une semaine d'observation` | Feature name = **semaine d'observation**, used consistently. `Your shadow week is done` → `Ta semaine d'observation est terminée`; `Enable real blocking` → `Activer le blocage réel`. |
| Reflect (button) | `Reflect` | `Réfléchir` | Same in the app, Live Activity and Watch. |
| Reflection (noun) | `Reflection summary`; `%lld reflections` | `Résumé des réflexions`; one:`%lld réflexion` / other:`%lld réflexions` | |
| Reflection prompt | `What were you hoping to find?` | `Qu'espérais-tu y trouver ?` | tu form. |
| Reflection answers | `Boredom` / `Anxiety` / `FOMO` / `Habit` / `Other` | `Ennui` / `Anxiété` / `FOMO` / `Habitude` / `Autre` | Direct, no softening (unlike the German "Anspannung"). |
| Smart Schedules | `Smart Schedules` / `Smart schedules` | `Horaires intelligents` / `Plannings intelligents` | Flag: inconsistent. The tab/section `Schedules` is `Horaires`; the title-case string is `Horaires intelligents` and the sentence-case one is `Plannings intelligents`. `Smart Schedules + custom app icons` → `Plannings intelligents + icônes d'app personnalisées`. |
| Goal tiers Light / Standard / Challenge | `Light` / `Standard` / `Challenge` | `Léger` / `Standard` / `Défi` | |
| Default schedules | `Work hours` / `Evenings` / `Weekends` / `Sleep` | `Heures de travail` / `Soirs` / `Week-ends` / `Sommeil` | |
| Daily goal | `Daily goal` | `Objectif quotidien` | Also `Progress to goal` → `Progression vers l'objectif`. |
| Adaptive goal | `Adaptive` | `Adaptatif` | |
| Steps | `Steps` | `Pas` | `%lld steps` → one:`%lld pas` / other:`%lld pas` |
| Active minutes | `Active minutes` | `Minutes d'exercice` | Flag: `Free is limited to Steps. Active Minutes and Active Calories are Premium.` uses `La version gratuite se limite aux Pas. Minutes actives et Calories actives sont Premium.` and another string says `minutes actives`. Prefer the goal-picker label `Minutes d'exercice` (it matches Apple's "Exercise minutes"). |
| Active energy / calories | `Active calories` | `Calories actives` | Helper text: `Active energy you burn moving — not your resting burn.` → `L'énergie active brûlée en bougeant — pas au repos.` |
| "2,026 steps until unlock" (shield) | `%@ until unlock`; `1,247 steps until unlock` | `%@ avant déverrouillage`; `1 247 pas avant déverrouillage` | Catalog example uses a space as thousands separator. Shield button `Earn it` → `Mérite-le`; shield title `Earn your way in` → `Mérite ton accès` (tu). |
| Emergency unlock | `Emergency unlock` | `Déverrouillage d'urgence` | `Emergency unlock until %@` → `Déverrouillage d'urgence jusqu'à %@`. |
| Partial unlock | `Partial unlock` | `Déverrouillage partiel` | Consistent between the Live Activity and the main app (`Ton déverrouillage partiel se termine dans 10 minutes.`). |
| Rest day | `Rest day` / `Weekly rest day` | `Jour de repos` / `Jour de repos hebdomadaire` | |
| Streak | `Streak`; `Current streak` | `Série`; `Série en cours` | |
| Streak shields | `Streak shields`; `Shield saved your streak` | `Boucliers de série`; `Le bouclier a sauvé ta série` | |
| Most-attempted blocked app | `Most attempted blocked app today` | `Appli bloquée la plus tentée aujourd'hui` | |
| Screen time saved (estimate) | `Screen time saved (estimated)` | `Temps d'écran économisé (estimation)` | Live Activity: `TIME SAVED` → `TEMPS ÉCONOMISÉ`. |
| Screen Time (Apple feature) | `Allow Screen Time access` | `Autoriser l'accès au Temps d'écran` | Apple's French term: Temps d'écran. |
| Apple Health | `Apple Health` | `Apple Santé` | The app uses "Apple Santé" and "Santé" for the Health app. |
| Locked apps | `Locked apps` | `Apps bloquées` | Elsewhere `Applis ...`; see the app/appli flag. |
| Family Sharing | `Family Sharing supported — Premium unlocks for up to five family members in your Apple Family group.` | `Compatible avec le partage familial — Premium est débloqué pour jusqu'à cinq membres de votre groupe Famille Apple.` | Flag: capitalisation `partage familial` vs `Partage familial` (other string: `Connectez-vous à iCloud pour activer le Partage familial`). Apple writes "Partage familial". |
| Lock-screen/Home-screen widget heatmap | `Activity heatmap` | `Carte thermique d'activité` | |
| Best week / best month | `Best week` / `BEST MONTH` | `Meilleure semaine` / `MEILLEUR MOIS` | |
| Goal cooldown | `Premium can bypass the 24h cooldown on lowering once per week.` | `Premium peut contourner le délai de 24 h sur la baisse une fois par semaine.` | |
| App icons | `Midnight` / `Ember` | `Minuit` / `Braise` | `Mono` not in the catalog. |

Widget names: no widget display-name string for the site's widget list was found in these catalogs (searched `widget`, ring, history, `Open the app to catch up`, `Today's ring`: not found). The Live Activity catalog holds the widget configuration texts (e.g. `A month, a rolling 30 days, or the year.` → `Un mois, les 30 derniers jours ou l'année.`).

#### Paid tier names as the French UI shows them

`Premium` (tier), `Mensuel` / `Annuel` / `À vie`, combined labels `Premium · Mensuel`, `Premium · Annuel`, `Premium · À vie`; button `Passer à Premium`, `Choisir À vie`, `Commencer l'essai gratuit`; `Restaurer les achats`; shared: `Premium · Partagé avec vous`; `EarnLock Premium` (the product name).

#### French App Store listing (fetched 2026-11-07)

- Name: **EarnLock : Temps d'écran** (English: "EarnLock: App Blocker & Focus"). Differs. Page `<title>`: "App EarnLock : Temps d'écran - App Store".
- Subtitle: **Bloqueur d'apps anti-scroll** (English: "Your steps unlock screen time"). Differs.
- IAP as shown (reference): `EarnLock Premium achat unique 22,99 €` · `EarnLock Premium annuel 9,99 €` · `EarnLock Premium mensuel 1,99 €`
- Langues: "Français et 32 de plus"
- Catégorie: **Productivité**
- Compatibility shown: iPhone, Mac (M1+), Apple Vision, Apple Watch. Age 9+.

---

### 2. GymLogger X (gymlogger-x, source `GymLogger`, ID 6755734580)

The app doesn't use `.xcstrings`. UI text comes from JSON files loaded by its LocalizationManager (`GymLogger/Localizations/fr.json`, `GymLoggerWidget/Localizations/fr.json`, `GymLoggerWatch Watch App/Localizations/fr.json`), plus `fr.lproj/InfoPlist.strings`. There's no AppShortcuts catalog. Separate files `ExerciseTranslations.fr.json` and `RehabTranslations.fr.json` hold exercise and rehab names (not audited here).

#### French coverage

| Catalog | Keys (en) | `fr` present | % | identical to English |
|---|---|---|---|---|
| GymLogger/Localizations/fr.json (main app) | 2848 | 2848 | 100% | 137 (loanwords: Pro, 1RM, Deload, Push / Pull / Legs...) |
| GymLoggerWidget/Localizations/fr.json | 115 | 115 | 100% | 7 |
| GymLoggerWatch Watch App/Localizations/fr.json | 98 | 98 | 100% | 6 |
| GymLogger/fr.lproj/InfoPlist.strings | 4 keys | 4 | yes | Display name "GymLogger X"; both Health permissions are French (vous): `GymLogger lit votre fréquence cardiaque et vos calories pour fournir des analyses d'entraînement et suivre vos progrès.` / `GymLogger enregistre vos entraînements terminés dans Apple Santé pour maintenir vos anneaux d'activité et votre historique à jour.` |

**Verdict: app is in French: yes** (100% of keys in app, widget and Watch; permission prompts localized). Quality gaps:
- **Missing accents (app-side bug):** at least 36 strings have no accents at all, concentrated in the Program Creator (44 of the 190 `creator_*` keys with long values have no accented character): `creator_title` = `Createur de programmes`, `creator_generate` = `Generer le programme`, `creator_periodization` = `Style de periodisation`, `creator_periodization_linear` = `Lineaire`, `creator_goal_rehab` = `Reeducation et recuperation`, `creator_muscle_shoulders` = `Epaules`, `creator_deload` = `Decharge`. Don't copy these into the site; use correct spelling.
- **tu/vous mixed:** 233 vous-strings vs 95 tu-strings; the tu strings are mostly the analytics/coach advice (`Tes 7 derniers jours sont une progression sensée...`, `Ton corps a besoin de %@ jours de repos`).
- French typography: some strings lack the space before `!` (`Programme activé!`, `Super début!`), while others have `?` spacing right.
- The app has an "AI Coach" (`ai_coach` → `Coach IA`, `ai_coach_locked_message`), while the English site page says there's no language model and no chat bot. Site copy must not translate "Coach IA" as a feature without checking with the owner.

#### Glossary

| English term on site | English UI string (key) | French UI string (verbatim) | Note |
|---|---|---|---|
| Free | `free` = Free | `Gratuit` | |
| Pro | `widget_pro` = Pro; `gymlogger_pro` = GymLogger X Pro | `Pro`; `GymLogger X Pro` | |
| Pro Monthly | `paywall_plan_monthly` = Monthly | `Mensuel` | `Continue with Monthly` → `Continuer avec le mensuel` |
| Pro Annual | `paywall_plan_yearly` = Yearly; `paywall_yearly_pro` = Yearly Pro | `Annuel`; `Pro Annuel` | The app says "Yearly", not "Annual". |
| Lifetime | `paywall_plan_lifetime` = Lifetime; `paywall_lifetime_pro` = Lifetime Pro | `À vie`; `Pro à Vie` | Flag: capital V in `Pro à Vie` / `Débloquer Pro à Vie`. Store IAP: "achat unique". |
| Restore Purchases | `restore_purchases` | `Restaurer les achats` | |
| Start free trial | `paywall_start_trial` = Start Free Trial; `paywall_trial_text` = 1-week free trial | `Commencer l'essai gratuit`; `1 semaine d'essai gratuit` | Trial in the app is 1 week. |
| Tabs: Home / Training / Progress / Settings | `home_title` / `training_title` / `progress` / `settings` | `Accueil` / `Entraînement` / `Progrès` / `Paramètres` | Flag: uses `Paramètres` where EarnLock/LiftLog use Apple's `Réglages`. |
| Smart Program Creator | `paywall_tile_program_creator` = Smart Program Creator — built around you | `Smart Program Creator — conçu pour vous` | English name kept; `creator_create_program` = `Créer un programme intelligent`; `creator_title` = `Createur de programmes` (unaccented). |
| Plateau detection | `plateau_detection` = Plateau Detection | `Détection de plateau` | Status labels: `plateau_confirmed` = `Plateau détecté`, `plateau_watch` (Monitoring) = `À surveiller`, `plateau_none` (Progressing) = `Progression`. |
| Estimated 1RM | `analytics_estimated_1rm` = Estimated 1RM | `1RM estimé` | LiftLog also uses `1RM estimé`. `widget_e1rm_a11y` = `Maximum estimé sur une répétition`. |
| Deload week | `insert_deload_week` = Insert Deload Week | `Insérer une semaine de décharge` | Flag: `décharge` is the main form (`Essayer une semaine de décharge`, `Envisager une semaine de décharge`) but `load_deload` = `Deload`, `coach_insight_next_block_deload` has `un deload`, and `creator_deload` = `Decharge` (unaccented). |
| Periodization types: linear / DUP / block / wave | `creator_periodization_*` | `Lineaire` / `Ondulatoire (DUP)` / `Par blocs` / `Par vagues` | `Lineaire` is unaccented (bug); correct form would be Linéaire. |
| Splits: Full Body / Upper-Lower / PPL / Push-Pull / Arnold / Bro | `creator_split_*` | `Full body` / `Haut / Bas` / `Push / Pull / Legs` / `Push / Pull` / `Split Arnold` / `Bro split` | Flag: analytics uses `Haut/Bas`, `Poussée / Tirage` (`push_pull_balance`) and `Pousser/Tirer` (`analytics_push_pull`) for the same pair: three forms. |
| Balance cards | `muscle_balance`; `front_back_balance`; `upper_lower_balance` | see `Équilibre musculaire` below; `Avant / Arrière`; `Haut / Bas du corps` | |
| Program library | `programs` = Programs; `example_programs` = Example Programs | `Programmes d'entraînement`; `Programmes exemples` | Flag: `program_workouts` (en "Programs") = `Entraînements du programme`. `paywall_tile_programs` = `Plus de 35 programmes éprouvés`. |
| The Golden Six | `arnold_golden_six_name` | `The Golden Six` | Name left in English. |
| Rest timer | `watch_a11y_rest_timer` = Rest timer | `Minuteur de repos` | Also `Les minuteries de repos se lancent automatiquement.` (`info.logging.bullet3`): minuteur vs minuterie. Heart Rate Rest Timer = `Minuteur de repos par fréquence cardiaque`. |
| Templates | `templates`; `workout_templates` | `Modèles`; `Modèles d'entraînement` | `save_as_template` → `Enregistrer comme modèle`. |
| Superset / Giant set | `superset` / `giant_set` | `Superset` / `Série géante` | Flag: `create_giant_set` = `Créer un set géant` while the rest say `série géante`. LiftLog writes `Super-série`, GymLogger writes `Superset`. |
| Warm-up set | `warmup_set` / `mark_as_warmup` | `Série d'échauffement` / `Marquer comme échauffement` | |
| Sets / Reps | `sets` / `reps` | `Séries` / `Répétitions` | Widget: `Répétitions`; elsewhere `reps` (`Record de reps`). |
| Personal records | `personal_records` = Personal Records; `prs` = PRs | `Records personnels`; `Records` | Consistent in French. |
| Rep-max table | `analytics_rep_max_table` = Rep-Max Table | `Tableau des maxima` | |
| Strength progress | `analytics_strength_progress` | `Progression en force` | |
| Next Move card | `analytics_next_move_label` = Next Move | `Prochaine étape` | |
| Training load ratio | `analytics_acwr_title` | `Ratio de charge d'entraînement` | `training_load` = `Charge d'entraînement`. |
| Set volume vs MEV / MAV / MRV | `analytics_set_volume` | `Volume de séries` | `MEV %1$@ · MAV %2$@ · MRV %3$@` kept as acronyms. |
| Muscle heatmap | `muscle_heatmap` | `Carte thermique musculaire` | |
| Muscle balance | `muscle_balance` | `Équilibre musculaire` | |
| Plate calculator | `plate_calculator` | `Calculateur de disques` | |
| Weekly summary | `weekly_summary_title` | `Résumé hebdomadaire` | |
| Custom exercises | `create_custom_exercise` | `Créer un exercice personnalisé` | |
| Import a coach's spreadsheet program | `import_program` = Import Program; `import_from_spreadsheets` = Spreadsheets (CSV) | `Importer un programme`; `Tableurs (CSV)` | |
| Apple Health export | `health_saved_to_health` = Saved to Apple Health | `Enregistré dans Apple Health` | Flag: this string says "Apple Health" while the Info.plist permissions say `Apple Santé`. |
| Training vs workout | `start_workout` = Start Workout | `Démarrer l'entraînement` | Mixes `entraînement` and `séance`. |
| Family Sharing | `paywall_family_sharing_title` | `Partage familial inclus` | |

#### Paid tier names as the French UI shows them

`Gratuit` / `GymLogger X Pro` / `Pro`; plan cards `Mensuel`, `Annuel` (`Pro Annuel`), `À vie` (`Pro à Vie`, `ACCÈS À VIE`); `Commencer l'essai gratuit`; `Restaurer les achats`; `Continuer avec la version gratuite`; `Acheter l'accès à vie`; `Paiement unique`; `Pas d'abonnement nécessaire`; `MEILLEURE OFFRE`; `LE PLUS POPULAIRE`.

#### French App Store listing (fetched 2026-11-07)

- Name: **GymLogger X: Suivi Fitness** (English: "GymLogger X: Workout Tracker"). Differs.
- Subtitle: **Musculation & Carnet Gym** (English: "Strength Training & Gym Log"). Differs.
- IAP as shown (reference): `GymLogger X Pro achat unique 44,99 €` · `GymLogger X Pro annuel 19,99 €` · `GymLogger X Pro mensuel 1,99 €` · `Support the developer 1,00 €` (name not translated). Coach-program IAPs also exist (not listed here).
- Langues: "Français et 33 de plus"
- Catégorie: **Forme et santé**
- Compatibility shown: iPhone and Apple Watch. Age 9+.

---

### 3. LiftLog (liftlog, source `CoreLift`, ID 6760043411)

#### French coverage

| Catalog | Keys | `fr` present | `fr` translated | % |
|---|---|---|---|---|
| CoreLift/Resources/Localizable.xcstrings (main app) | 991 | 981 | 981 | 99.0% |
| CoreLift/Resources/AppShortcuts.xcstrings | 6 | 6 | 6 (stringSet, 3-4 phrasings each) | 100% |
| CoreLift/Resources/InfoPlist.xcstrings | 4 | 2 | 2 | 50% (both Health permission texts are French; no display-name entry, so "LiftLog") |
| LiftLogWidgets/WidgetLocalizable.xcstrings | 137 | 137 | 137 | 100% |

The 10 main-app keys without `fr`: ` / %lld`, `%@` (symbols only, fine) and eight words that have no English value either, so the key itself shows as English: `Average`, `Best`, `Best run`, `By month`, `By weekday`, `min`, `Sessions in run`, `Weekly avg`. Those eight are real user-visible English strings in the French app.

Siri: the AppShortcuts phrases are French (e.g. `Démarre ma prochaine séance avec ${applicationName}`, `Quelle est ma série dans ${applicationName}`), but the Siri hint in Localizable tells users to say English phrases: `Dites « Start my next workout with LiftLog » pour commencer une séance, ou demandez « What’s my streak in LiftLog? » et « How much did I lift this week in LiftLog? »...`. App-side inconsistency.

Unlike German, the French Health permission texts name the app **LiftLog**, not CoreLift: `LiftLog enregistre vos séances de musculation terminées dans Apple Santé...`.

**Verdict: app is in French: yes** (99% main app, 100% widgets and Shortcuts; 8 English fallbacks in the stats screens).

Tone: 70 tu-strings vs 28 vous-strings in the main catalog; the widgets are all tu (14 tu, 0 vous): `Enregistre ta première séance`, `À ton record`, `Quand tu veux`. Deletion warnings mix tu (`Supprimer cet entraînement peut affecter tes records`) with the vous forms in the paywall and notification texts (`Soyez prévenu à la fin de votre temps de repos...`).

#### Glossary

| English term on site | English UI string (key) | French UI string (verbatim) | Note |
|---|---|---|---|
| Free trial | `Free Trial`; `Free for 7 days.` | `Essai gratuit`; `Gratuit pendant 7 jours.` | `%d days left in trial` → `%d jours restants d’essai`. |
| Tier: Fair | `Fair` | `Juste` | Flag: the French App Store IAP name is **`Équitable`** (`Accès complet · Équitable`). |
| Tier: Good | `Good` | `Bien` | Flag: the French App Store IAP name is **`Correct`** (`Accès complet · Correct`). |
| Tier: Generous | `Generous` | `Généreux` | Same as the store. |
| Tier: Patron | `Patron` | `Mécène` | Same as the store. |
| One-time purchase / no subscription | `One-time purchase`; `No subscription` | `Achat unique`; `Pas d'abonnement` | |
| Restore Purchases | `Restore Purchases` | `Restaurer les achats` | |
| Tabs: Home / Exercises / Programs / Progress / Settings | same | `Accueil` / `Exercices` / `Programmes` / `Progression` / `Réglages` | `Progression` is also the double-progression word. |
| Log set key | `Log set · start rest`; `Log Set` | `Enregistrer la série · lancer le repos`; `Enregistrer une série` | Consistent verb (`Enregistrer`). |
| Rest timer | `Rest Timer` / `Rest timer` | `Minuteur de repos` | Consistent. |
| Estimated 1RM | `Estimated 1RM`; `Est. 1RM` | `1RM estimé`; `1RM est.` | |
| Rep PRs | `Rep PRs`; `PR` | `Records de répétitions`; `RP` | Flag: the badge `PR` → `RP` is an unusual abbreviation (French lifters say "PR" or "record"). |
| Personal bests | `Personal Bests`; `New Personal Bests`; `Personal record` | `Records personnels`; `Nouveaux records personnels`; `Record personnel` | Consistent. |
| Best set / Best volume | `Best Set` / `Best Volume` | `Meilleure série` / `Meilleur volume` | |
| 26-week activity heatmap | `Complete workouts to see your progress and activity heatmap.` | `Termine des entraînements pour voir ta progression et ta carte d’activité.` | Feature name = **carte d’activité** (tu string). |
| Last 30 days | `Last 30 days` | `30 derniers jours` | |
| Training Max | `Training max`; `Set a training max` | `Max d'entraînement`; `Définis ton max d'entraînement` | |
| Double progression / Progression | `Double progression` / `Progression` | `Double progression` / `Progression` | |
| Deload (trigger) | `Deload` | `Décharge` | Consistent with GymLogger X's main form. |
| Adaptive 1RM formula | `Adaptive (recommended)`; `1RM Formula` | `Adaptative (recommandée)`; `Formule 1RM` | |
| Superset / Giant set | `Superset` / `Giant Set` | `Super-série` / `Série géante` | `Create Superset` → `Créer une super-série`. |
| How To (exercise detail) | `How To` | `Comment faire` | |
| Workout | `Workout` | `Séance` | Also `entraînement` in other strings (`Terminez un entraînement` style): `Supprimer cet entraînement`, `séances de musculation`. Flag: both used. |
| Sets / Reps | `Sets` / `Reps` | `Séries` / `Reps` | Flag: `Série` also means Streak (`Streak` → `Série`, `%lld week streak` → `Série de %lld semaines`), so "série" is overloaded inside this one app. |
| Streak | `Streak` | `Série` | |
| Export (JSON / CSV) | `Export Data (CSV)` / `Export Data (JSON)` | `Exporter les données (CSV)` / `Exporter les données (JSON)` | |
| Apple Health | `Apple Health` | `Apple Santé` | |
| Family Sharing | `Family Sharing` | `Partage familial` | |
| Warm-up set | `Warm-up set %lld` | `Série d’échauffement %lld` | |

Program names (StrongLifts 5×5, 5/3/1, ...) stay in English; descriptions are French.

#### Paid tier names as the French UI shows them

LiftLog has no Pro/Premium and no subscription: it's a one-time purchase with four "tiers" that all unlock the same app: `Juste` / `Bien` / `Généreux` / `Mécène` (in-app) against `Équitable` / `Correct` / `Généreux` / `Mécène` (App Store IAP names); buttons `Débloquer`, `Débloquer LiftLog`, `Essai gratuit`, `Restaurer les achats`; `Un seul paiement. À toi pour toujours. Gratuit pendant les 7 prochains jours.` Choosing the site's tier names needs a decision: in-app label or store name.

#### French App Store listing (fetched 2026-11-07)

- Name: **LiftLog: Musculation Carnet** (English: "LiftLog: Workout Gym Tracker"). Differs.
- Subtitle: **Séries, répétitions & séance** (English: "Sets, reps & strength programs"). Differs.
- IAP as shown (reference): `Accès complet · Équitable 9,99 €` · `Accès complet · Correct 22,99 €` · `Accès complet · Généreux 39,99 €` · `Accès complet · Mécène 44,99 €`
- Langues: "Français et 43 de plus"
- Catégorie: **Forme et santé**
- Compatibility shown: iPhone, Mac (M1+), Apple Vision. Age 4+.

---

### 4. MediaKit (mediakit, source `ClearCut`, ID 6761451361)

#### French coverage

| Catalog | Keys | `fr` present | `fr` translated | % |
|---|---|---|---|---|
| MediaKit/Localizable.xcstrings (main app) | 2562 | 2562 | 2562 | 100% |
| MediaKit/AppShortcuts.xcstrings | 6 | 6 | 6 (translated, unlike German's `needs_review`) | 100% |
| MediaKit/InfoPlist.xcstrings | 25 | 22 | 22 | 88% (Photo Library add permission, Speech Recognition permission and the file-type names are French; missing: CFBundleDisplayName, CFBundleName, NSHumanReadableCopyright, so the name stays "MediaKit") |
| MediaKitShareExtension/Localizable.xcstrings | 13 | 13 | 13 | 100% |

**Verdict: app is in French: yes** (100% of the main app, Shortcuts and share extension; permissions localized). Tone: vous throughout (63 vous-strings, 0 tu). Wording flags: loudness is `sonie` in 5 strings and `sonorité` in 2 (`Normaliser la sonie` vs `Normalisation de la sonorité EBU R128`); "preset" is `Préréglage` in 6 strings; `Réglages` (16) is used for Settings; `app` (20) vs `application` (2) vs `appli` (5); `Trim` = `Rogner` while `Crop` = `Recadrer` (Rogner is more usually "crop" in French video tools; a site term for "trim" should be checked).

#### Glossary

| English term on site | English UI string (key) | French UI string (verbatim) | Note |
|---|---|---|---|
| Pro | `Pro` | `Pro` | `Upgrade to Pro` → `Passer à Pro`; `Unlock Pro` → `Débloquer Pro`. |
| Pro · Monthly | `Monthly` | `Mensuel` | |
| Pro · Annual | `Annual` | `Annuel` | |
| Lifetime | `Lifetime` | `À vie` | Store IAP: "MediaKit Pro achat unique". |
| Free trial (3 days) | `Start Free Trial`; `Every tool, 3 days free`; `%@ free trial` | `Commencer l'essai gratuit`; `Tous les outils, 3 jours gratuits`; `Essai gratuit de %@` | Also `Start Your Free Trial` → `Démarrer votre essai gratuit`. |
| Free tier (five tools stay free) | `Free tier` | `Offre gratuite` | |
| Tool (generic) | `Tool`; `Add a Tool to the Recipe` | `Outil`; `Ajouter un outil à la recette` | |
| Recipes (chained tools) | `Recipes`; `Create a new multi-step recipe` | `Recettes`; `Créer une nouvelle recette en plusieurs étapes` | Feature name = **recette**; `Browse Recipe Marketplace` → `Parcourir la place de marché des recettes`. |
| Video Compress / Image Compress | `Compress`; `Compress Video`; `Compress Image` | `Compresser`; `Compresser une vidéo`; `Compresser une image` | |
| Image Resize | `Resize` | `Redimensionner` | |
| Convert (audio, image...) | `Convert`; `Convert Image` | `Convertir`; `Convertir une image` | |
| Categories: Video / Audio / Image / PDF / Archive / Ebook | same | `Vidéo` / `Audio` / `Image` / `PDF` / `Archive` / `Livre numérique` | |
| Batch processing | `Batch Processing` | `Traitement par lots` | |
| Export presets | `Preset`; `Platform preset` | `Préréglage`; `Préréglage de plateforme` | |
| Shortcuts actions | `Shortcuts & Siri` | `Raccourcis et Siri` | Apple's term "Raccourcis". Action phrases e.g. `Compresser une vidéo avec ${applicationName}`, `Fusionner des PDF avec ${applicationName}`. |
| Merge PDFs | `Merge PDFs` | `Fusionner des PDF` | `Merge` → `Fusionner`. |
| Extract text / OCR | `Extract Text from Image`; `OCR` | `Extraire le texte d’une image`; `OCR` | |
| Remove background | `Remove background` | `Supprimer l'arrière-plan` | |
| AI upscale | `AI Upscale` | `Agrandissement IA` | |
| Transcribe | `Transcribe` | `Transcrire` | |
| Strip EXIF metadata | `Strip Metadata` | `Supprimer les métadonnées` | |
| Reduce noise | `Noise Reduce` / `Denoise` | `Réduire le bruit` / `Réduire le bruit` | Same value for both keys. |
| Normalize (EBU R128 / LUFS) | `Normalize loudness`; `EBU R128 loudness normalization` | `Normaliser la sonie`; `Normalisation de la sonorité EBU R128` | Flag: sonie vs sonorité. |
| Redact | `Redact PDF`; `Redact` | `Caviarder un PDF`; `Caviarder` | |
| Compare | `Compare`; `Compare Takes` | `Comparer`; `Comparer les prises` | Consistent. |
| Trim / Merge / Stabilize / Watermark / Sign / Encrypt | same | `Rogner` / `Fusionner` / `Stabiliser` / `Filigrane` / `Signer` / `Chiffrer` | Also `Crop` → `Recadrer`, `Rotate` → `Pivoter`, `Flip` → `Retourner`. |
| Drop a file in | `Drop a file to preview` | `Déposez un fichier pour l’aperçu` | The verb is "déposer"; also `glissez-déposez`. |
| Watch folder | `Watch folder` | `Dossier surveillé` | |
| Menu bar | no UI string | n/a | Use Apple's French term "barre des menus" (not present in the catalog; count 0). |
| Settings | `Settings` | `Réglages` | |
| Restore Purchases | `Restore Purchases` | `Restaurer les achats` | |
| Share extension | `Open in MediaKit`; `Send to MediaKit` | `Ouvrir dans MediaKit`; `Envoyer vers MediaKit` | |

#### Paid tier names as the French UI shows them

`Pro`; `Mensuel` / `Annuel` / `À vie`; `Commencer l'essai gratuit`; `Offre gratuite`; `Passer à Pro`; `Restaurer les achats`. Store IAP names: `MediaKit Pro mensuel`, `MediaKit Pro annuel`, `MediaKit Pro achat unique`.

#### French App Store listing (fetched 2026-11-07)

- Name: **MediaKit: Compresser Vidéo** (English: "MediaKit: Compress & Convert"). Differs.
- Subtitle: **Vidéo, Audio, Image, PDF, ZIP** (English: "Video, Audio, Image, PDF & ZIP"). Differs (no ampersand).
- IAP as shown (reference): `MediaKit Pro annuel 24,99 €` · `MediaKit Pro achat unique 44,99 €` · `MediaKit Pro mensuel 4,99 €`
- Langues: "Français et 11 de plus"
- Catégorie: **Utilitaires**
- Compatibility shown: iPhone, Mac, Apple Vision. Age 4+.

---

### 5. Millrace (millrace, source `thegame`, ID 6759511759)

The site never writes the number the old name contained. None of the French strings below contain it, and the French catalog has 0 strings with it.

#### French coverage

| Catalog | Keys | `fr` present | `fr` translated | % |
|---|---|---|---|---|
| thegame/Localizable.xcstrings (only catalog) | 333 | 333 | 333 | 100% |
| InfoPlist | no InfoPlist.xcstrings | | | Display name "Millrace" comes from the build settings and is the same in every language; the app requests no permissions. |

**Verdict: app is in French: yes (100%).** Tone: vous throughout (35 vous-strings, 0 tu). Flags: `Undo` = `Annuler`, which is also `Cancel` = `Annuler` (button ambiguity, though contexts differ); daily challenge has two forms (`Défi quotidien` vs `Défi du jour`); `Puzzles` = `Casse-tête`, with the singular used as the plural; the theme packs are `Pack Signature 1/2` in French while English says "Designer Pack".

#### Glossary

| English term on site | English UI string (key) | French UI string (verbatim) | Note |
|---|---|---|---|
| Chapter: Warm-up | `Warm-up` | `Échauffement` | |
| Chapter: Tactics | `Tactics` | `Tactique` | |
| Chapter: Pressure | `Pressure` | `Pression` | |
| Chapter: Precision | `Precision` | `Précision` | |
| Chapter: Deep Water | `Deep Water` | `Eaux profondes` | |
| Chapter: Mastery | `Mastery` | `Maîtrise` | |
| Level | `Level %lld` | `Niveau %lld` | No "Chapter" string. |
| Puzzle | `Puzzles`; `Next puzzle` | `Casse-tête`; `Casse-tête suivant` | Store name says "puzzle de chiffres" (the store uses "puzzle"; the app uses "casse-tête"). |
| Freeplay | `Freeplay` | `Jeu libre` | `Merge as long as you can. No goal, no move limit.` → `Fusionnez tant que vous le pouvez. Aucun objectif, aucune limite de coups.` |
| Hint | `Hint` | `Indice` | `Dismiss tip` → `Masquer l'astuce` (astuce vs indice: two words, no clash). |
| The Coach | `Coach`; `Coaching notes` | `Coach`; `Notes du coach` | |
| Daily board / daily challenge | `Daily Challenge` / `Daily challenge` / `Daily` | `Défi quotidien` / `Défi du jour` / `Quotidien` | Flag: inconsistent. No "daily board" string. `Daily Best` → `Record du jour`. |
| Undo | `Undo` | `Annuler` | Noun forms are clean: `10 Undos` → `10 annulations`, `%lld Undos` → one:`%lld annulation` / other:`%lld annulations`, `Undo Tokens` → `Annulations`. |
| Daily streak | `Current Streak` / `Longest Streak` / `Streak Rewards` | `Série actuelle` / `Plus longue série` / `Récompenses de série` | `%lld-day streak: %lld undos` → `Série de %lld jours : %lld annulations`. |
| Personal best | `Personal Best` / `Best` / `NEW BEST` | `Record personnel` / `Record` / `NOUVEAU RECORD` | `Best Score` → `Meilleur score`; `Best Tile` → `Meilleure tuile`. |
| Move budget / moves left | `%lld moves left`; `No moves left` | one:`%lld coup restant` / other:`%lld coups restants`; `Aucun coup possible` | The unit is **coup**. `Best possible is %lld moves` → `Le minimum possible est de %lld coups`. No "move budget" string. |
| Target cell | `…This is the target cell.` | `…C’est la case cible.` | VoiceOver strings; the feature term is **case cible**, and the grid is `plateau` (`sur votre plateau`). |
| Inlet | no UI string | VoiceOver: `Les tuiles arrivent ici.` | The app describes the inlet without naming it (`Tiles keep arriving at the marked cell...` → `Les tuiles arrivent sans cesse sur la case marquée.`). The site needs its own French term; the store subtitle says "une seule entrée". |
| Tile | `%lld tiles arriving` | one:`%lld tuile à venir` / other:`%lld tuiles à venir` | Term = **tuile**. |
| Blocked | `Blocked` | `Bloqué` | |
| Theme / themes | `Theme` / `Themes` | `Thème` / `Thèmes` | |
| Theme packs | `Designer Pack 1` / `Designer Pack 2` / `Summer Pack` / `Winter Pack` | `Pack Signature 1` / `Pack Signature 2` / `Pack Été` / `Pack Hiver` | Matches the store IAP names. |
| Complete Collection | `Complete collection` | `Collection complète` | Also `Unlock All Themes` → `Débloquer tous les thèmes`; `Every theme. Forever.` → `Tous les thèmes. Pour toujours.` |
| Classic (free theme) and theme names | no catalog entries | n/a | Theme names aren't localized. |
| Support the Developer (tip) | `Support the Developer` | `Soutenir le développeur` | |
| Game Center leaderboards / achievements | `Leaderboards` / `Achievements` | `Classements` / `Succès` | |
| Settings: Haptics / Sound Effects / Music | same | `Retour haptique` / `Effets sonores` / `Musique` | |
| Settings | `Settings` | `Réglages` | |
| No subscription | `One-time purchases. No subscription. No ads, ever.` | `Achats uniques. Aucun abonnement. Aucune publicité, jamais.` | |
| Restore Purchases | `Restore Purchases` | `Restaurer les achats` | |

#### Paid tier names as the French UI shows them

Millrace has no Premium/Pro tier. It is free with one-time purchases: `Collection complète`, `Pack Signature 1`, `Pack Signature 2`, `Pack Été`, `Pack Hiver`, undo packs `10 annulations` / `50 annulations` / `200 annulations`, tip `Soutenir le développeur`; buttons `Débloquer`, `Débloquer %@`, `Tout débloquer`, `Restaurer les achats`. No free-trial string.

#### French App Store listing (fetched 2026-11-07)

- Name: **Millrace : puzzle de chiffres** (English: "Millrace: Tile Delivery Puzzle"). Differs. Page `<title>`: "App Millrace : puzzle de chiffres - App Store".
- Subtitle: **64 niveaux, une seule entrée** (English: "64 forged levels, one inlet"). Differs.
- IAP as shown (reference): `Collection complète 6,99 €` · `50 annulations 2,99 €` · `Pack Hiver 1,99 €` · `Soutenir le développeur 1,99 €` · `200 annulations 6,99 €` · `10 annulations 0,99 €` · `Pack Signature 2 1,99 €` · `Pack Signature 1 1,99 €` · `Pack Été 1,99 €`
- Langues: "Français et 33 de plus"
- Catégorie: **Jeux de société** (English storefront: "Board")
- Compatibility shown: iPhone, iPad, Mac (M1+), Apple Vision. Age 4+.


## French glossary, batch 3: mockly, observa, pawza, rightsplit, shogiful

Method (checked 2026-11-07). Read-only. Counts come from a python3 script over every `.xcstrings` in each app's source folder (worktrees and `.build` copies ignored): `strings` → key → `localizations` → `fr` → `stringUnit` (state, value) or `variations`. "Translated" = state `translated`, or a `variations` block. French values are copied verbatim from the catalogs. App Store data comes from `curl` (Safari User-Agent, `Accept-Language: fr-FR`) of `https://apps.apple.com/fr/app/id<ID>` and `/us/app/id<ID>`, parsed from the raw `serialized-server-data` JSON, not a summarizer. Prices use a NO-BREAK SPACE before the euro sign (U+00A0). Prices are reference only. The seller line on the store pages carries the owner's personal name; it is deliberately not copied. Register counts are rough regex counts over `fr` values (vous/votre/vos vs tu/ton/ta/tes/toi/t').

## Summary

| App | Main catalog `fr` | Extensions / other catalogs | InfoPlist / permissions | Verdict |
|---|---|---|---|---|
| Mockly | 332/333 (99.7%) | none | InfoPlist 4/4 | **yes** |
| Observa | 6674/6693 translated (99.7%); 6686 have a `fr` value | Watch 478/480 (99.6%), Widgets 404/406 (99.5%), AppShortcuts 10/15 translated (15/15 have a value) | app 5/5, watch 5/5 (Health, Siri texts in French) | **yes** |
| Pawza | 1322/1331 (99.3%) | AppShortcuts 4/4; no widget catalog (widgets share the main one) | **none**: no InfoPlist catalog, camera and photo texts are English build settings | **yes** (permission prompts in English) |
| RightSplit | 498/499 (99.8%) | Widgets 376/376, Share 3/3, SplititKit 65/65 | InfoPlist 5/5 | **yes** |
| Shogiful | 3719/3721 (99.9%) | none | InfoPlist 0/2 (only display and bundle name) | **yes** |

Keys without `fr` are format-only or debug strings (`''`, `'%@'`, `'·'`, `'%lld'`, `'i'`, `'v'`, `'Floor'`, `'Layer'`, `'Reading'`, two Pawza UI-test fixtures). The real gaps are listed per app.

Cross-app flags for the whole batch:
- **Register is not uniform.** Mockly, Observa, Pawza and RightSplit are vous. Shogiful is tu. Check TRANSLATION.md section 13 (vous for the site) against the Shogiful UI, which will address players with tu.
- **"Best value" has three French values across the apps:** "Meilleure offre" (Observa, Pawza, Shogiful paywall), "Meilleur rapport qualité-prix" (Observa `Best Value`, RightSplit).
- **Lifetime tier:** the apps say "à vie" (Observa `Lifetime` → "À vie", Pawza, RightSplit, Shogiful), but the French App Store IAP names say "achat unique" (Observa, Pawza, RightSplit). Shogiful matches ("Premium à vie").
- **Name spacing:** the French store names put a space before the colon for Mockly, Observa, Shogiful ("Observa : VFC & Récupération") and none for Pawza and RightSplit ("Pawza: Carnet de Santé Animal"). Decide one rule for the site (French typography wants the space).

---

### 1. Mockly (`mockly`, source `AppScreenMaker/`, ID 6756589122, macOS)

### French coverage

- `Resources/Localizable.xcstrings`: 333 keys, 332 with `fr`, all state translated (99.7%). Only missing key: the empty string `''`. The catalog holds 10 languages: de, en, es-ES, es-MX, fr, ja, ko, pt-BR, tr, zh-Hans.
- `InfoPlist.xcstrings`: 4/4 in French (`CFBundleDisplayName` "Mockly", `CFBundleName` "Mockly", `Mockly Project` → "Projet Mockly", copyright → "Copyright © 2026. Tous droits réservés."). The old "ScreenFlow Studio" display name that the German glossary flagged (M1) is gone from this catalog now (it says Mockly in en and fr).
- No extensions, no Siri phrases, no widgets, no `.lproj` files.
- Register: vous (24 strings with vous/votre against 1 false hit, "Ton" = Tone). Both "Souhaitez-vous" and "Voulez-vous" appear; both are vous.
- **Verdict: app is in French: yes.**

Flags
- **M2 (same as German):** the app sells translation credit packs ("Packs de traduction", "Crédits de traduction") next to bring-your-own-key. The French store page shows no in-app purchases, so the packs may not be live. The site only says "your own key". Check before the French page says anything about packs.
- **M3:** the French store subtitle says "50 langues, un seul workflow". The site says 39 App Store locales in places. Pick one number.
- Anglicisms left in French UI: "workflow" (store subtitle), "Powered by Claude" → "Propulsé par Claude pour une localisation de captures de qualité."
- Mixed French words for the same thing: `Screenshot` is "capture d'écran" everywhere ("Captures générées"), good; `Upload` is "Téléverser" in the main button and "envoyée(s)" in the progress string (`%lld uploaded` → "%lld envoyée(s)", `%lld uploaded, %lld failed` → "%lld téléversée(s), %lld en échec").
- The app has no strings for "Templates", "Bulk Import", "Panorama", "3D device frame" or "Metal". The site's "device models" has no UI string; the closest are `Devices` / `Device Style` / `Model`.

### Glossary

| English term on site | English UI string (key) | French UI string (verbatim) | Note |
|---|---|---|---|
| Upload to App Store Connect | `Upload to App Store Connect` | Téléverser vers App Store Connect | button |
| App Store Connect credentials | `App Store Connect Credentials` | Identifiants App Store Connect | settings section; `API Credentials` → "Identifiants API"; `Delete Credentials` → "Supprimer les identifiants" |
| Issuer ID / Key ID / .p8 key | `Issuer ID` / `Key ID` / `Import .p8 File` | ID d'émetteur / ID de clé / Importer un fichier .p8 | |
| API key (bring your own) | `API Key` / `Own API Key` | Clé API / Clé API personnelle | |
| AI translation | `AI Translation` | Traduction par IA | feature name |
| AI Translate (button) | `AI Translate` | Traduire avec l'IA | |
| Translate All | `Translate All` | Tout traduire | |
| Bulk translations | `Bulk Translations` | Traductions groupées | |
| AI integration | `AI Integration` | Intégration IA | |
| Provider | `Provider` / `Default Provider` | Fournisseur / Fournisseur par défaut | OpenAI, Anthropic, Google are not in the catalog as strings |
| Localization panel | `Localizations` | Localisations | |
| Languages / locales | `Languages` / `Target Languages` / `Source Language` | Langues / Langues cibles / Langue source | the app says "langues", not "locales" |
| Add language | `Add Language` / `Add All (%lld)` | Ajouter une langue / Tout ajouter (%lld) | |
| Linked to source | `Linked to source` / `Changes follow %@` | Lié à la source / Les modifications suivent %@ | the site's "link-to-source switch" |
| Device models | `Devices` / `Device Style` / `Model` | Appareils / Style d'appareil / Modèle | |
| Artboard | `Artboard` / `Artboards` | Plan de travail / Plans de travail | |
| Export | `Export` / `Export %lld Artboards` | Exporter / Exporter %lld plans de travail | |
| Save images | `Save Images` | Enregistrer les images | |
| Text overlays / captions | `Text Block` / `Text Blocks` | Bloc de texte / Blocs de texte | the app's own word for captions |
| Copy Style | `Copy Style` | Copier le style | |
| Auto-apply screenshots | `Auto-apply screenshots to devices across all pages and languages.` | Applique automatiquement les captures d'écran aux appareils de toutes les pages et langues. | the app has no "Bulk Import" string |
| CSV import/export | `Import CSV` / `Export CSV` | Importer un CSV / Exporter en CSV | |
| Pages | `Pages` / `Page` | Pages / Page | |
| Layers | `Layers` | Calques | |
| Background | `Background` | Arrière-plan | |
| Gradient | `Gradient` | Dégradé | |
| Shadow | `Shadow` | Ombre | |
| Border / Corner radius | `Border` / `Corner Radius` | Bordure / Rayon des coins | |
| Camera / Lighting | `Camera` / `Lighting` | Caméra / Éclairage | |
| Perspective / Orthographic | `Perspective` / `Orthographic` | Perspective / Orthographique | |
| Rotation / Scale / Offset | `Rotation` / `Scale` / `Offset` | Rotation / Échelle / Décalage | |
| Device overflow | `Device Overflow` | Débordement d'appareil | |
| New Project | `New Project` | Nouveau projet | |
| macOS Keychain | `Your API key is stored in the macOS Keychain.…` | Votre clé API est stockée dans le trousseau macOS. | Keychain = "trousseau" |
| Translation packs (IAP) | `Translation Packs` / `Translation Credits` | Packs de traduction / Crédits de traduction | see M2 |
| Restore Purchases | `Restore Purchases` | Restaurer les achats | |
| Templates | no UI string | no UI string | |
| Percentage-based layout | no UI string | no UI string | |

Paid tier names: Mockly is a paid app (one-time), with no tiers. The only purchase UI is the translation-pack sheet: "Packs de traduction", "Acheter plus", "Restaurer les achats", "Packs ponctuels. Aucun abonnement. Conçu pour les développeurs." No free trial.

### French App Store listing (https://apps.apple.com/fr/app/id6756589122, read 2026-11-07)

- Name: **Mockly : Captures d'écran 3D** (differs from English "Mockly: Screenshot Maker"; straight apostrophe, space before the colon)
- Subtitle: **50 langues, un seul workflow** (translated; English "50 Languages, One Workflow")
- Category: **Outils de développement** (English "Developer Tools")
- Price: **14,99 €** (paid app; US $12.99). No in-app purchases listed.
- Langues: "Français et 8 de plus": Français, Allemand, Anglais, Chinois simplifié, Coréen, Espagnol, Japonais, Portugais, Turc
- Compatibility: "Nécessite macOS 14.0 ou version ultérieure." (Mac only)

---

### 2. Observa (`observa`, source `HealthLogger/`, ID 6757438990)

### French coverage

- Main `HealthLogger/Localizable.xcstrings`: 6693 keys, 6686 with a `fr` value, 6674 state translated (99.7%). 12 are state `needs_review` (all `insight_signal_*`, values present, e.g. `insight_signal_morning_hrv` → "VFC du matin"). 7 have no `fr`: `-- %@`, `%@`, `Floor`, `i`, plus format-only keys. 41 languages.
- Watch `ObservaWatch/Localizable.xcstrings`: 478/480 (missing `%@`, `v`). Widgets `ObservaWidgets/Localizable.xcstrings`: 404/406 (same two).
- `AppShortcuts.xcstrings`: 15 keys, all have a `fr` value, 10 translated and 5 `needs_review` (the Siri phrases "Log my … morning check-in", "Log water", "Should I train today", "What was my … sleep score", "What's my … readiness"). Values exist, so Siri works in French, but they are unreviewed.
- `InfoPlist.xcstrings` app 5/5 and watch 5/5 in French, including `NSHealthShareUsageDescription`, `NSHealthUpdateUsageDescription`, `NSSiriUsageDescription`.
- Register: **mixed, mostly vous.** About 1586 strings with vous/votre/vos against 25 with tu/ton/ta/ouvre. The tu strings are the Siri/voice answers and some empty states: "C'est fait — j'ai enregistré ta matinée comme %@.", "Je n'ai pas encore de score de sommeil — ouvre Observa pour synchroniser ta dernière nuit.", "Tu accumules environ %@ heures de dette de sommeil cette semaine.", "Une fois quelques boissons enregistrées, tu verras ici ton schéma quotidien…". Next to them: "Votre récupération est meilleure quand…".
- **Verdict: app is in French: yes** (all user-visible parts; 5 Siri phrases and 12 insight labels flagged needs_review).

**How the French UI labels HRV:** **"VFC"** (keys `HRV`, `metric_label_hrv` → "VFC"). The long form is **"Variabilité de la fréquence cardiaque"** (`Heart Rate Variability`). There is no short "VFC (SDNN)" label in the app. SDNN appears only in explanatory sentences ("L'écart type des intervalles NN (SDNN) reflète la variabilité globale de votre fréquence cardiaque issue de toutes les sources…"). RMSSD and pNN50 stay as they are ("RMSSD et pNN50 dérivés de l'ECG"). For the site: HRV is SDNN; write "VFC (SDNN)". Use RMSSD/pNN50 only for the ECG path. Note the app still uses the English acronym in 10 strings ("HRV") and "VFC" in about 190.

Flags
- **O1 (tier name):** the French app says **Premium** everywhere (paywall, Watch "Premium requis", widgets "Nécessite Observa Premium", Siri/Watch "Observa Premium le débloque"), and the store IAPs are "Premium annuel/mensuel/achat unique". No "Pro" tier in French. The English site says "Pro". The French page needs "Premium".
- **O2 (readiness):** `Readiness` → "Disponibilité" (81 strings, tab/score/Siri/widgets), but running text says "préparation" in 39 strings ("fait baisser votre score de préparation", "préparation supérieure à 70"). The French store subtitle avoids the word ("Sommeil, Cycle, Coach & Score"). Pick "disponibilité" (the label the user sees on the score).
- **O3 (baseline):** `Baseline` → "Référence" (181 strings; "Votre référence"), but "ligne de base" appears in 11 and the English "Baseline" in 3.
- **O4 (resting heart rate):** "Fréquence cardiaque au repos" (38), "FC au repos" (50) and "FCR" (24, the `RHR` key).
- **O5 (weekly reflection):** `Weekly Reflection` → "Bilan hebdomadaire", but `Unlock Weekly Reflections` → "Débloquez les réflexions hebdomadaires" and one other string says "réflexion". Pick "bilan hebdomadaire".
- **O6 (check-in):** `Morning Check-In` → "Point du matin"; the Watch complication says "Bilan" / "Votre bilan du matin, à portée de doigt." Same thing, two words ("point" vs "bilan"), and "bilan" is also used for the weekly reflection.
- **O7 (patterns):** `Patterns` tab → "Schémas", lowercase `patterns` → "tendances".
- **O8 (English left in a button):** `Unlock Lifetime Access` → "Débloquez Lifetime Access" (English kept). The onboarding paywall uses "Débloquer l'accès à vie".
- **O9 (Best value):** `Best Value` → "Meilleur rapport qualité-prix", `Best value` → "Meilleure offre", `pricing_label_yearly` → "Annuel (meilleure offre)".
- `ECG` → "ECG" (correct in French, unlike the German "EKG").
- Cycle tracking: the French store subtitle says "Cycle". The English site page does not cover cycle tracking. Fact gap to check (same as German).
- The FR storefront lists a tip IAP "Soutenir le développeur" (1,00 €).

### Glossary

| English term on site | English UI string (key) | French UI string (verbatim) | Note |
|---|---|---|---|
| Tab: Sleep | `Sleep` | Sommeil | tab bar: Sleep, Recovery, Heart, Patterns, More |
| Tab: Recovery | `Recovery` | Récupération | |
| Tab: Heart | `Heart` | Cœur | |
| Tab: Patterns | `Patterns` | Schémas | O7 |
| Tab: More | `More` | Plus | |
| HRV | `HRV` / `metric_label_hrv` | VFC | no "(SDNN)" label, see note above |
| Heart rate variability | `Heart Rate Variability` | Variabilité de la fréquence cardiaque | |
| ECG-derived RMSSD & pNN50 | `ECG-derived RMSSD & pNN50` | RMSSD et pNN50 dérivés de l'ECG | ECG path only |
| ECG | `ECG` / `ECG Recording` / `ECG Analysis` | ECG / Enregistrement ECG / Analyse ECG | |
| Autonomic balance | `Autonomic Balance` | Équilibre autonome | |
| Sinus rhythm | `Sinus Rhythm` | Rythme sinusal | |
| Readiness | `Readiness` | Disponibilité | O2 |
| Readiness score | `Readiness Score` | Score de disponibilité | |
| Sleep Score | `Sleep Score` | Score de sommeil | |
| Recovery score | `recovery score` | score de récupération | `insight_signal_recovery_score` → "Score de récupération" |
| Training call | `Should I train today?` | Devrais-je m'entraîner aujourd'hui ? | `${applicationName} training call` (Siri) → "Conseil d'entraînement ${applicationName}" |
| Resting heart rate | `Resting Heart Rate` / `RHR` | Fréquence cardiaque au repos / FCR | O4 |
| Sleep efficiency | `Sleep Efficiency` | Efficacité du sommeil | |
| Sleep stages | `Sleep Stages` | Stades de sommeil | |
| Deep sleep / REM | `Deep Sleep` / `REM Sleep` | Sommeil profond / Sommeil paradoxal | |
| Sleep debt | `Sleep Debt` | Dette de sommeil | |
| Heart-rate dip | `Nocturnal Dip` | Baisse nocturne | |
| Heart rate recovery | `Heart Rate Recovery` | Récupération cardiaque | |
| Stress | `Stress` | Stress | |
| Today's Plan | `Today's Plan` | Plan du jour | |
| Functional Age | `Functional Age` (in `Unlock Functional Age`) | âge fonctionnel (`Unlock Functional Age` → "Débloquer l'âge fonctionnel") | |
| Chronotype | `Chronotype Analysis` | Analyse du chronotype | `chronotype_intermediate` → "Chronotype intermédiaire" |
| Training load | `Training Load` | Charge d'entraînement | |
| Strain | `Strain` | Effort | the Siri/insight signal `insight_signal_strain` → "Contrainte d'entraînement" (needs_review) |
| Workouts | `Workouts` | Entraînements | |
| Energy | `Energy` / `Active Energy` | Énergie / Énergie active | |
| Personal baseline | `Baseline` / `Your baseline` | Référence / Votre référence | O3 |
| Confidence | `Confidence` | Confiance | |
| Patterns / correlations | `Correlation strength (r)` | Force de corrélation (r) | |
| Insight cards | `Daily insights` / `Insights` | Analyses quotidiennes / Analyses | the app uses "analyses", not "aperçus" |
| Weekly reflection | `Weekly Reflection` | Bilan hebdomadaire | O5 |
| Long-term trends | `Long-Term Trends` | Tendances à long terme | |
| Morning check-in | `Morning Check-In` | Point du matin | O6 |
| Hydration | `Hydration` | Hydratation | |
| Apple Watch complications | `watch.complication.*.title` | Bilan / Hydratation / Mesure | descriptions: "Votre bilan du matin, à portée de doigt." |
| Premium tier | `Premium` / `Upgrade to Premium` / `Unlock Premium` | Premium / Passer à Premium / Débloquer Premium | O1 |
| Monthly / Yearly / Lifetime | `Monthly` / `Yearly` / `Lifetime` | Mensuel / Annuel / À vie | |
| Unlock lifetime | `Unlock Lifetime Access` / `onboarding_paywall_lifetime_cta` | Débloquez Lifetime Access / Débloquer l'accès à vie | O8 |
| Start free trial | `Start Free Trial` / `Start %@ Free Trial` | Démarrer l'essai gratuit / Démarrer l'essai gratuit de %@ | |
| Start plan | `Start Yearly Plan` | Démarrer l'abonnement annuel | |
| Restore Purchases | `Restore Purchases` | Restaurer les achats | |
| Free | `Free` | Gratuit | |

Paid tier names as the French UI shows them: **Premium** (Watch and widgets too), **Mensuel / Annuel / À vie**, `Best Value` variants (O9), "Débloquer Premium", "Passer à Premium", "Restaurer les achats", "Démarrer l'essai gratuit". Premium is unlocked for the first 7 days ("Toutes les fonctionnalités Premium sont débloquées pendant vos 7 premiers jours.").

### French App Store listing (https://apps.apple.com/fr/app/id6757438990, read 2026-11-07)

- Name: **Observa : VFC & Récupération** (differs from English "Observa: HRV & Recovery Score"; space before colon)
- Subtitle: **Sommeil, Cycle, Coach & Score** (translated; English "Readiness, Sleep & Cycle Coach")
- Category: **Forme et santé** (English "Health & Fitness")
- Price: Gratuit. In-app purchases as shown: Premium annuel **24,99 €**, Premium mensuel **3,99 €**, Premium achat unique **59,99 €**, Soutenir le développeur **1,00 €**
- Langues: "Français et 33 de plus"
- Compatibility: iOS 17.6, iPadOS 17.6, macOS 14.6 (M1), visionOS 1.3, watchOS 10.0

---

### 3. Pawza (`pawza`, source `PetCare/`, ID 6773507068)

### French coverage

- `PetCare/Localizable.xcstrings`: 1331 keys, 1322 with `fr`, all translated (99.3%). Missing: format-only keys (`''`, `·`, `%@`, `%@ · %@`, `%@%@`, `%lld`, `%lld%%`) and two debug strings (`Fixture (UI test)`, `Inject a synthesized vet-record image`). 50 languages. The widget target shares this catalog (no catalog of its own).
- `AppShortcuts.xcstrings`: 4/4, e.g. "Enregistrer un soin dans ${applicationName}", "Enregistrer l'humeur de ${pet} dans ${applicationName}".
- **No `InfoPlist.xcstrings`.** The camera and photo-library permission texts are `INFOPLIST_KEY_NSCameraUsageDescription` / `…NSPhotoLibraryUsageDescription` build settings in English only ("Pawza uses your camera to scan vet documents and take photos of your pets."). French users see the permission prompts in English. The project's known regions include `fr` and `fr-CA`.
- Register: **mixed.** About 93 strings with vous/votre against 32 with tu/ton/ta/imperatives: "Ajoute d'abord une fiche de santé pour %@, puis tu pourras…", "Importe les documents de ton animal", "Création de ton PDF…", "Impossible d'ouvrir ta photothèque", "réinstalle Pawza", next to "Ajoutez d'abord un animal", "Un PDF de votre vétérinaire", "Débloquez un nombre illimité…". Even one pair of sentences ("Nous n'avons trouvé aucun achat Pawza Pro antérieur sur ton identifiant Apple." / "Votre achat Pawza Pro est de nouveau actif.") mixes both.
- **Verdict: app is in French: yes** (permission prompts and display name in English from build settings).

Flags
- **P1:** permission texts not localized (see above).
- **P2 (scan):** "scanner" (4 strings, e.g. "Scanner un document vétérinaire", "pour scanner un carnet de vaccination") and "numériser" (5 strings plus "numérisations de documents", 10 in all), plus the English noun "scans" ("Animaux et scans illimités"). The site page headline verb is "Scan a vet document", which the app renders "Scanner un document vétérinaire" while the button `Scan` → "Numériser".
- **P3 (records):** `Records` → "Fiches" (also "fiche de santé"), but `vaccinations` lowercase → "vaccins" and `Vaccinations` → "Vaccinations"; `Vaccines` → "Vaccins".
- **P4 (accounts):** "Les comptes gratuits suivent un seul animal." The app has no accounts (same as German). Use "version gratuite" on the site.
- `Start 7-day free trial` → "Commencer l'essai gratuit de 7 jours", while Observa and Shogiful say "Démarrer l'essai gratuit".

### Glossary

| English term on site | English UI string (key) | French UI string (verbatim) | Note |
|---|---|---|---|
| Tab: Pets | `Pets` | Animaux | tabs: Pets, Reminders, Settings |
| Tab: Reminders | `Reminders` | Rappels | |
| Tab: Settings | `Settings` | Réglages | |
| Pet / Add pet | `Pet` / `Add Pet` | Animal / Ajouter un animal | |
| Health records | `Records` | Fiches | "fiche de santé", P3 |
| Vaccinations | `Vaccinations` / `Vaccines` | Vaccinations / Vaccins | |
| Medications | `Medications` / `Medication` | Médicaments / Médicament | |
| Doses | `Doses` | Doses | |
| Vet visits | `Vet visits` | Visites vétérinaires | |
| Vet | `Vet` | Vétérinaire | `Emergency vet` → "Vétérinaire d'urgence" |
| Weight / weight alerts | `Weight` / `Weight trend alerts` | Poids / Alertes de tendance du poids | |
| Symptoms | `Symptoms` | Symptômes | `Log Symptom` → "Noter un symptôme" |
| Care log | `Care log` / `Log care` | Journal de soins / Enregistrer un soin | |
| Walks | `Walks` | Promenades | |
| Mood | `Mood` | Humeur | |
| Document scanning | `Scan a vet document` / `Scan` | Scanner un document vétérinaire / Numériser | P2 |
| Import past records | `Import past records` | Importer des fiches antérieures | |
| AI auto-fill | `Unlock AI auto-fill` | Débloquer le remplissage automatique par IA | |
| AI summaries | `AI Summaries` / `AI summaries for every record` | Résumés par IA / Résumés par IA pour chaque fiche | |
| Apple Intelligence | `Apple Intelligence summary` / `Fill with Apple Intelligence` | Résumé Apple Intelligence / Remplir avec Apple Intelligence | |
| Vet-visit PDF | `Vet Visit PDF` / `Vet visit PDF generator` | PDF de visite vétérinaire / Générateur de PDF de visite vétérinaire | |
| Since last vet visit | `Since last vet visit` | Depuis la dernière visite chez le vétérinaire | |
| Emergency Card | `Emergency Card` | Carte d'urgence | `Emergency Info` → "Infos d'urgence" |
| Lost Pet Kit | `Lost Pet Kit` / `Lost Pet Poster` | Kit animal perdu / Affiche animal perdu | |
| Sitter Pack | `Sitter Pack` | Fiche de garde | |
| Photo gallery | `Unlimited photo gallery` | Galerie photo illimitée | |
| Unlimited pets and scans | `Unlimited pets and scans` | Animaux et scans illimités | |
| Free / Pro | `Free` / `Pro` / `Pawza Pro` | Gratuit / Pro / Pawza Pro | |
| Unlock Pro | `Unlock Pawza Pro` / `Upgrade to Pawza Pro` | Débloquer Pawza Pro / Passer à Pawza Pro | |
| Monthly / Yearly / Lifetime | `Monthly` / `Yearly` / `Lifetime` | Mensuel / Annuel / À vie | `Pro (Lifetime)` → "Pro (à vie)", `Buy Lifetime — %@` → "Acheter à vie — %@" |
| 7-day free trial | `Start 7-day free trial` | Commencer l'essai gratuit de 7 jours | |
| Subscribe | `Subscribe` | S'abonner | |
| Best value | `Best value` | Meilleure offre | |
| Due / Upcoming | `Due` / `Upcoming` | Échéance / À venir | |
| iCloud sync | `iCloud Sync: up to date.` | Synchronisation iCloud : à jour. | |
| Syncing with iCloud | `Syncing with iCloud...` | Synchronisation avec iCloud… | correct progress form (the German version reads as a command) |
| Restore Purchases | `Restore Purchases` | Restaurer les achats | |

Paid tier names as the French UI shows them: **Pawza Pro** (also "Pro"), labels **Mensuel / Annuel / À vie**, "Commencer l'essai gratuit de 7 jours", "Restaurer les achats", "S'abonner". Paywall legal lines: "Mensuel : essai gratuit de 7 jours, puis %@ par mois, renouvellement automatique chaque mois." and "À vie : achat unique, sans renouvellement automatique."

### French App Store listing (https://apps.apple.com/fr/app/id6773507068, read 2026-11-07)

- Name: **Pawza: Carnet de Santé Animal** (differs from English "Pawza: Pet Health & Records"; no space before the colon; capitalised "Santé Animal")
- Subtitle: **Vaccins & rappels vétérinaire** (translated; English "Vaccine Tracker & Reminders"; note "rappels vétérinaire" singular)
- Category: **Style de vie** (English "Lifestyle")
- Price: Gratuit. In-app purchases as shown: Pawza Pro annuel **22,99 €**, Pawza Pro mensuel **2,99 €**, Pawza Pro achat unique **44,99 €**
- Langues: "Français et 43 de plus"
- Compatibility: iOS 17.6 (iPhone, iPad), macOS 14.6 (M1), visionOS 1.3

---

### 4. RightSplit (`rightsplit`, source `splitit/`, ID 6757268612)

### French coverage

- Main `splitit/Localizable.xcstrings`: 499 keys, 498 with `fr`, all translated (99.8%). Only missing: `''`. 40 languages.
- Widgets `splititWidgets`: 376/376. Share extension `splititShare`: 3/3. SplititKit package (`Sources/SplititKit/Resources`): 65/65. (A stale build-folder copy shows 52/56; ignore it.)
- `InfoPlist.xcstrings`: 5/5 in French (camera: "RightSplit utilise la caméra pour scanner les reçus de restaurant et partager l'addition."; contacts; photo-library add).
- Register: **mostly vous** (28 vous against 4 tu). The tu strings: "Salut %1$@ ! Ta part de l'addition chez %2$@ est de %3$@." (the message sent to friends), "Si tu as une minute, dis-nous ce qui manque.", "Tape rapide — ta réponse honnête façonne l'app." Duplicate English keys translated differently: "A day after you start tracking…" appears as "RightSplit vous rappelle…" in two variants.
- **Verdict: app is in French: yes.**

Flags
- **R1 (split verb):** the app mixes "Diviser" (`Split by items` → "Diviser par articles"), "Partager"/"partage" (33 strings with "partage", 11 "partager": `Split Receipt` → "Partager le reçu", `Equal splits & tip` → "Partage égal et pourboire", `Unlimited split history` → "Historique de partages illimité", `Start splitting` → "Commencer à partager") and "répartir" (2). "Partager" also means "share" (`Share` → "Partager", `Share RightSplit` → "Partager RightSplit"), so "partager" is ambiguous. The store subtitle uses "Partager facture & dépenses".
- **R2 (receipt/bill):** `Receipt` → "Reçu" (32), `Bill` → "Addition" (12), "facture" (2), "note" (2). The store name says "Addition". Site: keep "reçu" for the scanned paper and "addition" for the bill.
- **R3 (Best value):** `Best value` → "Meilleur rapport qualité-prix" (Observa and Pawza say "Meilleure offre").
- **R4 (tax):** `Tax` → "Taxe". France has TVA included in prices and no add-on sales tax, so "taxe" reads foreign. Check the French site copy ("taxe" vs "TVA" vs "service").
- **R5 (spaces):** `Spaces` → "Espaces" (`New space` → "Nouvel espace"), consistent. `Trips` → "Voyages".
- `Send feedback` → "Envoyer un commentaire" and `Send Feedback` → "Envoyer un avis" (two values for the same action).
- `Everyone's settled — no transfers needed.` → "Tout est réglé — aucun virement nécessaire." (em dash in UI, do not copy to site).
- `Text / WhatsApp share` → "Partage SMS / WhatsApp" (the site says iMessage/WhatsApp).
- `Pro+ restored successfully!` → "Pro+ restauré avec succès !" (one line of English-style exclamation).

### Glossary

| English term on site | English UI string (key) | French UI string (verbatim) | Note |
|---|---|---|---|
| Scan receipt | `Scan Receipt` | Scanner le reçu | R2 |
| Receipts | `Receipts` / `Receipt` | Reçus / Reçu | |
| Receipt language | `Receipt Language` | Langue du reçu | |
| Item-level splits | `Split by items` | Diviser par articles | R1 |
| Shared dishes | `Shared dishes` / `Add shared item` | Plats partagés / Ajouter un article partagé | |
| Equal splitting | `Equal splits & tip` | Partage égal et pourboire | R1 |
| Per person | `Per person` / `Adjust per person` | Par personne / Ajuster par personne | |
| Tip | `Tip` / `Tip included` | Pourboire / Pourboire inclus | |
| Tax | `Tax` | Taxe | R4 |
| Subtotal / Total | `Subtotal` / `Total` | Sous-total / Total | |
| Fair rounding | `Round fairly` | Arrondir équitablement | |
| Send totals / payment requests | `Send Payment Requests` | Envoyer les demandes de paiement | |
| Text / WhatsApp share | `Text / WhatsApp share` | Partage SMS / WhatsApp | |
| Paid | `Paid` | Payé | |
| Spaces | `Spaces` / `New space` | Espaces / Nouvel espace | R5 |
| Trips | `Trips` / `Trips & shared expenses` | Voyages / Voyages et dépenses partagées | |
| Balances / settle-up | `Balance` / `Settlement` / `Settle in` | Solde / Règlement / Régler en | |
| Split history | `History` / `Unlimited split history` | Historique / Historique de partages illimité | |
| Templates | `Templates` / `Split template` | Modèles / Modèle de partage | |
| People | `People` | Personnes | |
| Currency | `Currency` | Devise | |
| Free | `Free` | Gratuit | |
| Pro+ | `Pro+` / `Unlock Pro+` / `Upgrade to Pro+` | Pro+ / Débloquer Pro+ / Passer à Pro+ | |
| Pro+ yearly | `Pro+ Yearly` | Pro+ Annuel | |
| Pro+ lifetime | `Pro+ Lifetime` / `Unlock Pro+ Lifetime` | Pro+ à vie / Débloquer Pro+ à vie | `Unlock Pro+ — Pay once` → "Débloquer Pro+ — Paiement unique" |
| Free trial | `%lld-day free trial` | %lld jours d’essai gratuit | uses curly apostrophe U+2019 |
| Best value | `Best value` | Meilleur rapport qualité-prix | R3 |
| Restore Purchases | `Restore Purchases` | Restaurer les achats | |

Paid tier names as the French UI shows them: **Pro+** (no plain "Pro"), **Pro+ Annuel**, **Pro+ à vie**, "Débloquer Pro+", "Continuer avec Pro+", "Restaurer les achats". Auto-renew line: "Se renouvelle automatiquement chaque année jusqu'à résiliation."

### French App Store listing (https://apps.apple.com/fr/app/id6757268612, read 2026-11-07)

- Name: **RightSplit: Addition Pourboire** (differs from English "RightSplit: Bill Splitter Tip"; no space before the colon)
- Subtitle: **Partager facture & dépenses** (translated; English "Scan & share group expenses")
- Category: **Utilitaires** (English "Utilities")
- Price: Gratuit. In-app purchases as shown: RightSplit Pro+ Achat unique **8,99 €**, RightSplit Pro+ annuel **4,99 €**
- Langues: "Français et 33 de plus"
- Compatibility: iOS 17.0, macOS 14.0 (M1), visionOS 1.0 (no iPad listed)

---

### 5. Shogiful (`shogiful`, source `shogi/`, ID 6761656926)

### French coverage

- `Localization/Localizable.xcstrings`: 3721 keys, 3719 with `fr`, all translated (99.9%). Missing: `''` and `dashboard.accuracy %lld`. 39 languages. Most keys are semantic (`tab.play`, `paywall.plan.monthly`), so look up by key, not English text.
- `InfoPlist.xcstrings`: 0/2 (only `CFBundleDisplayName` "Shogiful" and `CFBundleName` "shogi", no translation needed). The app requests no permissions.
- No extensions or Siri phrases.
- Register: **tu.** About 699 strings with tu/ton/ta/imperatives ("Va plus loin", "Libère tout ton potentiel", "Joue une partie, puis reviens ici", "Fais un court test pour fixer ton rang kyu/dan") against 4 with vous. Rare exceptions: `error.engineNotReady` → "Le moteur n’est pas prêt. Veuillez patienter." (vous form).
- **Verdict: app is in French: yes.** The only decision is register (tu in the app, vous on the site).

Flags
- **S1 (opponents):** the code has 8 `OpponentTier` levels: Novice, Débutant, Occasionnel, Joueur de club, Intermédiaire, Avancé, Expert, Maître. The site says 40 engine opponents (the German glossary flagged 10 AI opponents across 4 tiers); check the count against the blueprint.
- **S2 (tsume spelling):** "tsumé" with an accent in most strings ("Parcours tsumé", "Tsumé manqué", "Règles du tsumé"), but "tsume" without accent in achievements ("Accro au tsume", "Maître du tsume"). `Tsume-Shogi` is "Tsumé : le mat forcé". Pick one for the site.
- **S3 (joseki spelling):** "joseki" (lessons, "Écart au joseki", "Élève du Joseki") vs "jōseki" with macron (`mistakeType.josekiInaccuracy` → "Imprécision de jōseki", `module.josekiLab.title` → "Labo de jōseki").
- **S4 (positioning):** `skill.positioning` → "Positionnement", but the achievement `gc.achievement.haichi.locked` says "Placement" and calibration titles say "Position".
- **S5 (rating):** `Rating` → "Classement" (also `Estimated Rating` → "Classement estimé"). "Classement" also means ranking. Kyu/dan is "rang" ("Ton rang").
- **S6 (International):** the "Western" piece set is called "International" (`settings.pieceSet.western`, `onboarding.style.international`). Onboarding describes it as "Kanji avec flèches de déplacement". The settings label is "Style de pièces" (`settings.pieceSet`, `settings.pieceStyle`).
- **S7 (drop = parachutage):** drops are "parachutage" throughout ("Exercices de parachutage", "Erreur de parachutage", "Parachutage éclair").
- Dashboard tab is "Accueil" (key `tab.dashboard`, English "Dashboard").
- The app has no "skill radar" string. It shows `onboarding.outcomes.radar.label` → "Ton profil de compétences".
- Free-trial text appears via `paywall.startTrial` → "Démarrer l’essai gratuit". Apostrophes in this catalog are curly (U+2019), in Observa mostly straight.

### Glossary

| English term on site | English UI string (key) | French UI string (verbatim) | Note |
|---|---|---|---|
| Tab: Dashboard | `Dashboard` (`tab.dashboard`) | Accueil | |
| Tab: Play | `Play` (`tab.play`) | Jouer | |
| Tab: Analysis | `Analysis` (`tab.analysis`) | Analyse | |
| Tab: Training | `Training` (`tab.training`) | Entraînement | |
| Tab: Progress | `Progress` (`tab.progress`) | Progression | |
| Premium | `Shogiful Premium` (`settings.premium.name`) | Shogiful Premium | |
| Premium · Monthly | `Premium Monthly` (`paywall.plan.monthly`) | Premium mensuel | |
| Premium · Annual | `Premium Yearly` (`paywall.plan.yearly`) | Premium annuel | |
| Lifetime | `Premium Lifetime` (`paywall.plan.lifetime`) | Premium à vie | matches the store IAP name |
| Upgrade | `Upgrade to Premium` (`settings.premium.upgrade`) | Passer à Premium | `Premium Active` → "Premium actif", `Free Plan` → "Forfait gratuit" |
| Family Sharing | `Premium via Family Sharing` | Premium via le Partage familial | |
| Best value | `BEST VALUE` (`paywall.bestValue`) | MEILLEURE OFFRE | |
| Start free trial | `Start Free Trial` (`paywall.startTrial`) | Démarrer l’essai gratuit | |
| Tsume-shogi | `Tsume-Shogi: Forced Checkmate` | Tsumé : le mat forcé | S2 |
| Tsume Trail | `Tsume Trail` (`module.tsumeTrail.title`) | Parcours tsumé | |
| Drop Drills | `Drop Drills` (`module.dropDrills.title`) | Exercices de parachutage | S7 |
| Castle Atelier | `Castle Atelier` (`module.castleAtelier.title`) | Atelier des châteaux | |
| Joseki Lab | `Joseki Lab` (`module.josekiLab.title`) | Labo de jōseki | S3 |
| Lessons | `Lessons` (`hub.lessons.title`) | Leçons | |
| Handicap play | `Handicap` (`kif.import.preview.handicap`) | Handicap | `komaochi.*`: "Handicap fou", "Handicap quatre pièces" |
| Game review | `Game Review` (`analysis.review.title`) | Revue de partie | `Review Game` → "Revoir la partie" |
| Deep analysis | `Go deeper` (`paywall.hero.deepAnalysis.title`) | Va plus loin | the app has no "Deep Analysis" label |
| Engine | `YaneuraOu is evaluating every move...` | YaneuraOu évalue chaque coup… | `Engine ready` → "Moteur prêt" |
| Western / kanji piece sets | `International` / `Traditional (Kanji)` | International / Traditionnel (kanji) | S6 |
| Piece style setting | `Piece Style` (`settings.pieceSet`) | Style de pièces | |
| KIF import | `Import KIF` / `Copy KIF` | Importer un KIF / Copier le KIF | `Share KIF` → "Partager le KIF" |
| In-game coach | `In-game Coach` | Coach en partie | `Coach's tip` → "Conseil du coach", `Unlimited Coach` → "Coach illimité" |
| Today's training | `Today's Training` | Entraînement du jour | |
| Train weaknesses | `Train These Weaknesses` | Travailler ces faiblesses | |
| Estimated rating | `Estimated Rating` | Classement estimé | S5 |
| Accuracy trend | `Accuracy Trend` | Tendance de précision | |
| Skill profile | `Your skill profile` | Ton profil de compétences | no "radar" string |
| Five skills | `Tactics` / `Defense` / `Positioning` / `Endgame` / `Openings` | Tactique / Défense / Positionnement / Finale / Ouvertures | S4 |
| Blunder / Mistake / Inaccuracy | `Blunder` / `Mistake` / `Inaccuracy` | Gaffe / Erreur / Imprécision | |
| Drop mistake | `Drop Mistake` | Erreur de parachutage | |
| Castle weakness | `Castle Weakness` | Faiblesse du château | |
| Hanging piece | `Hanging Piece` | Pièce en prise | |
| Missed fork | `Missed Fork` | Fourchette manquée | |
| Missed tsume | `Missed Tsume` | Tsumé manqué | |
| Passive move | `Passive move — tempo lost` | Coup passif — tempo perdu | |
| Opponent tiers | `Novice`…`Master` (`opponentTier.*`) | Novice, Débutant, Occasionnel, Joueur de club, Intermédiaire, Avancé, Expert, Maître | S1 |
| Kyu / Dan | `Kyu / Dan ladder` | Échelle kyu/dan | `Your rank` → "Ton rang" |
| Resign | `Resign` | Abandonner | |
| Restore Purchases | `Restore Purchases` (`paywall.restore`) | Restaurer les achats | |

Paid tier names as the French UI shows them: **Shogiful Premium** with plans **Premium mensuel / Premium annuel / Premium à vie**, "MEILLEURE OFFRE", "Démarrer l’essai gratuit", "Restaurer les achats", "Gérer l’abonnement". Lifetime note: "Un achat unique — il n’y a rien à renouveler ni à gérer." Trial note: "…, puis renouvellement automatique. Annulable à tout moment."

### French App Store listing (https://apps.apple.com/fr/app/id6761656926, read 2026-11-07)

- Name: **Shogiful : Échecs japonais** (differs from English "Shogiful Learn & Analyze Shogi"; space before the colon)
- Subtitle: **Shogi : tactique et analyse IA** (translated; English "Japanese Chess Tactics Trainer")
- Category: **Jeux de société** (English "Board")
- Price: Gratuit. In-app purchases as shown: Premium annuel **9,99 €**, Premium mensuel **1,99 €**, Premium à vie **22,99 €**, Soutien **5,99 €**, Énorme soutien **9,99 €**, Un café **1,99 €**
- Langues: "Français et 32 de plus"
- Compatibility: iOS 18.0, iPadOS 18.0, macOS 15.0 (M1), visionOS 2.0


## French glossary, batch 4: soon, tare, taskful-day, wanderwiki, xiangqiful, clippet

Method note. Extracted 2026-11-07, read-only, from each app's string catalogs under `~/Downloads/<source>/` (`.xcstrings` is JSON; I counted keys with `shouldTranslate` not false, and a key counts as French only if `localizations.fr.stringUnit.state == "translated"` or it has `fr` plural variations). French values are copied verbatim from the catalogs. No app has `.lproj` folders or JSON localizations; every catalog is `.xcstrings`. The tu/vous counts are strings whose French value contains a pronoun or possessive of that register (`tu/ton/ta/tes/toi` versus `vous/votre/vos`); they undercount imperatives but show the split. The French App Store pages were fetched on 2026-11-07 with curl (Safari User-Agent, `Accept-Language: fr-FR`), compared with the US pages, and read from the raw HTML (prices carry U+00A0 before €). Clippet returned HTTP 404 on both the fr and us storefronts (not released), so its listing section uses the French listing text prepared in `~/Downloads/clipboard/marketing/aso/` (labelled as unpublished). Prices are reference only; the site prints prices from its catalog.

Storefront page title for each app also begins with the app name followed by the French subtitle in the page body; the owner's personal name appears on the store pages and is deliberately not copied.

Cross-app summary:
- All five released apps are fully in French (100 % in the main catalogs). Only stray non-user-facing keys are missing.
- Register is NOT uniform. Xiangqiful speaks **tu** (376 strings vs 2 with vous). WanderWiki, Clippet, Tare and all permission prompts and widget descriptions speak **vous**. Soon. and Taskful Day mix both inside the same catalog. TRANSLATION.md section 13 says vous for the site, so the app quotes on the site need care wherever a tu string is quoted.
- "Lifetime" is rendered four ways: Soon./WanderWiki/Xiangqiful/Clippet "À vie", Taskful Day "Accès définitif" (plan label) and "Pro à vie" (status).
- "Restore purchases" is "Restaurer les achats" everywhere (consistent).
- "Settings" is "Réglages" everywhere (iOS term); WanderWiki's settings tab key `settings` is also "Réglages".

---

### 1. Soon. (`soon`, source `countdown/`, ID 6757280643)

### French coverage
| Catalog | keys | `fr` translated | % |
|---|---|---|---|
| countdown/Localizable.xcstrings (main app, includes paywall) | 741 | 741 | 100 % |
| countdown/AppShortcuts.xcstrings (Siri and Spotlight phrases) | 13 | 13 | 100 % |
| countdown/InfoPlist.xcstrings | 6 | 5 | 83 % (only the stray key `Soon` is missing; display name, calendar and location permission texts are in French) |
| CountdownWidgets/Localizable.xcstrings | 184 | 182 | 98.9 % (missing only the format strings `%@ ` and `%@ %@`) |

Not in French: nothing user-visible. Widget gallery names stay English by design (`Soon · Ring`, `Soon · Timeline`, `Soon · StandBy`, `Soon · Streak`, `Soon · Hero`, `Soon · Dots`, `Soon · Year` and the rest of the 20 `Soon · …` names). **Verdict: app is in French: yes** (mirrors the German result).

### Glossary
| English term on site | English UI string (key) | French UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Home tab | `Home` | Accueil | |
| Plan tab | `Plan` | Planifier | |
| Search tab | `Search` | Recherche | |
| Profile tab | `Profile` | Profil | |
| Plan Mode | `Plan mode reminders` | Rappels du mode planification | only UI string naming the mode, so the French name is **mode planification**. No standalone "Plan Mode" label |
| Premium | `Premium` | Premium | `Go Premium` → "Passer Premium" |
| Free | `Free` | Gratuit | |
| Monthly / Annual | `Monthly` / `Yearly` | Mensuel / Annuel | app says "Yearly", not "Annual" |
| Lifetime | `Lifetime` | À vie | also `One-time purchase` → "Achat unique". The store IAP is "Premium achat unique" |
| 7-day free trial | `1 week free` / `Free trial` | 1 semaine gratuite / Essai gratuit | |
| Restore purchases | `Restore Purchases` | Restaurer les achats | |
| Countdown | `Countdown` | Compte à rebours | |
| Event / moment | `Event` / `Moment` / `Moments` | Moment / Moment / Moments | FLAG: the key `Event` is also "Moment", so French loses the word "événement" in the UI (it appears only in some descriptions, e.g. "Convertir des événements du calendrier en comptes à rebours") |
| Memories | `Memories` / `Memory` | Souvenirs / Souvenir | no clash with Reminders in French |
| Reminders / event notifications | `Reminders` | Rappels | |
| Reflection mode | `Notes` | Notes | no UI string says "Reflection" |
| Daily notes | `Personalized daily notes` / `Weather & daily notes` | Notes quotidiennes personnalisées / Météo et pensées du jour | FLAG: the second says "pensées du jour" ("thoughts of the day"), the first "notes quotidiennes" |
| Weather | `Weather` / `Weather forecast` / `Smart weather forecast` | Météo / Prévisions météo / Prévisions météo intelligentes | attribution: "Données météo fournies par Apple Météo" |
| Calendar import | `Import from your calendar` / `Turn calendar events into countdowns` | Importer depuis votre calendrier / Convertir des événements du calendrier en comptes à rebours | vous |
| Recurring events | `Recurring countdowns` / `Repeat` | Comptes à rebours récurrents / Répéter | |
| Natural language search | `Search` | Recherche | example hint: "“anniversaires cette année” — fenêtres temporelles naturelles" |
| Timeline / checklist | `Timeline` / `Checklist` | Chronologie / Liste | FLAG: Checklist is only "Liste" |
| Themes | `Theme` / `All themes unlocked` | Thème / Tous les thèmes débloqués | theme names are not localized; no `Sunrise`/`Ocean`/`Forest` key exists in the main catalog |
| Final Countdown | `Final Countdown` | Compte à rebours final | |
| Widget styles | `Progress Rings`, `TIMELINE` | Anneaux de progression, CHRONOLOGIE | gallery names stay English |
| StandBy | `Soon · StandBy` | Soon · StandBy | description: "…optimisé pour le mode StandBy" |
| Lock Screen / Home Screen | `Keep on Lock Screen`; `Your countdown on Home Screen and Lock Screen.` | Garder sur l’écran verrouillé; Ton compte à rebours sur l'écran d'accueil et l'écran de verrouillage | FLAG: Lock Screen is "écran verrouillé" in one string and "écran de verrouillage" in another. Apple's iOS term is "écran verrouillé" |
| Event types | `Trip` `Wedding` `Birthday` `Anniversary` `Concert` `Baby` `Exam` `Work` `Holiday` `Health` `Sport` | Voyage, Mariage, Anniversaire, Anniversaire de couple, Concert, Bébé, Examen, Travail, Fête, Santé, Sport | FLAG: Anniversary → "Anniversaire de couple" while Birthday → "Anniversaire"; `Holiday` → "Fête". The category is "Bébé", not "Pregnancy" |
| Baby mode | `Baby` | Bébé | |
| On This Day | `ON THIS DAY` | CE JOUR-LÀ | |
| Milestone | `Add milestone` | Ajouter un jalon | |
| Streak (widget) | `Day streak` / `day streak` | Série de jours / jours d'affilée | |
| Count up | `days since` / `%lld days since` | jours écoulés / il y a %lld jours | |
| Pin | `Pin to top` | Épingler en haut | |
| iCloud sync | `iCloud Sync` | Synchronisation iCloud | the catalog has iCloud strings; check against the site claim (on-device and own iCloud) |
| Save | `Save` / `Save moment` | Enregistrer / Enregistrer le moment | consistent in French |

Other flags:
- **tu / vous mix in one catalog**: main app 33 strings with tu-forms vs 35 with vous-forms; widgets 0 vs 33 (all vous); permission prompts all vous. Examples: tu: "Ajoute des comptes à rebours pour remplir ce widget", "Planifie tes moments", "Ton écran d'accueil, tes moments." vous: "Importer depuis votre calendrier", "Ouvrez Soon. pour passer à Premium.", "Demandez combien de jours restent…". No string mixes both.
- Permission prompts (verbatim): calendar "Soon. lit vos événements de calendrier pour que vous puissiez les transformer en comptes à rebours. Rien n'est modifié ni partagé."; location "Votre position est utilisée pour afficher les prévisions météo de vos événements à rebours." (awkward "événements à rebours").
- Premium wording elsewhere: `Manage Subscription` → "Gérer l'abonnement"; `Purchases Restored` → "Achats restaurés"; `Support the Developer` → "Soutenir le développeur"; `One-time tip. Not a subscription.` → "Pourboire unique. Pas d'abonnement."

### Paid tier names (as the French UI shows them)
Premium; plan labels Mensuel / Annuel / À vie; "Essai gratuit" and "1 semaine gratuite"; "Restaurer les achats". The store product names: "Premium mensuel", "Premium annuel", "Premium achat unique", "Soutenir le développeur".

### French App Store listing (checked 2026-11-07, https://apps.apple.com/fr/app/id6757280643)
- Name: **Soon. - Jours Avant Événements** (English: "Soon. - Days Until Big Events", so it differs)
- Subtitle: **Mariage, Voyage Bébé Countdown** (English: "Wedding, Trip & Baby Countdown"; FLAG: no comma between Voyage and Bébé, English word "Countdown" kept)
- In-app purchases (reference): `Premium achat unique 14,99 €` · `Soutenir le développeur 1,00 €` · `Premium mensuel 1,99 €` · `Premium annuel 9,99 €` (US: $12.99 / $1.00 / $1.99 / $9.99)
- Langues: **Français et 35 de plus** (list: Français, Allemand, Anglais, Arabe, Bulgare, Catalan, Chinois simplifié, Chinois traditionnel, Coréen, Croate, Danois, Espagnol, Finnois, Grec, Hindi, Hongrois, Hébreu, Indonésien, Italien, Japonais, Kazakh, Malais, Norvégien, Néerlandais, Polonais, Portugais, Roumain, Russe, Slovaque, Slovène, Suédois, Tchèque, Thaï, Turc, Ukrainien, Vietnamien)
- Category: **Style de vie** (also tagged "Utilitaires"; US: Lifestyle / Utilities)

---

### 2. Tare (`tare`, source `weightbalance/`, ID 6806255929)

### French coverage
| Catalog | keys | `fr` translated | % |
|---|---|---|---|
| weightbalance/Localizable.xcstrings (main app, the only catalog) | 121 | 121 | 100 % |

No InfoPlist.xcstrings and no permission prompts; the display name is set in build settings and stays "Tare". **Verdict: app is in French: yes.**

### Glossary
| English term on site | English UI string (key) | French UI string (verbatim) | Note |
|---|---|---|---|
| Chapter I…X | `Chapter %lld` | Chapitre %lld | |
| Unlock / buy chapters | `Open Chapters %lld to %lld` / `Buy Chapters %lld to %lld, %@` / `Buy Chapter %lld, %@` | Ouvrir les chapitres %1$lld à %2$lld / Acheter les chapitres %1$lld à %2$lld, %3$@ / Acheter le chapitre %1$lld, %2$@ | |
| Unlock text | `%@ more %lld chapters of handcrafted levels. Yours forever.` | %1$@ %2$#@chapters@ de plus, avec des niveaux faits main. À vous pour toujours. | the only vous in the catalog |
| Restore purchases | `Restore purchases` | Restaurer les achats | |
| Settings | `Settings` | Réglages | |
| Hints | `Hints` / `Hint` | Indices / Indice | |
| Three gold stars | `Marks` | Étoiles | setting is "Marks" in English, "Étoiles" in French |
| Sound / Haptics | `Sound` / `Haptics` | Son / Vibrations | |
| High contrast | `High contrast` | Contraste élevé | |
| Beam | `Beam %lld` | Fléau %lld | Owner decision 2026-11-11: « fléau » (masculine: « un fléau peint », « suspendu au fléau »), replacing « branche » in the app and the fr-FR listing. The arm stays « bras » (`%@ arm, notch %lld` → "Bras %1$@, cran %2$lld"). |
| Hook / notch | `empty hook` / `notch` | crochet vide / cran | |
| Hidden "?" weight | `hidden %@` / `cannot settle, hidden weight` | %@, poids caché / ne peut pas se stabiliser, poids caché | |
| Picture cards | `Reference scale` | Balance de référence | VoiceOver wording; no UI string says "picture card" |
| Shelf (weights below) | `Tray` / `Return to tray` | Plateau / Reposer sur le plateau | |
| Balanced | `Balanced` / `balanced` | En équilibre / en équilibre | `Balanced. Level complete.` → "En équilibre. Niveau terminé." |
| Mobile | `Mobile` | Mobile | the hanging sculpture |
| Play | `Play` | Jeu | noun, not an action verb |
| Level | `Level %lld` | Niveau %lld | |
| Restart / Pause / Resume | `Restart level` / `Pause` / `Resume` | Recommencer le niveau / Pause / Reprendre | |
| Chapter names | `The Hang`, `The Secret`, `The Cascade`, `The Exhibition`, `The Ledger`, `The Inventory`, `The Fulcrum`, `The Forgery`, `The Restoration`, `The Retrospective` | L'Accrochage, Le Secret, La Cascade, L'Exposition, Les Comptes, L'Inventaire, Le Pivot, Le Faux, La Restauration, L'Anthologie | in the catalog's order |
| Worlds | `Morning Sky`, `Twilight Meadow`, `Deep Sea`, `Evening Stars`, `Coral Reef`, `Firefly Forest`, `Polar Night`, `Rose Dawn`, `Summer Fields`, `Sunset Hills` | Ciel du matin, Prairie du crépuscule, Grands fonds, Étoiles du soir, Récif de corail, Forêt des lucioles, Nuit polaire, Aube rose, Champs d'été, Collines du couchant | |
| Share / rate | `Share Tare` / `Rate Tare` | Partager Tare / Noter Tare | |
| Terms | `Terms of use` / `Privacy` | Conditions d'utilisation / Confidentialité | |

Register: essentially no direct address (tu 0, vous 1). Safe for vous.

### Paid tier names and the one-time unlock
There is no tier name: Tare is free with chapter packs. The French UI sells chapters through "Acheter les chapitres %1$lld à %2$lld, %3$@" and "Ouvrir les chapitres %1$lld à %2$lld", and the unlock text reads "…de plus, avec des niveaux faits main. À vous pour toujours." The store IAP is named **"Chapitres II–X"** (so it matches the site's "Chapters II to X"; the German glossary recorded "Kapitel II–IV", which looks stale). Locked levels are announced as "Chapitre %lld, non acheté".

### French App Store listing (checked 2026-11-07, https://apps.apple.com/fr/app/id6806255929)
- Name: **Tare: Casse-tête de réflexion** (English: "Tare: Balance Logic Puzzle", so it differs; FLAG: colon with no space before it, whereas Shogiful's French name uses " : ")
- Subtitle: **Énigme, logique et équilibre** (English: "Brain Teaser & Hidden Weights")
- In-app purchase (reference): `Chapitres II–X 2,99 €` (U+00A0 before €; US: "Chapters II–X $2.99")
- Langues: **Français et 43 de plus**
- Category: **Casse-tête** (also tagged "Parties rapides"; US: Puzzle)

---

### 3. Taskful Day (`taskful-day`, source `TaskLogger/`, ID 6757345400)

### French coverage
| Catalog | keys | `fr` translated | % |
|---|---|---|---|
| TaskLogger/Localization/Localizable.xcstrings (main app) | 1427 (+1 not translatable) | 1427 | 100 % |
| TaskfulDayKit Localizable.xcstrings (shared package) | 114 | 112 | 98.2 % (missing `End focus session`, `Extend focus session`) |
| TaskLogger/InfoPlist.xcstrings | 7 | 7 | 100 % (calendar, Reminders, microphone, speech permission texts) |
| TaskLogger/AppShortcuts.xcstrings | 12 | 12 | 100 % |
| TaskLoggerWidgetsExtension Localizable + InfoPlist | 420 + 3 | 420 + 3 | 100 % |
| watch app AppShortcuts.xcstrings | 4 | 4 | 100 % (the source has a watch target; the site page says "iPhone, iPad, Mac, and Apple Watch" in its pre_headline, check against the master) |

Not in French: only the two TaskfulDayKit focus-session strings (they fall back to English). **Verdict: app is in French: yes (two shared-package strings missing).**

### Glossary
| English term on site | English UI string (key) | French UI string (verbatim) | Note |
|---|---|---|---|
| Day Clock | `Day Clock` (`clock.title`, `pro.feature.clock_view`) | Horloge du jour | picker label `Clock` has many sub-keys |
| Energy River | `Energy River` (`river.title`) | Rivière d’énergie | |
| Day Map | `Day Map` (`pro.feature.day_map`) | Carte du jour | picker/title `Map` → "Carte" |
| Focus Orbit / Focus Mode | `Focus Mode` (`pro.feature.focus_orbit`) | Mode concentration | FLAG: the feature is "Mode concentration" but the session strings use the loanword: `Focus Session` → "Session focus", `Start Focus` → "Démarrer le focus", `focus.enter` `Focus` → "Focus". No UI string says "Focus Orbit" |
| Inbox | `Inbox` / `Add to Inbox` (`inbox.title`) | boîte ("La boîte est vide.") / Ajouter à la boîte | no title string "Inbox" → "Boîte de réception"; the app says only "la boîte". Needs a decision |
| Today / Tomorrow | `Today` / `Tomorrow` | Aujourd'hui / Demain | |
| Tabs | `Tasks`, `All Tasks`, `Analytics`, `Settings` (`tab.*`) | Tâches, Toutes les tâches, Analyses, Réglages | |
| Insights / analytics | `Insights` / `Full Analytics & Insights` | Aperçu (e.g. "Aperçu mensuel") / Analyses | FLAG: `Insights` has no single French term; "Analyses" is the pro-feature label for "Full Analytics & Insights" |
| Journal | `Journal` | Journal | |
| Mood | `Mood` / `Mood pattern` | (mood scale: Super, Bien, Neutre) / Tendance d’humeur | |
| Workspaces | `Workspace` / `Multiple Workspaces` | Espace / Espaces de travail multiples | FLAG: "Supprimer l'espace", "Gérer les espaces" vs the Pro label "Espaces de travail multiples" |
| Carry forward | `Carry Forward` / `Auto carry-forward` / `Rollover` | Reporter / Report automatique (iPad canvas: Reporter automatiquement) / Reports | FLAG: "Reporter automatiquement" vs "Report automatique" |
| Voice capture | `Voice capture` / `Voice Task` / `Smarter Voice Input` | Capture vocale / Tâche vocale / Saisie vocale | the paywall title also drops "smarter" |
| iCloud sync | `iCloud Sync` | Synchronisation iCloud (Settings) / Synchronisation (Pro list) / "sync iCloud" ("Préparation de la sync iCloud …") | three variants |
| Apple Reminders import | `Import from Reminders` / `Reminders Re-import` | Importer depuis Rappels / Rappels | Pro label is only "Rappels" |
| Widgets (Pro) | `All Widgets` / `Unlock all widgets` | Widgets / Débloquer tous les widgets | |
| Pro | `Taskful Day Pro` / `Unlock Pro` | Taskful Day Pro / Déverrouiller Pro | FLAG: "Déverrouiller Pro" (settings) vs "Débloquez Pro" (widget gallery) |
| Free | `Free Plan` / `Available with Free` | Offre gratuite / Gratuit | |
| Monthly / Yearly / Lifetime | `pro.plan.monthly` / `.yearly` / `.lifetime` | Mensuel / Annuel / Accès définitif | FLAG: lifetime has three wordings: plan "Accès définitif", button `pro.buy_lifetime` "Acheter l'accès définitif", status "Pro à vie", terms "L’achat à vie est unique. Aucun renouvellement." |
| 7-day free trial | `7-day free trial` / `Start 7-day free trial` | Essai gratuit / Commencer l'essai | "7 days" is not in the French strings |
| Restore purchases | `Restore Purchases` | Restaurer les achats | |
| Schedule | `Schedule` (week grid) | (week strings; empty state "Aucune tâche programmée cette semaine") | |
| Overdue / Later | `Overdue` / `Later` | En retard / Plus tard | |
| Streak | `Streak` | Série | |

Other flags:
- **tu / vous mix**: main catalog 56 strings with tu-forms vs 112 with vous-forms; widgets 0 vs 29; InfoPlist prompts all vous. The "insight" sentences use tu ("Tu es présent depuis %d jours. Pas de pression — juste de la reconnaissance.", "Garde-le doux.", "Ton énergie était concentrée…"); most UI uses vous ("Créez plusieurs espaces…", "Capturez une idée quand elle vous vient.", "Vous avez créé 50 tâches avec le plan gratuit").
- Permission prompts (verbatim): calendar "Affichez vos événements de calendrier à côté de vos tâches pour avoir tout le programme de la journée au même endroit."; Reminders "Taskful Day peut importer vos Rappels Apple pour planifier votre journée en un seul endroit."; microphone "Taskful Day utilise le microphone pour capturer votre voix et créer des tâches rapidement."; speech "Taskful Day utilise la reconnaissance vocale pour convertir votre voix en texte de tâche."
- The paywall lists Day Clock, Day Map, Energy River and Focus Mode as Pro features; the site's Free tier says "All four visual day views". Check against the code before translating the Free tier (same flag as German).

### Paid tier names (as the French UI shows them)
"Taskful Day Pro"; plan labels Mensuel / Annuel / Accès définitif; status "Pro mensuel", "Pro à vie"; "Offre gratuite"; "Commencer l'essai"; "Restaurer les achats"; "Déverrouiller Pro". Store products: "Taskful Day Pro mensuel", "Taskful Day Pro annuel", "Taskful Day Pro achat unique", "Soutenir le développeur".

### French App Store listing (checked 2026-11-07, https://apps.apple.com/fr/app/id6757345400)
- Name: **Taskful Day: Planificateur** (English: "Taskful Day: Day Planner", so it differs)
- Subtitle: **Liste Tâches & Rappels** (English: "Calm Task Tracker & To-Do List")
- In-app purchases (reference): `Soutenir le développeur 1,00 €` · `Taskful Day Pro achat unique 44,99 €` · `Taskful Day Pro annuel 29,99 €` · `Taskful Day Pro mensuel 2,99 €` (US: $1.00 / $39.99 / $24.99 / $2.99)
- Langues: **Français et 33 de plus**
- Category: **Productivité** (also tagged "Utilitaires"; US: Productivity)

---

### 4. WanderWiki (`wanderwiki`, source `WanderWiki/`, ID 6758459119)

### French coverage
| Catalog | keys | `fr` translated | % |
|---|---|---|---|
| WanderWiki/Resources/Localizable.xcstrings (main app) | 425 | 425 | 100 % |
| WanderWikiWidget/Localizable.xcstrings | 129 | 129 | 100 % |

No InfoPlist.xcstrings; the display name comes from build settings and no permission texts are declared. **Verdict: app is in French: yes.**

### Glossary
| English term on site | English UI string (key) | French UI string (verbatim) | Note |
|---|---|---|---|
| Random | `Random` (`random_mode`) | Aléatoire | |
| Browse | `Browse` (`browse_title`) | Parcourir | |
| For You | `For You` (`for_you_mode`) | Pour vous | quoted « Pour vous » in running text |
| Today in History | `Today in history` / `On This Day` | Ce jour dans l'histoire | both English terms give the same French string |
| On This Day categories | `Events` / `Births` / `Deaths` / `Holidays` | Événements / Naissances / Décès / Fêtes | |
| Tabs | `Feed` / `Profile` / `settings` | Flux / Profil / Réglages | |
| WanderWiki Plus | `Unlock Premium` / `Premium feature` | Débloquer Premium / Fonctionnalité premium | FLAG: no "Plus" string; the tier is "Premium". Capitalization: "Premium" on a button, "premium" in "Fonctionnalité premium" and "une expérience premium" |
| Monthly / Annual / Weekly / Lifetime | `monthly` / `yearly` / `weekly` / `lifetime` | Mensuel / Annuel / Hebdomadaire / À vie | `subscribe_*` keys give the same words; suffixes "/mois", "/semaine", "/an" |
| Best long-term value | `Best Value` | Meilleure offre | |
| Free trial | `%lld-day free trial` / `Start %lld-Day Free Trial` | Essai gratuit de %lld jours / Démarrer l'essai gratuit de %lld jours | `trial_description`: "Commencez votre essai gratuit de 3 jours…" |
| Free articles per day | `%lld free articles left today` | Encore %lld articles gratuits aujourd'hui | |
| Restore purchases | `Restore Purchases` | Restaurer les achats | |
| Saved | `saved` / `Saved` | Enregistré / Enregistrés | consistent (number agreement only) |
| Liked list | `Liked` | Aimé | list header; `No liked articles yet` → "Aucun article aimé" |
| Folders | `Folders` / `New folder` | Dossiers / Nouveau dossier | |
| Read aloud | `Listen` | Écouter | |
| Where Next | `Where next` | Et ensuite | |
| Show less / hide | `Show less like this` / `Hide this article` | Afficher moins de ce type / Masquer cet article | |
| Reader themes | `Reader Theme`, `Sepia`, `Solarized` | Thème de lecture, Sépia, Solarized | |
| Search | `Search Wikipedia` | Rechercher sur Wikipédia | note the accent: Wikipédia |
| Reading streak | `%lld-day streak` / `Streak reminder` | Série de %lld jours / Rappel de série | |
| Widgets | `On This Day`, `Reading Year`, `Continue Reading`, `Got a Minute`, `Two Doors` | Ce jour dans l'histoire, Année de lecture, Reprendre la lecture, Une minute ?, Deux portes | |
| Control: Surprise Me | `Surprise Me` | Surprenez-moi | vous form |
| On-device summaries | `AI summary: %@` | Résumé IA : %@ | |
| 16 topics | `interest_*` | Science, Technologie, Histoire, Arts, Musique, Sports, Nature, Espace, Philosophie, Géographie, Littérature, Cinéma, Gastronomie, Architecture, Mathématiques, Politique | `movies` → "Cinéma", `food` → "Gastronomie", `space` → "Espace" |
| No ads | `feature_no_ads` / `onboarding_benefit_no_ads_title` | Expérience sans publicité / Ni pubs. Ni bruit. | |

Other flags:
- `for_you_english_only` → "Le flux personnalisé est actuellement disponible uniquement en anglais." The site says native category queries work in 17 editions; the string may be stale (same flag as German). `For You isn't available in %@ yet — showing Random.` → « Pour vous » n'est pas encore disponible en %@ — affichage Aléatoire.
- Register: vous (50 main strings, 12 widget strings, 0 tu pronouns). Five VoiceOver hints use a bare imperative ("Ouvre l'article", "Ouvre un défilement infini…") that reads as tu or as a neutral third person. Worth normalising to "Ouvre"/"Ouvrir".
- The paywall disclosure is in vous: "Vous pouvez gérer et résilier vos abonnements dans les réglages de votre compte App Store."

### Paid tier names (as the French UI shows them)
"Premium" (button "Débloquer Premium"; headline "WanderWiki est une expérience premium."); plan labels Mensuel / Annuel / Hebdomadaire / À vie; lifetime pitch "Possédez WanderWiki pour toujours"; "Meilleure offre"; "Restaurer les achats". Store products: "WanderWiki mensuel", "WanderWiki annuel", "WanderWiki hebdomadaire", "WanderWiki achat unique", "Soutenir le développeur". FLAG: there is a weekly plan the site does not list (same as German).

### French App Store listing (checked 2026-11-07, https://apps.apple.com/fr/app/id6758459119)
- Name: **WanderWiki : la curiosité** (English: "WanderWiki: Swipe to Discover", so it differs; note the space before the colon)
- Subtitle: **Faits, histoire et culture** (English: "Daily facts, history & trivia")
- In-app purchases (reference): `WanderWiki annuel 9,99 €` · `WanderWiki hebdomadaire 0,99 €` · `Soutenir le développeur 1,00 €` · `WanderWiki achat unique 29,99 €` · `WanderWiki mensuel 1,99 €` (US: $8.99 / $0.99 / $1.00 / $24.99 / $1.99)
- Langues: **Français et 33 de plus**
- Category: **Éducation** (also tagged "Références"; US: Education)

---

### 5. Xiangqiful (`xiangqiful`, source `Xiangqi/`, ID 6794340136)

### French coverage
| Catalog | keys | `fr` translated | % |
|---|---|---|---|
| Xiangqi/Localization/Localizable.xcstrings (main app, includes the paywall) | 3263 | 3263 | 100 % |
| Xiangqi/Localization/InfoPlist.xcstrings | 2 | 2 | 100 % (display name only, stays "Xiangqiful") |

No widget or extension catalogs. **Verdict: app is in French: yes.**

### Glossary
| English term on site | English UI string (key) | French UI string (verbatim) | Note |
|---|---|---|---|
| Tabs | `Home`, `Play`, `Training`, `Analysis`, `Progress` (`tab.*`) | Accueil, Jouer, Entraînement, Analyse, Progrès | |
| Game Review | `Game review` (`analysis.review.title`) | Revue de partie | |
| Analyze | `Analyze` | Analyser | `Analyze this game` → "Analyser cette partie" |
| Move grades | `Best`, `Great`, `Good`, `Book`, `Inaccuracy`, `Mistake`, `Blunder` (`classification.*`) | Meilleur, Excellent, Bon, Théorique, Imprécision, Erreur, Gaffe | counts header: Meilleurs / Imprécisions / Erreurs / Gaffes. `Better was` → "Meilleur coup". "Meilleur" alone is an adjective without a noun |
| Accuracy | `Accuracy` | Précision | `%@ accurate` → "%@ de précision" |
| Estimated rating | `Estimated rating` | Classement estimé | |
| Skill profile / radar | `Skill profile` | Profil de compétences | paywall: "Radar de compétences complet" |
| Weakness trends | `Weakness trends` | Tendances des points à travailler | paywall hero: "l'évolution de tes points faibles" |
| Five skills | `Tactics`, `Defense`, `Positioning`, `Endgame`, `Openings` | Tactique, Défense, Position, Finale, Ouvertures | note "Finale" (xiangqi term), not "Fin de partie" |
| Phases | `Opening`, `Middlegame`, `Endgame` | Ouverture, Milieu de partie, Finale | |
| Today's plan | `Today's plan` | Plan du jour | |
| Lessons / 8 tracks | `Lessons`; `Fundamentals`, `Openings`, `Palace Defense`, `Cannon Tactics`, `Horse Technique`, `Middlegame`, `Endgame`, `Advanced` | Leçons; Fondamentaux, Ouvertures, Défense du palais, Tactiques de canon, Technique du cheval, Milieu de partie, Finale, Avancé | "Huit parcours" = eight tracks |
| Skill assessment | `Skill Assessment` | Évaluation de Niveau | FLAG: also "l'évaluation de compétences" in an achievement and "l'évaluation de niveau" in onboarding |
| Drill modules | `Tactics Yard`, `Cannon Range`, `Horse Trails`, `Palace Workshop`, `Endgame Studio`, `Opening Lab`, `Mate Trail`, `Tactic Cards`, `Handicap House` | Terrain de Tactique, Portée du Canon, Pistes du Cheval, Atelier du Palais, Atelier des Finales, Labo des Ouvertures, Piste du Mat, Cartes Tactiques, Maison des Handicaps | FLAG: Title Case on every French module title (not French usage); "Atelier" is used twice (Palace Workshop and Endgame Studio) |
| Mate problems / puzzles | `Mate problem` / `Puzzles` | Problème de mat / Problèmes | |
| Coach hints | `Unlimited in-game coach hints` / `Hint` | Indices de coach illimités en partie / Indice | consistent: coach and lesson buttons both use "Indice" |
| Named mistakes | `Screenless cannon`, `Trapped horse`, `Broken advisors`, `Iron Bolt`, `Missed mate` | Canon sans écran, Cheval piégé, Conseillers brisés, Verrou de Fer, Mat manqué | "Verrou de Fer" capitalised in the title, "Le verrou de fer" in a lesson |
| Piece styles | `Traditional` / `Western` / `Hybrid` (`board.pieceSet.*`) | Traditionnel / Occidental / Hybride | setting `Pieces` → « Pièces » ; site term « style de pièces » (2026-11-14, I-0324). « Jeu de pièces » now means only the eight finishes (`Piece Finish` → « Finition des pièces » in the app; Ivoire, Bois sculpté …) |
| Characters | `Traditional` / `Simplified` (`board.charset.*`) | Traditionnel / Simplifié | |
| Notation | `WXF` / `Chinese` | WXF / (Chinese notation text: "notation chinoise") | |
| Boards | `Boxwood` / `Rosewood` / `3D Board` | Buis / Palissandre / Plateau 3D | |
| Flip board / New game | `Flip board` / `New Game` | Retourner le plateau / Nouvelle partie | |
| Premium | `Xiangqiful Premium` / `Upgrade to Premium` | Xiangqiful Premium / Passer à Premium | `Welcome to Premium` → "Bienvenue dans Premium" |
| Free | `Free plan` | Offre gratuite (settings) / formule gratuite ("Continuer avec la formule gratuite") | FLAG: two words, "offre" and "formule" |
| Monthly / Yearly / Lifetime | `paywall.plan.*` | Mensuel / Annuel / À vie | `Unlock forever` → "Débloquer pour toujours"; `settings.premium.lifetimeNoManage` → "À vie — rien à renouveler, rien à annuler" |
| Best value | `Best value` | Meilleure offre | same as WanderWiki |
| Start free trial | `Start free trial` | Démarrer l'essai gratuit | `%lld-day free trial` → "Essai gratuit de %lld jours" |
| Restore purchases | `Restore purchases` | Restaurer les achats | |
| Check / checkmate / stalemate | `Check` / `Checkmate` / `Stalemate` | Échec / Échec et mat / pat | the stalemate explainer says "Contrairement aux échecs, un joueur sans coup légal… perd" |
| Sides | `Red` / `Black` | Rouge / Noir | `Play as Red` → "Jouer les Rouges" |
| Palace / river | `palace` / `river` | palais / rivière | |

**French piece names the app uses** (`piece.*`): Général (general), Conseiller (advisor), Éléphant (elephant), Cheval (horse), Chariot (chariot), Canon (cannon), Soldat (soldier). Lower-case inline forms: général, conseiller, éléphant, cheval, chariot, canon, soldat. The cannon's "screen" is "écran" throughout (e.g. "Canon sans écran", "Shénpào voit l'écran dont tu avais oublié l'existence"). The pinyin names stay in running text (chángjiāng, kùnbì).

Other flags:
- **Register is tu** (376 strings with tu/ton/ta/tes/toi; 2 with vous). Examples: "Tu as déjà tout débloqué. Merci.", "Annule à tout moment dans Réglages.", "Vérifie ta connexion et réessaie.", "Xiangqiful te plaît ?". The two vous strings are the plural address "Aucun de vous deux…" (achievement text), not formal vous. Site rule (section 13) is vous, so quoting app strings needs a register conversion.
- Stale string like German: `paywall.benefit.opponents` ("All 40 opponents…") → "Les 40 adversaires, débloqués d'un coup" is unused in code (per the German note), so do not use it.
- Title-case French module names and "Évaluation de Niveau" read as English-style capitalization.
- Paywall benefits (verbatim): "Analyse de partie illimitée", "Indices de coach illimités en partie", "Analyse moteur multi-lignes approfondie", "Tous les exercices de chaque module", "Radar de compétences complet, tendances et progression hebdomadaire", "Problèmes d'entraînement illimités". Free limits: "2 analyses, 3 problèmes et 2 indices du coach par jour".

### Paid tier names (as the French UI shows them)
"Xiangqiful Premium"; plan labels Mensuel / Annuel / À vie; "Offre gratuite"; "Démarrer l'essai gratuit"; "Restaurer les achats"; "Gérer l'abonnement"; "Achat unique". Store products: "Premium mensuel", "Premium annuel", "Premium à vie", and tip items "Soutien", "Énorme soutien", "Un café".

### French App Store listing (checked 2026-11-07, https://apps.apple.com/fr/app/id6794340136)
- Name: **Xiangqiful : Échecs chinois** (English: "Xiangqiful Learn Xiangqi & AI", so it differs)
- Subtitle: **Apprendre le xiangqi avec l'IA** (English: "Chinese Chess Tactics Trainer")
- In-app purchases (reference): `Premium annuel 9,99 €` · `Premium mensuel 1,99 €` · `Soutien 5,99 €` · `Énorme soutien 9,99 €` · `Un café 1,99 €` · `Premium à vie 22,99 €` (US: $9.99 / $1.99 / $4.99 / $9.99 / $1.99 / $19.99)
- Langues: **Français et 33 de plus**
- Category: **Jeux de société** (US: Board)

---

### 6. Clippet (`clippet`, source `clipboard/`, ID 6829498729, NOT released; no German section exists)

Built from the English page `_apps/clippet.md`, the blueprint `~/Downloads/clipboard/APP_BLUEPRINT.md` (sections 1, 4.O, 7) and the catalogs. The blueprint says all 40 App Store locales are written and every catalog carries every language.

### French coverage
| Catalog | keys | `fr` translated | % |
|---|---|---|---|
| clipboard/Localizable.xcstrings (main app, paywall) | 634 | 634 | 100 % |
| clipboard/AppShortcuts.xcstrings (Siri and Spotlight) | 2 | 2 | 100 % |
| clipboard/InfoPlist.xcstrings | 8 | 7 | 87.5 % (missing `CFBundleName`, not user-facing) |
| ClipboardKit Localizable.xcstrings | 26 | 26 | 100 % |
| ClipboardKeyboard Localizable + InfoPlist | 104 + 2 | 104 + 1 | 100 % / 50 % (missing `CFBundleName`; the display name is set) |
| ClipboardAction Localizable + InfoPlist | 1 + 2 | 1 + 1 | 100 % / 50 % (missing `CFBundleName`) |
| ClipboardWidgets Localizable + InfoPlist | 63 + 2 | 63 + 1 | 100 % / 50 % (missing `CFBundleName`) |
| ClipboardShare Localizable + InfoPlist | 28 + 2 | 28 + 1 | 100 % / 50 % (missing `CFBundleName`) |
| ClipboardMacBridge Localizable.xcstrings | 19 | 19 | 100 % |

Permission prompts are in French: contacts "Enregistre un numéro de téléphone ou une carte de visite d’un élément comme nouveau contact lorsque vous choisissez Ajouter à Contacts."; Face ID "Permet à Verrouillage de l’app de déverrouiller Clippet pour vous, afin que vous seul puissiez voir vos éléments."; photo library "Enregistre la photo ou la vidéo d’un élément dans votre photothèque lorsque vous choisissez Enregistrer dans Photos."; Reminders "Ajoute un rappel dans l’app Rappels lorsque vous lancez une action Rappel que vous avez configurée pour un élément." (three of the four prompts start with a bare third-person verb, which is intentional French style, not tu). Siri phrases: "Coller la dernière copie dans ${applicationName}", "Enregistrer ma dernière copie dans ${applicationName}". **Verdict: app is in French: yes** (only the non-visible `CFBundleName` keys are missing).

### Glossary
| English term on site | English UI string (key) | French UI string (verbatim) | Note |
|---|---|---|---|
| Clipboard | `Clipboard` | presse-papiers ("Accès au presse-papiers", "Surveiller le presse-papiers") | |
| Clip | `Clip` / `Clips` | Élément / éléments | matches the listing ("clip = élément", "clip card = vignette"); widgets say "Dernier élément" |
| Library | `Library` | bibliothèque ("Ses éléments restent dans votre bibliothèque.") | the photo library is "photothèque" |
| Smart Actions | `Smart Actions` | Actions intelligentes | |
| Custom actions | `Custom Actions` | Actions personnalisées | |
| Boards | `Boards` / `New Board` / `Add to Board` | Tableaux / Nouveau tableau / Ajouter au tableau | |
| Tags | `Tags` | Tags | listing keeps "tags" |
| Pin | `Pin` / `Pinned` | Épingler / Épinglés | widget "Pinned Clips" → "Éléments épinglés" |
| Quick Paste | `Quick Paste` | Collage rapide | |
| Quick Add (widget) | `Quick Add` | Ajout rapide | |
| Paste | `Paste` | Coller | |
| App Lock | `App Lock` | Verrouillage de l’app | `Face ID Lock` → "Verrouillage par Face ID" |
| iCloud Sync | `iCloud Sync` | Synchronisation iCloud | |
| Backup | `Backup` | Sauvegarde | file type "Sauvegarde Clippet" |
| Auto-delete | `Auto-Delete` | Suppression automatique | `Auto-delete in %@?` → "Supprimer auto dans %@ ?" (abbreviated) |
| Menu bar | `Menu Bar` | Barre des menus | |
| Open at login | `Open at Login` | Ouvrir à l’ouverture de session | FLAG: the listing says "se lancer à l’ouverture de session" |
| Save to Clippet | `Save to Clippet` | Enregistrer dans Clippet | |
| Clippet keyboard | `Clippet Keyboard` | Clavier Clippet | |
| Quick Look | `Quick Look` | Coup d’œil | |
| Copy as plain text | `Copy as Plain Text` | Copier en texte brut | |
| Search | `Search` / `Search Clips` | Rechercher / Rechercher des éléments | |
| Settings | `Settings` | Réglages | |
| Content types | `Link`, `Images`, `Videos`, `PDFs`, `Audio`, `Files`, `Code`, `Text` | Lien, Images, Vidéos, PDF, Audio, Fichiers, Code, Texte | |
| Sensitive | `Sensitive Clips` | contenu sensible / "Supprimer automatiquement les éléments sensibles" | |
| Older clips hidden | `%lld older clips are hidden` | plural variations ("%lld élément plus ancien est masqué", …) | `See Older Clips` → "Voir les éléments plus anciens"; `Not Now` → "Pas maintenant" |
| Widgets | `Latest Clip`, `Pinned Clips`, `Add Clip`, `Recently copied` | Dernier élément, Éléments épinglés, Ajouter un élément, Copiés récemment | |
| Free trial | `Start Free Trial` / `%lld days free` | Commencer l’essai gratuit / plural "%lld jour gratuit", … | |

Register: vous (99 main strings, 14 keyboard, 6 widget; 0 tu pronouns). Consistent.

### Paid tier names (as the French UI shows them)
**"Clippet Pro"**; "Obtenir Clippet Pro" (purchase button); plan labels Mensuel / Annuel / À vie; "Commencer l’essai gratuit"; "Restaurer les achats"; "Gérer l’abonnement"; the description of the purchase: "Un seul achat débloque Clippet Pro sur votre iPhone, votre iPad et votre Mac, et le partage familial…". The planned store product names (`marketing/aso/purchases.json`, fr-FR): "Clippet Pro mensuel", "Clippet Pro annuel", "Clippet Pro à vie".

### French App Store listing
Not live: https://apps.apple.com/fr/app/id6829498729 and the US page both returned HTTP 404 on 2026-11-07. The prepared listing (`~/Downloads/clipboard/marketing/aso/listing.json`, `listing-texts.md`, fr-FR; not yet published, so reference only):
- Name: **Clippet : Presse-papiers** (English plan: "Clippet: Clipboard Manager")
- Subtitle: **Historique du copier-coller** (English plan: "Copy & Paste History, Snippets")
- Promotional text: "Tout ce que vous copiez, conservé. Une recherche retrouve textes, liens, images, PDF et code dans Clippet, un historique du presse-papiers pour iPhone, iPad et Mac."
- Terms used (from the listing file): Smart Actions = Actions intelligentes; boards = tableaux; Quick Add = Ajout rapide; Home Screen = écran d’accueil; menu bar = barre des menus; app switcher = sélecteur d’app; Quick Look = Coup d’œil; widget = widget; photo library = photothèque; open at login = se lancer à l’ouverture de session; clipboard = presse-papiers; clip = élément; clip card = vignette; tags = tags; pin = épingler. Register: vous.
- Category (blueprint suggestion, not confirmed): Utilities primary, Productivity secondary. Langues line: not available (page not live); the blueprint says 40 locales.


