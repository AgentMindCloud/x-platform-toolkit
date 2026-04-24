# 02 · Follower Intent Classifier

Category: Analytics

> Stop counting followers. Start understanding why they followed you.

![Status](https://img.shields.io/badge/Status-Spec'd-52525b?style=for-the-badge&labelColor=000000)
![Family](https://img.shields.io/badge/Family-grok--install-a855f7?style=for-the-badge&labelColor=000000)

## What it does

Follower Intent Classifier pulls your full follower list, analyzes each follower's bio and recent posts, and sorts them into five behavioral segments: buyers, lurkers, amplifiers, competitors, and bots. The output is a dashboard plus exportable lists you can target with pinned posts, DMs, or product drops.

## Why it exists

A follower count is a vanity number. It doesn't tell you whether those people will buy, share, stay silent, or scrape your posts for their own niche. Creators who understand the composition of their audience write different hooks, price differently, and reply differently. This tool turns an opaque follower list into a segmented CRM so you can stop writing for a ghost.

## Tech stack

- Node.js backend
- Classification via local heuristics first, Grok API second pass
- Firebase Firestore cache keyed by follower ID
- Dashboard UI (vanilla JS + Tailwind)
- Hosted on Render + Hostinger

## Install

This tool is currently in the design phase. See [SPEC.md](./SPEC.md) for full implementation plan.

## License

Apache 2.0 — Part of the [grok-install family](https://github.com/AgentMindCloud/x-platform-toolkit).
