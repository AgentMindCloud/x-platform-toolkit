# Changelog

All notable changes to `x-platform-toolkit` are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/).

## [0.1.0] — 2026-04-21

### Added

- Initial repo scaffold with brand identity (grok-install family)
- 4 LIVE tools shipped (vanilla JS, single-file):
  - 04 Pre-Post Virality Scorer
  - 07 Content Compound Calculator
  - 09 Engagement Quality Score
  - 18 Emotional Tone Trend Tracker
- 15 SPEC'D tools with detailed implementation plans
- Shared UI kit (tokens, components, shell template)
- Shared X API v2 wrapper (`@x-platform-toolkit/x-api-client`)
- Shared xAI Grok API wrapper (`@x-platform-toolkit/grok-client`)
- Documentation: PHILOSOPHY, ARCHITECTURE, BRAND, ROADMAP
- Contributing guide, Code of Conduct, issue templates

### Notes

- Tool 12 (Controversy Detector) was excluded from this release. Its scope requires inlining politically-charged keyword lists, which is better handled outside a general-purpose open source tool. Numbering is preserved (01–11, 13–20); folder 12 is intentionally absent.
- Tool 05 (Pinned Post A/B Rotator) is spec'd but not yet live — its initial implementation is queued for v0.2.0. See [tools/05-pinned-post-ab-rotator/SPEC.md](tools/05-pinned-post-ab-rotator/SPEC.md).

---

Part of the [grok-install family](https://github.com/AgentMindCloud/x-platform-toolkit). Apache 2.0.
