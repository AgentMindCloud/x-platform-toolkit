# Changelog

All notable changes to `x-platform-toolkit` are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/).

## [0.2.0] — 2026-05-07

### Removed

- Retired 8 tool folders during portfolio cleanup. The remaining 12 are the focused, shippable set:
  - 01 Thread Decay Tracker
  - 02 Follower Intent Classifier
  - 08 Follow/Unfollow Velocity Map
  - 09 Engagement Quality Score
  - 10 Cross-Account Niche Benchmarker
  - 14 Warm Introduction Mapper
  - 15 Spaces Recorder + Clips
  - 18 Emotional Tone Trend Tracker

### Changed

- README, CHANGELOG, ROADMAP, tokens, and the CI categorization assertion now reflect the 12-tool surface (4 Live, 8 Spec'd).
- Added `MERGE_PLAN.md` documenting the planned fold into `grok-agent OS / Tools tab` in Tier 3.

## [0.1.0] — 2026-04-21

### Added

- Initial repo scaffold with brand identity (grok-install family)
- 6 LIVE tools shipped (vanilla JS, single-file):
  - 04 Pre-Post Virality Scorer
  - 05 Pinned Post A/B Rotator
  - 07 Content Compound Calculator
  - 09 Engagement Quality Score (later retired in 0.2.0)
  - 12 Controversy Detector
  - 18 Emotional Tone Trend Tracker (later retired in 0.2.0)
- 14 SPEC'D tools with detailed implementation plans
- Shared UI kit (tokens, components, shell template)
- Shared X API v2 wrapper (`@x-platform-toolkit/x-api-client`)
- Shared xAI Grok API wrapper (`@x-platform-toolkit/grok-client`)
- Documentation: PHILOSOPHY, ARCHITECTURE, BRAND, ROADMAP
- Contributing guide, Code of Conduct, issue templates

### Notes

- Tool 12 (Controversy Detector) ships with empty default keyword lists. Users add their own niche-specific risk vocabulary via the in-UI "Edit keywords" control, which persists locally. The tool's value is the scoring framework and highlight UI, not a baked-in glossary — every niche has different risk vocabulary.

---

Part of the [grok-install family](https://github.com/AgentMindCloud/x-platform-toolkit). Apache 2.0.
