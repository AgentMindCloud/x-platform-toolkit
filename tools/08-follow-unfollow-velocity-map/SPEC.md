# SPEC · 08 Follow/Unfollow Velocity Map

## Tagline

Timeline chart of every follow and unfollow, mapped to what you posted.

## Why it exists

Creators react to follower count as if it's a single number, but the signal lives in the derivative. A post that gains you 30 followers and loses you 12 is a different post than one that gains you 42 and loses you zero, even though both read as "plus 30" on the dashboard. Over a month, the pattern of who leaves and who arrives is the clearest feedback X will give you, but it is completely hidden unless you log it yourself.

This tool logs it. It runs a cron, records your follower count, computes the daily delta, and lines it up against the posts you published in the preceding window. The output is a scrubable timeline that answers "which post did that?" in one glance.

## User journey

1. User connects X account with read scope on profile and tweets.
2. Cron job runs at 00:05 UTC daily and records follower count, following count, and a post list for the prior 24 hours.
3. Backend computes net delta since previous snapshot and stores the result.
4. Correlation engine attaches each delta to posts published in the 24 hours prior.
5. Dashboard renders a horizontal timeline: follower count line on top, post markers below, with hover tooltips showing post text, metrics, and delta contribution score.

## Data sources

- X API v2 `GET /2/users/{id}` with `user.fields=public_metrics` for follower and following counts
- X API v2 `GET /2/users/{id}/tweets` with `tweet.fields=public_metrics,created_at` for post timeline
- Optional `GET /2/users/{id}/followers` if user upgrades tier for individual follower churn

## Tech stack

- Node.js + Express backend on Render, background worker for cron
- Firebase Firestore for snapshots (one doc per user per day) and post metadata
- Firebase Auth linked to X for login
- Vanilla JS + Chart.js (or lightweight D3) for timeline UI
- Hostinger static host for frontend

## Estimated build

10–14 hours.

## Open questions / risks

- Basic X API tier exposes only net follower count, not individual follower list. Correlation is therefore to "the set of posts in the 24h window" rather than "the specific post that caused the follow."
- Daily cadence misses intra-day spikes. 6-hour cadence is better but quadruples API cost.
- Correlation is associative not causal; UI must avoid implying otherwise.
- Users joining mid-month have no baseline; first-week charts look noisy.
- Accounts that protect tweets partway through the tracking window break the post-fetch step.
