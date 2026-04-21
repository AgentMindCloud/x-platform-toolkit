# SPEC · 10 Cross-Account Niche Benchmarker

## Tagline

Stop wondering if your numbers are good. See how you stack against your niche.

## Why it exists

Every creator spends time wondering whether their numbers are actually good. X gives you absolute metrics — likes, replies, followers — but absolute metrics mean nothing without peers. A tech-founder account with 50 likes per post is performing very differently from a meme account with 50 likes per post, and no platform-provided dashboard accounts for that.

This tool asks the user to nominate a cohort: five to ten accounts they consider peers or role models in the same niche. It then benchmarks the user against that cohort on four dimensions that matter for growth: how often they post, how many likes each post averages, how fast their follower count is changing, and what fraction of their posts are replies rather than originals. The output is a percentile position, not a raw number.

## User journey

1. User signs into the app with X OAuth.
2. User enters 5–10 X usernames representing their niche cohort.
3. Backend fetches public metrics for each cohort member plus the user.
4. Weekly cron refreshes the cache so ranks stay current without burning API budget on every page load.
5. Dashboard shows user's rank and percentile across four axes (posting frequency, average likes per post, follower growth rate, reply-to-original ratio) with bar charts and sparklines.

## Data sources

- X API v2 `GET /2/users/by/username` for resolving handles to IDs and pulling bio and public metrics
- X API v2 `GET /2/users/{id}/tweets` with `max_results=100` and `tweet.fields=public_metrics,created_at` for post metrics over the last 30 days
- Internal Firestore cache keyed by user ID with weekly TTL

## Tech stack

- Node.js + Express backend on Render
- Firebase Firestore for cohort definitions and cached metrics
- Firebase Auth for login
- Vanilla JS + Tailwind + Chart.js dashboard on Hostinger
- GitHub Actions for weekly cohort refresh trigger

## Estimated build

10–12 hours.

## Open questions / risks

- Public metrics do not include impressions, so "posting frequency vs impressions" benchmarks are not possible at the basic tier.
- Users may pick weak cohorts (much larger or much smaller accounts), which invalidates the percentile. UI should warn when size variance exceeds a threshold.
- Follower growth rate requires at least two snapshots; first-time users get a placeholder until the second weekly refresh.
- Private or suspended accounts in a cohort must degrade gracefully.
- Weekly refresh cadence may feel stale to power users; tradeoff vs. API cost needs testing.
