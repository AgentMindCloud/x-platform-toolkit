---
title: "15 · Spaces Recorder + Clips — x-platform-toolkit"
description: "Spaces shouldn't disappear. Record, transcribe, clip — automated."
image: /docs/posters/og-tool-15-spaces-recorder-clips.png
---

# 15 · Spaces Recorder + Clips

Category: Media

> Spaces shouldn't disappear. Record, transcribe, clip — automated.

![Status](https://img.shields.io/badge/Status-Spec'd-52525b?style=for-the-badge&labelColor=000000)
![Family](https://img.shields.io/badge/Family-grok--install-a855f7?style=for-the-badge&labelColor=000000)

## What it does

Captures audio from a live or recently-ended X Space, transcribes it with Whisper, detects high-energy moments (volume spikes, applause, laughter cues, Q&A peaks), and auto-cuts 60-second captioned video clips ready to post back to X as video tweets.

## Why it exists

Spaces produce hours of conversation and then vanish. The best 90 seconds of a 2-hour Space would make a viral clip, but creators rarely go back and edit. Automating the capture-transcribe-clip pipeline converts ephemeral audio into durable, shareable assets — and turns every Space into a week of follow-on content.

## Tech stack

- Node.js orchestration layer
- FFmpeg for audio/video processing and captioning
- yt-dlp or Twspace-dl for Space audio retrieval
- Whisper (local `whisper.cpp` for cost, OpenAI API fallback)
- Python worker for energy-moment detection (librosa)
- S3-compatible storage (R2) for artifacts

## Install

This tool is currently in the design phase. See [SPEC.md](./SPEC.md) for full implementation plan.

## License

Apache 2.0 — Part of the [grok-install family](https://github.com/AgentMindCloud/x-platform-toolkit).
