# 19 · Grok Thread Composer

Category: AI Writing

> Write threads grounded in what's actually happening on X right now.

![Status](https://img.shields.io/badge/Status-Spec'd-52525b?style=for-the-badge&labelColor=000000)
![Family](https://img.shields.io/badge/Family-grok--install-a855f7?style=for-the-badge&labelColor=000000)

## What it does

Takes a topic or angle, asks Grok to read the current X discourse on that topic, and drafts a thread informed by what's trending this hour. You edit the draft in-place and copy the formatted thread to X when ready.

## Why it exists

Grok has native X access — that's xAI's unique advantage. No other LLM knows what is trending on X this hour, which arguments are ascendant, or whose take is getting traction. Threads written with that context feel native to the conversation; threads written without it feel like they were drafted yesterday. This tool puts Grok's live-context advantage directly into the composer.

## Tech stack

- Single-page web app (Vite + React)
- Grok API (xAI) with X-context enabled
- Thin Node proxy on Render to keep API keys server-side
- Tailwind UI with tweet-by-tweet editor

## Install

This tool is currently in the design phase. See [SPEC.md](./SPEC.md) for full implementation plan.

## License

Apache 2.0 — Part of the [grok-install family](https://github.com/AgentMindCloud/x-platform-toolkit).
