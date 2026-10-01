---
layout: journal
slug: xiangqi-mate-problems-from-classical-manuals
title: "902 xiangqi mate problems, eight old books, and the problems I left out"
date: 2026-10-01
seo:
  title: "Xiangqi Mate Problems from Classical Manuals — Xiangqiful"
  description: "Where Xiangqiful's 902 xiangqi mate problems come from: 708 from eight classical manuals such as the Shiqing Yaqu, 194 original, every line solver-checked."
  keywords:
    - xiangqi mate problems
    - chinese chess puzzles
    - xiangqi checkmate puzzles
    - consecutive check mate
    - shiqing yaqu
    - classical xiangqi manuals
    - xiangqi puzzle app
    - xiangqiful
lede: "Xiangqiful ships 902 consecutive-check mate problems. I composed 194 of them; the other 708 come from eight classical manuals, one of them from 1570. No book problem was edited to make it work. The ones that didn't work aren't in the app. Here is the full count, by book and by depth, and how every line was checked."
quick_answer: "Xiangqiful's 902 mate problems are all consecutive-check mates (连将杀): every move by the attacking side must give check, and the defender resists as long as possible. 708 come from eight classical manuals: Shiqing Yaqu (适情雅趣, 1570) 227, Lanke Shenji (烂柯神机) 166, Taolue Yuanji (韬略元机) 129, Mengru Shenji (梦入神机) 94, Yuanshen Haige (渊深海阁) 84, Juzhongmi (橘中秘) 5, Zhuxiang Zhai (竹香斋) 2 and Xinwu Canbian (心武残编) 1. The other 194 were composed for the app. They run from mate in 1 to mate in 7, counted in plies (single moves by either side): 245 mate-in-1, 239 mate-in-3, 125 mate-in-5 and 293 mate-in-7. 36 book problems are used whole; 672 are the last 1, 3, 5 or 7 plies of a longer line from the book. The app's own solver, MateValidator, proved every one. The book's line must be legal, check on every attacking move and end in checkmate, there must be exactly one winning first move, and no later move may have a second mate. Book lines were never corrected to fit; a problem that failed was left out. The same validator checks every problem again on the device before the problem is stored."
faq:
  - q: "What is a consecutive-check problem in xiangqi?"
    a: "A consecutive-check problem (连将杀) is xiangqi's native puzzle form. The attacker, usually Red, must give check with every move until the defending general is checkmated, and the defender plays the reply that holds out longest. A quiet move that sets up an unstoppable mate is a different kind of problem, and so is a win by stalemate: in xiangqi a player with no legal move loses, but leaving the general with no move without giving check does not count as a consecutive-check mate. The form has the same constraint as Japanese tsume-shogi."
  - q: "What is the Shiqing Yaqu?"
    a: "The Shiqing Yaqu (适情雅趣) is a Ming-dynasty xiangqi manual from 1570 and the standard collection of classical mating problems. The transcription Xiangqiful worked from has 549 positions, and the book scores 452 of them as wins for Red. 227 problems in Xiangqiful come from it, more than from any other manual, and every one was re-proved by the app's own solver before it shipped."
  - q: "What does mate in 3 mean in a xiangqi problem?"
    a: "In xiangqi problems, and in Xiangqiful, depth is counted in plies: single moves by either side. Mate in 3 means Red checks, Black replies, Red mates. Mate in 5 is three Red moves and mate in 7 is four. The count is always odd because the attacker gives the last move. Chess counts only the attacker's moves, so a xiangqi mate in 3 is what a chess book would call mate in 2, and a mate in 7 is a chess mate in 4. Japanese tsume-shogi counts the same way xiangqi does."
  - q: "Are the problems in classical xiangqi manuals always correct?"
    a: "Not always. When a solver checks them, some book lines don't end in checkmate, some first moves can be met by a reply the book never mentions, and some problems have a second mating move that makes the book's answer only one of several. Xiangqiful's import checked each book line with its own solver and left out every problem that failed, rather than editing the book until it passed. Of the 1,218 positions the eight manuals score as wins for Red, 708 produced a problem that passed."
  - q: "How many mate problems are in Xiangqiful, and are they free?"
    a: "There are 902: 245 mate-in-1, 239 mate-in-3, 125 mate-in-5 and 293 mate-in-7. They are in the Mate Trail module, grouped by depth. The free tier includes 3 training puzzles a day, and mate problems count toward that. Premium removes the limit for $1.99 a month or $9.99 a year, each with a one-week free trial, or $19.99 once. Everything runs offline on iPhone, iPad and Mac, with no account."
  - q: "Do I need to read Chinese to solve classical xiangqi problems?"
    a: "No. The positions come from Chinese manuals, but you don't need the language to solve them. Xiangqiful has three piece sets: traditional characters, Western symbols and a hybrid of the two. Moves can be shown in WXF notation or Chinese notation."
mentioned_apps:
  - xiangqiful
read_time: "9 min read"
excerpt: "Xiangqiful's launch-day design essay: where its 902 consecutive-check mate problems come from, with counts per book and per depth, and how a solver re-proved every line from eight classical manuals. Book problems were never corrected to fit, so the ones that failed were left out."
---

Xiangqiful has 902 mate problems, and every one is a consecutive-check mate (连将杀). Red must check on every move until the black general is mated, and Black always picks the reply that lasts longest. I composed 194. The other 708 come from eight classical manuals, transcribed position by position and line by line. Each book line was then proved by the app's own solver. None was edited to pass, and a book problem that failed is not in the app.

The whole corpus, by source and by depth:

| Source | Mate in 1 | Mate in 3 | Mate in 5 | Mate in 7 | Total |
|---|---|---|---|---|---|
| Shiqing Yaqu (适情雅趣, 1570) | 50 | 35 | 36 | 106 | **227** |
| Lanke Shenji (烂柯神机) | 39 | 34 | 16 | 77 | **166** |
| Taolue Yuanji (韬略元机) | 30 | 19 | 29 | 51 | **129** |
| Mengru Shenji (梦入神机) | 21 | 15 | 15 | 43 | **94** |
| Yuanshen Haige (渊深海阁) | 22 | 19 | 29 | 14 | **84** |
| Juzhongmi (橘中秘) | 2 | 1 | 0 | 2 | **5** |
| Zhuxiang Zhai (竹香斋) | 2 | 0 | 0 | 0 | **2** |
| Xinwu Canbian (心武残编) | 1 | 0 | 0 | 0 | **1** |
| Composed for Xiangqiful | 78 | 116 | 0 | 0 | **194** |
| **Total** | **245** | **239** | **125** | **293** | **902** |

How much of each book made it in:

| Manual | Positions transcribed | Scored by the book as a Red win | In the app |
|---|---|---|---|
| Shiqing Yaqu | 549 | 452 | 227 |
| Lanke Shenji | 258 | 220 | 166 |
| Taolue Yuanji | 341 | 225 | 129 |
| Mengru Shenji | 150 | 134 | 94 |
| Yuanshen Haige | 374 | 115 | 84 |
| Juzhongmi | 181 | 42 | 5 |
| Zhuxiang Zhai | 200 | 25 | 2 |
| Xinwu Canbian | 155 | 5 | 1 |
| **All eight** | **2,208** | **1,218** | **708** |

Depth is counted in plies, single moves by either side. Mate in 3 means Red, Black, Red. That is how the app labels its tiers, and it is how tsume problems are counted in shogi. A chess book would call the same problem mate in 2.

## What the genre demands

Xiangqi's native puzzle has the same constraint as tsume-shogi. That is why the solver in [Xiangqiful](/apps/xiangqiful/) started as a port of the one in [Shogiful](/apps/shogiful/). It has two rules. Every attacker move must give check. The defender plays the longest defence, so the line a problem records is the one that survives longest, not the first one found.

Xiangqi adds a trap that shogi doesn't have. A player with no legal move loses, so a quiet final move that leaves the general stranded is a win in a real game. It is not a consecutive-check mate. The solver checks that the defender is in check before it counts his replies, and it only accepts a line that ends in checkmate. A straight port of the shogi solver would get this wrong, and it is the first thing the comments in that file warn about.

## 152 problems was not enough

The app was first going to ship only problems I composed. By early September there were 152 of them: 60 mate-in-1 and 92 mate-in-3. The mate-in-5 and mate-in-7 shards existed in the code but were empty. A Premium player on the long daily session would have seen every unseen problem in 19 days and then started getting repeats. Shogiful had already taught me what that costs. A one-star review there said that with only a few hundred problems, you end up memorising them.

Composing more had limits. The composer is a generator, and a candidate survives only if it passes a strict bar. Red must have at least two checking moves, and exactly one of them forces mate. Every red piece except the general has to be load-bearing, so removing any one of them destroys the problem. The defender must keep pieces near his general and at least six legal replies. No two problems may share a position or its mirror image. One more run per shard brought the originals to their final 194. The generator only composes mate in 1 and mate in 3, so it could never fill the two empty shards.

The deep problems already existed, in books.

## Eight books, 2,208 positions

I transcribed eight pre-1900, public-domain manuals from the digital editions on xqdao.com. Each problem became a starting position and the book's main line, in the notation the app's rules engine reads. That came to 2,208 positions. 837 of them are draws by the book's own verdict, 66 are wins for Black, and 87 carry no verdict at all. That left 1,218 the books score as wins for Red.

Most of those don't fit a mate-in-7 ceiling. The median main line among the 1,218 is 13 plies, the longest is 74, and only 195 are seven plies or shorter. So the import works from the end of the line. For each book problem it tries the whole problem first, then the position the book's line reaches 7 plies before the mate, then 5, 3 and 1. It keeps the longest version that passes, and it never keeps more than one per book problem.

That is why the data carries two kinds of book credit. `classical:` marks a whole problem, the book's own diagram and main line, unchanged. Only 36 problems are used whole. `after:` marks an ending, and 672 problems are endings. For example, the Shiqing Yaqu's first problem has an 11-ply main line. Xiangqiful's first mate-in-7 starts from the position after the book's fourth ply and plays the book's last seven moves exactly. The other 194 problems are credited `original`, and none of them is attributed to any collection.

## The book was not corrected to make a problem fit

That sentence is in the provenance field of every shard file, and the import works by it. A book position and line ship only if all of these hold:

- **The book claims a win for Red.** Draws and Black wins are never imported.
- **Every piece stands where a game could have put it,** neither side starts in check, and the line replays legally.
- **The book's key move holds against every reply.** Books record one defence, and the solver plays out every reply the book leaves out. If any reply escapes, the problem is out.
- **MateValidator accepts the book's line at the book's depth.** Every attacker move checks, the line ends in checkmate, no shorter mate exists, and exactly one first move wins.
- **No later move has a twin.** At every Red move along the book's line, and along every defence the solver added, the recorded move must be the only one that still mates in time. During a problem the app accepts only the recorded move, so a second mate would mark a player's correct answer as wrong.
- **It isn't already in the corpus,** in either mirror image.
- **A slow phone can re-prove it.** The solver's work is capped at 8,000 search nodes, which keeps each problem inside the device's two-second budget.

There is no step where a failing line gets patched. The import doesn't swap in a better key move or move a piece to remove a dual. When a book problem fails, the importer moves on to a shorter ending of the same problem. If no ending passes, the problem doesn't ship. 708 of the 1,218 Red wins produced a problem; the other 510 produced nothing the app would ship. Not all 510 are broken. The same gate also turns away sound problems, such as one a phone would take too long to re-prove, or one already in the corpus as a mirror image. The counts above are the real yield either way.

The Juzhongmi line in the table shows the effect. Of its 181 transcribed positions, the book scores only 42 as Red wins, and five survived. The manual is still in the app: the advanced lesson track teaches from it, alongside the Plum Blossom manual (梅花谱) and the Seven Stars endgame (七星聚会).

## Checked twice, by the same code

MateValidator runs twice: once when a problem is written into the bundle, and again on your device the first time the problems are loaded, before any problem reaches the puzzle database. Both runs use the same Swift source: the authoring tool compiles `MateValidator` and `MateSolver` directly, so the gate that admitted a problem and the gate that loads it can't drift apart.

The second pass is there because a change to the rules engine can quietly break a problem that used to be sound. If that happens, a player should get a smaller corpus, not a board they can't solve. A rejected problem never reaches the database. If an entire shard fails, the loader treats that as a shipping error rather than a content decision and stores none of it. Mate-in-1 and mate-in-3 problems are checked during launch; the deeper two shards are checked in the background. Each problem gets two seconds.

When the validator later gained the twin check along every line, I re-ran all 902 shipped problems through it. None was rejected, and the run took about 1.7 seconds in an optimised build. The test suite proves the whole bundled set again on every run. It's the same idea as [proving Millrace's levels in the test suite](/journal/how-millrace-levels-are-made/): a problem that stops passing should fail by name, not reach a player.

## How the problems reach you

The problems live in **Mate Trail**, one of Xiangqiful's nine drill modules. The hub lists one row per depth, mate in 1, 3, 5 and 7, with how many you've solved in each. A session opens with "Find the mate. Every move must give check." You play Red's moves and the app answers with Black's. Black's replies come from the problem's recorded lines, so the board never stops responding partway through.

Problems you miss come back through spaced repetition. The session header marks a returning problem as "Review — due today", or as "Seen before — no new problems left" once the unseen ones run out. There's no credit line under the board; the source lives on every problem in the data instead.

The first problem a new player sees comes from the books. During setup, before any trial offer, the app asks you to solve the last move of Lanke Shenji #46, a chariot mate with seven pieces on the board.

Mate Trail is separate from the exercises Xiangqiful cuts from your own analysed games. Nobody has screened those positions for a second mate. So when the answer to one of them is a mate in one, the app accepts any mating move instead of insisting on the one it recorded.

The free tier includes three training puzzles a day, and mate problems count toward that. Premium removes the limit for $1.99 a month or $9.99 a year, each with a one-week free trial, or $19.99 once. Everything runs on your device on iPhone, iPad and Mac, with no account. The [app page](/apps/xiangqiful/) has the rest: ten opponents, Pikafish analysis, 80 lessons and more than 150 drills. A Shiqing Yaqu problem from 1570 is in the app only because a solver confirmed what the book says.
