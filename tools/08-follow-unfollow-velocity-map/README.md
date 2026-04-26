---
title: "08 · Follow/Unfollow Velocity Map — x-platform-toolkit"
description: "Timeline chart of every follow and unfollow, mapped to what you posted."
image: /docs/posters/og-tool-08-follow-unfollow-velocity-map.png
---

# 08 · Follow/Unfollow Velocity Map

Category: Analytics

> Timeline chart of every follow and unfollow, mapped to what you posted.

![Status](https://img.shields.io/badge/Status-Spec'd-52525b?style=for-the-badge&labelColor=000000)
![Family](https://img.shields.io/badge/Family-grok--install-a855f7?style=for-the-badge&labelColor=000000)

## What it does

Follow/Unfollow Velocity Map records your follower count on a daily cadence, detects net deltas, and overlays them onto a timeline of your posts. Hover over a dip or a spike to see exactly which posts went out in the 24 hours before the change.

## Why it exists

The raw follower number doesn't teach you anything. The delta paired with a specific post does. When you lose followers after a spicy take or gain them after a sleeper thread, you need to know which post caused it so you can repeat the pattern or stop the bleeding. This tool turns the invisible feedback loop into a visible timeline.

## Tech stack

- Node.js backend with cron running on Render
- Firestore for daily follower-count snapshots and post metadata
- Vanilla JS + D3 or Chart.js dashboard frontend
- Hostinger static host for frontend
- X API v2 user context OAuth

## Install

This tool is currently in the design phase. See [SPEC.md](./SPEC.md) for full implementation plan.

## License

Apache 2.0 — Part of the [grok-install family](https://github.com/AgentMindCloud/x-platform-toolkit).
