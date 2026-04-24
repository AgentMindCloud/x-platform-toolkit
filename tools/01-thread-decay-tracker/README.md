# 01 · Thread Decay Tracker

Category: Analytics

> See which of your threads are still earning impressions days after you posted them.

![Status](https://img.shields.io/badge/Status-Spec'd-52525b?style=for-the-badge&labelColor=000000)
![Family](https://img.shields.io/badge/Family-grok--install-a855f7?style=for-the-badge&labelColor=000000)

## What it does

Thread Decay Tracker polls the X API for each of your recent threads and charts how impressions accumulate over days, not minutes. It flags slow-burn threads that are still compounding days after posting and surfaces the exact window where a repost would catch the second wave.

## Why it exists

X's native analytics shows peak engagement on day one and then goes dark. That hides the most valuable threads on the platform: ones that quietly pick up impressions on day three, four, or five as the algorithm keeps surfacing them in search and recommendations. Without external polling you can't tell a dying thread from a climbing one, which means you either repost too early, too late, or not at all. This tool gives you the curve.

## Tech stack

- Node.js + Express backend on Render
- Cron polling every 12 hours
- Firebase Firestore for time-series storage
- Vanilla JS frontend hosted on Hostinger
- X API v2 OAuth 2.0 user context

## Install

This tool is currently in the design phase. See [SPEC.md](./SPEC.md) for full implementation plan.

## License

Apache 2.0 — Part of the [grok-install family](https://github.com/AgentMindCloud/x-platform-toolkit).
