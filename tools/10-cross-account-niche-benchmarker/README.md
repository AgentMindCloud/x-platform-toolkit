---
title: "10 · Cross-Account Niche Benchmarker — x-platform-toolkit"
description: "Stop wondering if your numbers are good. See how you stack against your niche."
image: /docs/posters/og-tool-10-cross-account-niche-benchmarker.png
---

# 10 · Cross-Account Niche Benchmarker

Category: Analytics

> Stop wondering if your numbers are good. See how you stack against your niche.

![Status](https://img.shields.io/badge/Status-Spec'd-52525b?style=for-the-badge&labelColor=000000)
![Family](https://img.shields.io/badge/Family-grok--install-a855f7?style=for-the-badge&labelColor=000000)

## What it does

Cross-Account Niche Benchmarker lets you add 5–10 X usernames in your niche and pulls their public metrics alongside yours. It computes your rank and percentile across posting frequency, average likes per post, follower growth rate, and reply rate, then charts the comparison.

## Why it exists

Creators usually evaluate their own numbers in a vacuum. An average of 30 likes per post feels bad until you learn it's the 70th percentile in your specific niche. Conversely, 300 likes feels great until you see the niche median is 800. Without a concrete comparison set, every engagement metric is meaningless. This tool fixes that by letting you define your own cohort and see where you actually sit.

## Tech stack

- Node.js backend on Render
- Firestore cache refreshed weekly
- Dashboard frontend with comparison charts (vanilla JS + Tailwind)
- X API v2 public endpoints
- Hostinger static host for frontend

## Install

This tool is currently in the design phase. See [SPEC.md](./SPEC.md) for full implementation plan.

## License

Apache 2.0 — Part of the [grok-install family](https://github.com/AgentMindCloud/x-platform-toolkit).
