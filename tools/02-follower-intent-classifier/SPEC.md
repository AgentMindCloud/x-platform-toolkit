# SPEC · 02 Follower Intent Classifier

## Tagline

Stop counting followers. Start understanding why they followed you.

## Why it exists

Creators optimize for follower count because it's the only signal the platform surfaces cleanly. But 1,000 followers where 200 are buyers, 500 are silent lurkers, 300 are competitors, and a handful are bots is a completely different asset than 1,000 followers where half are scrapers. Knowing the mix changes your posting strategy, your product pricing, and whether you even need to keep growing.

This tool reads each follower's public footprint and assigns a behavioral tag. The result is a CRM-style dashboard that lets you target segments explicitly rather than blast everyone and hope.

## User journey

1. User connects X account with read-only scope.
2. Backend paginates through `/users/{id}/followers`, storing each follower ID in Firestore.
3. For each follower the tool fetches bio and last 50 posts, then runs a classifier.
4. Classifier assigns one of five tags: Buyers (mentions pricing, "looking for", "recommend me"), Lurkers (low post volume, high follow count, low reply rate), Amplifiers (high reply or repost rate on your content), Competitors (bio and posts overlap with your niche keywords), Bots (account age under 90 days, follow count greater than 5,000, formulaic post patterns).
5. Dashboard shows segment distribution, trend over time, and CSV export per segment.

## Data sources

- X API v2 `GET /2/users/{id}/followers` with `user.fields=description,public_metrics,created_at`
- X API v2 `GET /2/users/{id}/tweets` for follower post samples
- Optional Grok API for borderline classifications

## Tech stack

- Node.js worker with bull queue for paginated batching
- Firebase Firestore for follower documents and segment aggregates
- Local rule-based classifier as first pass, Grok API as second pass for ambiguous cases
- Dashboard: vanilla JS + Tailwind, deployed on Hostinger
- Worker hosted on Render background worker tier

## Estimated build

12–16 hours.

## Open questions / risks

- X API rate limits cap follower endpoint at 15 requests per 15 minutes on most tiers. A 10,000-follower account takes hours to scan fully and must resume gracefully across cron runs.
- Bot detection is fuzzy. False positives will annoy users. Need a confidence score and a manual override.
- Niche keyword extraction for Competitors segment may require an initial user-provided seed list.
- Follower list can shift mid-scan; reconciliation logic needs to handle deletions and fresh follows.
- Grok API cost per classification needs to be capped per user per month.
