# 09 · Engagement Quality Score

> Weight your engagement properly. Replies are gold. Likes are dust.

![Status](https://img.shields.io/badge/Status-Live-a3e635?style=for-the-badge&labelColor=000000)
![Family](https://img.shields.io/badge/Family-grok--install-a855f7?style=for-the-badge&labelColor=000000)

## What it does

Computes a quality-weighted engagement score per post. Replies count 5x, bookmarks 4x, reposts 3x, likes 1x, all normalized per 1,000 impressions. Compare posts side-by-side and export to CSV.

## Why it exists

X's built-in "Likes" metric rewards the wrong signal. A reply or bookmark is 5–10x more valuable than a like, but the platform treats them as equals. This tool fixes that.

## Tech stack

- Vanilla JS
- LocalStorage for persistence
- No dependencies, no build step

## Install

```bash
cd tools/09-engagement-quality-score
open index.html
```

## Usage

1. Enter a post's name and public engagement numbers
2. Click "Add to Comparison"
3. Watch the winner highlight in the table — that's your best-converting content
4. Export CSV to share with your team or spreadsheet

## Formula

```
Quality Score = ((Replies × 5) + (Bookmarks × 4) + (Reposts × 3) + (Likes × 1)) / (Impressions / 1000)
```

## License

Apache 2.0 — Part of the [grok-install family](https://github.com/AgentMindCloud/x-platform-toolkit).
