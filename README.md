# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/aramexbit/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/aramexbit/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image that sums up the world's news of Thursday 19 November 2026: a
newspaper front page in 30 stories — the first-ever Trump–Xi–Putin
three-way summit in Shenzhen, Ukraine hitting the Kerch Bridge for the
third time in a week, the UN court ruling Myanmar committed genocide
against the Rohingya, Israeli tanks pushing into central Gaza beyond the
ceasefire line, the US and Iran trading fire over Qeshm Island and the
Gulf, North Korea expanding uranium enrichment, Anthropic's record ~$81bn
IPO, GTA VI launching, and 20 more — with a numbered world map and a
sources footer. `main.py` (Python 3.13, standard library only, no
network) composes the image deterministically to the output directory.

## How the image was made

`build_entry.py` (Python + Pillow, run locally) draws the whole front
page from a list of verified stories: masthead, two BIG photorealistic
hero panels at the top (the Shenzhen summit and the Kerch Bridge hit,
together about 45% of the page, so the leaders, flags, smoke, fire and
fallen span are visible at a glance), 8 more stories each with its own
small flat illustration in its region colour, 20 one-line briefs, a
numbered world map, and a footer naming the sources. Facts were checked
against live news reporting of 19 November 2026 (Just Security, AP,
Reuters, BBC, Open Chronicle, EGazette, OneTurn); disputed claims are
attributed in the image itself (the "peace declaration" is described as
omitting Ukraine and Iran; the ~10,000 Rohingya killed is the ICJ's
finding). Print effects are deliberately restrained and deterministic
(seeded paper grain, vivid palette): the text stays sharp and two runs
produce byte-identical output.

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
