# 18 · Emotional Tone Trend Tracker

Category: Analytics

> What's the emotional fingerprint of your X account?

![Status](https://img.shields.io/badge/Status-Live-a3e635?style=for-the-badge&labelColor=000000)
![Family](https://img.shields.io/badge/Family-grok--install-a855f7?style=for-the-badge&labelColor=000000)

## What it does

Analyzes a batch of your posts and classifies each into one of seven tones: hopeful, cynical, curious, angry, inspiring, analytical, playful. Produces a donut of your tonal distribution, a per-post line chart, and three plain-English insights.

## Why it exists

Most creators don't know their own voice. They think they're inspiring but read as cynical. They think they're curious but read as angry. This tool shows you the signal.

## Tech stack

- Vanilla JS
- Chart.js (CDN)
- No build step, no backend

## Install

```bash
cd tools/18-emotional-tone-trend-tracker
open index.html
```

## Usage

1. Paste 10–50 of your recent posts, one per line
2. Click Analyze
3. Read the insights. Share the donut if it's flattering.

## Method

Each post's words are scored against curated marker-word lists per tone, normalized by post length. Dominant tone = top score. Confidence = margin between top 1 and 2. Ties (<10% gap) are labeled "Mixed".

## License

Apache 2.0 — Part of the [grok-install family](https://github.com/AgentMindCloud/x-platform-toolkit).
