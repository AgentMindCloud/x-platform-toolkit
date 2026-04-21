# SPEC · 01 Thread Decay Tracker

## Tagline

See which of your threads are still earning impressions days after you posted them.

## Why it exists

X's built-in analytics treats every post like it lives and dies in the first 24 hours. In reality, a meaningful fraction of threads keep accumulating impressions for three to seven days as they get pulled into search results, bookmarks, and the For You feed. Creators who can see that curve know when to repost, when to pin, and when to fold a thread into a follow-up.

Without external tooling there is no way to observe the curve. You see a number at the top of the page and you have to guess whether it's still climbing. This tool removes the guessing by polling public metrics on a schedule and charting the result.

## User journey

1. User signs in with X OAuth 2.0 and grants read scope on tweets and metrics.
2. Backend fetches the user's last 90 days of posts, filtering for threads (self-reply chains).
3. A cron job polls public metrics for each tracked thread every 12 hours and writes a time-series row to Firestore.
4. Dashboard charts each thread's daily impression curve with a "still active" flag when the last 24h of impressions exceed 10% of cumulative total.
5. Tool ranks threads by predicted remaining lift and suggests optimal repost or quote-tweet windows.

## Data sources

- X API v2 `GET /2/users/{id}/tweets` with `tweet.fields=public_metrics,conversation_id,created_at`
- X API v2 `GET /2/tweets/{id}` for per-thread polling
- OAuth 2.0 Authorization Code with PKCE

## Tech stack

- Node.js + Express backend on Render (web service plus cron worker)
- Firebase Firestore for per-thread time-series documents
- Firebase Auth (linked to X) for session management
- Vanilla JS + Chart.js frontend hosted on Hostinger
- GitHub Actions for CI

## Estimated build

8–12 hours.

## Open questions / risks

- Basic tier of X API may not return impression counts; `non_public_metrics` requires OAuth 2.0 user context and is rate-limited. Need to confirm which tier unlocks what.
- Polling cost scales linearly with tracked threads; a 12h cadence on 200 threads is 400 reads per day per user.
- Firestore document size caps at 1 MB; long-running time-series may need sharding by month.
- Determining "thread" boundaries is fuzzy when users edit or delete replies mid-chain.
- Free-tier Render cron has a cold-start window that may drift polling times by several minutes.
