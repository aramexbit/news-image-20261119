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
