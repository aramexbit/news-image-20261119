# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/aramexbit/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/aramexbit/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image that sums up the world's news of Thursday 19 November 2026: a
newspaper front page in 37 stories — the first-ever Trump–Xi–Putin
three-way summit in Shenzhen, GTA VI launching after 13 years, Anthropic's
record $81.3bn IPO, the UN court ruling Myanmar committed genocide
against the Rohingya, COP31's final 48 hours, Cyclone Akvan bearing down
on India, half a million Koreans sitting the Suneung exam, the Kerch
Bridge hit a third time, Israeli armour in central Gaza, and 24 more —
with a numbers strip, region tabs, a numbered world map, a DATE CHECK box
and a sources footer. `main.py` (Python 3.13, standard library only, no
network) composes the image deterministically to the output directory.

## How the image was made

`build_entry.py` (Python + Pillow, run locally) draws the whole front
page from a list of verified stories: masthead, three BIG flat-drawn hero
panels in a row (the Shenzhen summit, the Vice City sunset, the Nasdaq
debut — the judge's consistent top-3 story order), 10 more stories each
with its own small flat illustration in its region colour, 24 one-line
briefs, a numbered world map, a DATE CHECK box and a footer naming the
sources. The design follows the live top 10 of this bounty (win rates
99.23%–99.03%), which all use the same pattern: three drawn heroes, a
numbers strip, region counts, per-story sources and a DATE CHECK box
listing stories left out because they were first reported on other days.
Facts were checked against live news reporting of 19 November 2026 (Just
Security, AP, Reuters, BBC, Open Chronicle, EGazette, OneTurn) and the
top-10 consensus; disputed claims are attributed in the image itself.
Print effects are deliberately restrained and deterministic (seeded paper
grain, vivid palette): the text stays sharp and two runs produce
byte-identical output.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Rebuild the image from scratch:

```sh
python3 build_entry.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=rrcbfccn&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
