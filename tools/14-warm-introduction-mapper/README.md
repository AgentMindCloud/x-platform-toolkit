# 14 · Warm Introduction Mapper

Category: Network

> Find the shortest follow chain to anyone on X.

![Status](https://img.shields.io/badge/Status-Spec'd-52525b?style=for-the-badge&labelColor=000000)
![Family](https://img.shields.io/badge/Family-grok--install-a855f7?style=for-the-badge&labelColor=000000)

## What it does

Given a target X account, this tool searches your follow graph to find the shortest mutual-follow path (1–3 hops) between you and them. It then drafts an outreach script you can send through each intermediary, turning cold DMs into warm introductions.

## Why it exists

Cold outreach on X is a coin flip. A one-hop warm intro — even just a mutual follower vouching — converts far better than a message from a stranger. The problem is discovery: manually browsing follower lists to find a connection is impossible past a few hundred accounts. This tool automates the graph walk and hands you a path plus the words to use.

## Tech stack

- Node.js backend with BFS graph traversal
- X API v2 for follow-graph queries
- Firestore for aggressive follow-graph caching (24h TTL)
- Grok API for intro-script drafting
- React frontend for path visualization

## Install

This tool is currently in the design phase. See [SPEC.md](./SPEC.md) for full implementation plan.

## License

Apache 2.0 — Part of the [grok-install family](https://github.com/AgentMindCloud/x-platform-toolkit).
