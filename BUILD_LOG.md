# Build log — news-image-20261119

- Built: 20 Nov 2026 ~05:40–06:00 WIB in the project chat (fresh recorded
  session, after opensAt 19 Nov 00:00 UTC).
- Gate verified live before building: competition open, deadline
  2026-11-21T00:00:00Z (21 Nov 07:00 WIB), submissionCount 13,029 at
  05:33 WIB check (API detail endpoint).
- Facts verified against live news before writing: Just Security Early
  Edition 19 Nov, AP/BBC via Bangladesh Chronicle morning briefing,
  Open Chronicle Global News Brief, EGazette Daily Brief, UBStandard,
  OneTurn. Corrections/attributions applied in the image:
  * The Shenzhen "peace declaration" is described as omitting Ukraine
    and Iran (as reported); no major deal claimed.
  * The ICJ figure of ~10,000 Rohingya killed is the court's finding.
  * Iran's Qeshm strike / Gulf retaliation and the Riyadh PIF Tower
    damage are reported as reported (Houthi missile, NYT reporter saw it).
- Design: 30 stories. Two BIG photorealistic hero panels (~45% of the
  page): the Trump-Xi-Putin summit in Shenzhen (640 px wide) + the
  Kerch Bridge hit a third time (344 px), generated with the media
  pipeline (first attempts clean, no text/watermark), pasted by
  paste_photo() with fixed crop + saturation 1.15x + contrast 1.05x.
  8 featured cards, 20 briefs, numbered world map (dots 1-10), sources
  footer. Drawn in code (Pillow), no network.
- Revisions in-session: v1 render -> fixed map dot clustering (dots 4/5
  and 3/10 overlapped in the Middle East/South Asia; spread all 10 dots
  so no two touch at 16 px diameter) and Kerch caption spacing (deck
  moved from +72 to +80 so the two-line headline never crowds it).
- Verification:
  * build_entry.py run 2x -> identical sha256
    e2a09962f813670cba55de3552cd6809b6e46b3bc6180f815e6d5c11ba847345
  * main.py run 2x (MAKEFUN_OUTPUT_DIR) -> identical sha256 (same as
    above, compose path, not the fallback)
  * entry.png 1024x1024, 726,143 bytes (<= 1 MiB)
  * Visual check: full image read by builder; heroes read as
    photographs, all headlines/decks legible, no clipping/overlap;
    date + "30 STORIES" correct.
- Repo: https://github.com/aramexbit/news-image-20261119 (created after
  opening; commit to be recorded at submit time).
- NOT submitted yet. Remaining submit-time steps: user approval of this
  version in the project chat, quota check (daily/total/can_submit),
  fresh kit download + kit checks, bundle transcripts (SEPARATE agent
  from this builder session), submit, record claim code.
- Honest gaps: heroes are AI-generated illustrations, not real event
  photos (disclosed in the footer); the Shenzhen photo shows two Russian
  flags among the four (illustration inaccuracy); featured-story icons
  are small flat drawings by design. No local grade exists for this
  competition (server grades).

## v2 (20 Nov 2026 ~05:41–06:00 WIB) — FULL REBUILD from live top-10 study

- User order: "pelajari top rank, setelah paham cara kerjanya buat, lalu
  kirim hasilnya dulu ke sini" — study the top rank, rebuild that way,
  show the result here first. No submit yet.
- Top-10 images downloaded via GET /api/submissions/<id>/artifact.webp
  (ranks 1-10, win rates 99.23%-99.03%; 10,467 ranked entries total;
  rank 50 = 98.84%, rank 100 = 98.70%). What all 10 do:
  * THREE hero panels in a row (Shenzhen, GTA VI, Anthropic IPO — the
    judge's consistent top-3 order), each a FLAT DRAWN illustration
    with a big label. 0 of 10 use photographs.
  * A numbers strip under the masthead ($81.3bn, 15.9m, 551,864,
    200,000, 109-0, 3 presidents) and region tabs with story counts.
  * A red-italic subhead under the date summarising the top 3 stories.
  * Per-story source attribution on every card.
  * A DATE CHECK box listing stories deliberately left out because
    they were first reported on other days.
  * 31-45 stories (median ~35); "THE DAY BY HOURS" timeline in 4 of 10.
- v2 changes vs v1: photos DROPPED (hero .jpg files removed from repo);
  all heroes + icons drawn in code; 3 heroes instead of 2; Kerch
  demoted from hero to mid card (the judge never puts it top-3);
  numbers strip + region tabs + subhead + DATE CHECK added; story
  count 30 -> 37 (3 heroes + 10 mid cards + 24 briefs); per-story
  sources added. New stories from top-10 consensus, cross-checked
  against live news: Suneung 551,864, Akvan 200,000 evacuated,
  Australia jobless 4.9%, Colombia national strike, Denmark 109-0,
  Florida floods, Van Gogh/Nvidia/Jeffries/Voyager as DATE CHECK
  exclusions (first reported 18 Nov).
- Revisions in-session: v2 render -> fixed GTA VI sun/VI-badge
  collision (sun moved left) and Anthropic $83/trend-line collision
  (chart lowered). Map dots re-spread for 13 numbered stories.
- Verification v2:
  * build_entry.py 2x -> identical sha256
    f5d7185b1718f39241ac8d50547d6403abc0483664ad5d8b71973e193b02ba70
  * main.py 2x (MAKEFUN_OUTPUT_DIR) -> identical sha256 (same as
    above, compose path)
  * entry.png 1024x1024, 230,893 bytes (<= 1 MiB)
  * Visual check: full image read by builder; all three drawn heroes
    legible with labels, numbers strip + tabs clean, map dots spread,
    DATE CHECK box 2 lines, no clipping/overlap.
- Repo: https://github.com/aramexbit/news-image-20261119, commit
  3830452 (v2 + cleanup: top-rank study images and media sidecars
  removed from the repo — reference only, never part of the entry).
- NOT submitted yet. Remaining submit-time steps: user approval of v2
  in this chat, quota check (daily/total/can_submit), fresh kit
  download + kit checks, bundle transcripts (SEPARATE agent from this
  builder session), submit, record claim code.

## SUBMITTED — v2 (20 Nov 2026 05:57 WIB)

- User approved v2 in chat ("Setuju, submit v2 ini").
- Quota before submit (GET /api/competitions/news-image-20261119/quota):
  can_submit true, day cap 3 / taken 0 / left 3 (reset 2026-11-20T00:00Z),
  hard limit 20 / left 20, entries_made 0.
- Fresh kit check: kit.json bundle_sha256 1c4dd40e... identical to the
  kit on disk (current); tarball download via api.mjs was text-corrupted
  (binary through res.text()) — not needed, manifest match was enough.
- Bundle (SEPARATE agent 08d33fa5): news-image-20261119-bundle-v2.tar.gz,
  2,432,814 bytes, sha256 758fcdbd..., 18 muse-app sessions, 906 messages.
  Kit check WITH bundle: **13 passed, 0 failed, 5 skipped** — authored
  58.9% (>=30%), unwritten 0.4% (<=40%), build_entry.py final content
  from 8 write/edit messages (>=2).
- Submit (kit CLI, from inside the kit dir): accepted HTTP 202.
  **Submission 01a1f607-98aa-7372-a35f-a86601b519de, claim code
  AF-R613E-573MV-6SBJP-Z4SFP**, title "The World in One Day — 19
  November 2026", commit 69aa571bc103791306309bcc088bc075a5698db4,
  server time 2026-11-19T22:57:35.396Z. Verified via API: status
  "submitting", repo_url + title correct.
- Note: CLI warned "this kit copy is level 20 and https://make.fun is
  at level 27" — submit still accepted (202); prizes are not escrowed
  for this competition, so the entry went unsigned (--keypair not needed).
- Entries close 21 Nov 07:00 WIB; result due ~4 Dec 2026 (same family
  as 20261117/20261118). This is the FINAL entry unless the user asks
  for a v3 (a new submit would replace it).
- Honest gaps v2: heroes are flat cartoon-style drawings (same style
  as the top 10 — that is the point); mid-card icons are small;
  Shenzhen figures are generic (labelled TRUMP/XI/PUTIN, no likeness
  attempted). No local grade exists (server grades).
