# SPEC · 14 Warm Introduction Mapper

## Tagline

Find the shortest follow chain to anyone on X.

## Why it exists

The gap between a cold DM and a warm introduction is the difference between a 2% and a 30% response rate. But on X, most users cannot see who in their network knows a target account — follower lists are long, private, or paginated across rate-limited endpoints. Creators default to cold outreach because warm paths are invisible, even when they exist.

This tool makes the invisible visible. It walks the follow graph breadth-first from both sides (you and the target), surfaces the shortest bridge, and writes a specific intro-request message naming the target, the shared context, and the ask. What would take hours of manual list-scrolling becomes a 30-second query.

## User journey

1. User connects X account via OAuth 2.0 (scopes: `follows.read`, `users.read`).
2. On first run, the tool backfills the user's direct follows into Firestore (cached 24h).
3. User enters a target X handle or URL.
4. Backend runs bidirectional BFS: expand user's follows and target's followers, meeting in the middle at depth 1, 2, or 3.
5. If a path is found, the UI renders it as a node chain with avatars and bio snippets; if none within 3 hops, the tool returns "no warm path — consider cold outreach" and offers a cold-DM draft instead.
6. User picks a path; Grok drafts a message to the intermediary asking for an intro, personalized with what both sides post about.
7. User copies the script and sends via X DM manually.

## Data sources

- `GET /2/users/{id}/following` (rate limit: 15 requests / 15 min on basic tier)
- `GET /2/users/{id}/followers` (same rate limit)
- `GET /2/users/by/username/{handle}` for target lookup
- Grok API for message drafting using recent posts as personalization

## Tech stack

- Node.js 20 + Fastify backend, hosted on Render
- BullMQ + Redis for queueing paginated follow-graph fetches
- Firestore for persistent cache of edges and node metadata
- React + Cytoscape.js frontend for path visualization
- OAuth 2.0 PKCE flow for X auth

## Estimated build

16–24 hours.

## Open questions / risks

- X API rate limits are the dominant constraint; a 2,000-following account needs 10+ paginated calls just for depth 1. Aggressive caching with stale-while-revalidate is mandatory.
- Best suited for accounts following fewer than 2,000 users; enterprise-tier API access would unlock larger graphs but breaks the toolkit's cost model.
- Follow graphs are asymmetric (you follow someone who does not follow back), so "warm" must be defined as mutual — requires checking both directions per edge.
- Privacy: the tool should never persist other users' follower lists beyond cache TTL, and should not expose them to anyone except the authenticated owner.
- Graph traversal can produce many same-length paths; ranking by intermediary engagement signals (recent mutual interactions) improves the first result.
