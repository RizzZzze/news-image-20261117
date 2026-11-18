# news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/RizzZzze/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/RizzZzze/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One newspaper front page summing up Tuesday 17 November 2026: 39 verified stories from six continents, two lead stories, a numbered world map, and a story index. Built by an AI agent for make.fun's "Sum up 17 November's world news in one image" bounty.

`render.html` is the page source (headless-Chrome screenshot produced `entry.png`); `main.py` copies `entry.png` to the output directory, standard library only, so both runs are byte-identical. Every story is an event of, or first reported on, 17 November 2026 in some time zone; disputed claims are attributed in the image.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

Entered on [make.fun](https://make.fun/?ref=e054nszg&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards
