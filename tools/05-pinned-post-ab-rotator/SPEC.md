# SPEC · 05 Pinned Post A/B Rotator

## Tagline

Rotate your pinned post on a schedule. Find your best converter.

## Why it exists

Your pinned post is the highest-leverage real estate on your X profile. Every profile visitor reads it first. Most creators set it once and never touch it — leaving compounding conversion gains on the table.

A scheduled rotator + metrics log turns guessing into a four-week experiment: post A for two days, post B for two days, log the impressions and follows each earned, and the winner reveals itself.

## User journey

1. Add 2–5 candidate pinned posts
2. Choose a rotation interval (24h / 48h / 72h / weekly)
3. Mark one candidate "Active" — pin it on X manually
4. When the tool's countdown hits zero, it prompts you to log the last rotation's impressions and follows, then advances to the next candidate
5. The results table sorts candidates by conversion (follows per 1k impressions). Top row is the winner. Keep that one pinned permanently.

## Data sources

- Fully local. All state in `localStorage` under key `xpt-pinned-rotator-v1`.
- No X API calls. You enter impressions and follows manually after each rotation (X's built-in analytics shows these on each post).

## Tech stack

- Single-file `index.html` (vanilla JS + localStorage)
- No build step, no dependencies
- Hostable anywhere static (Hostinger, Netlify, GitHub Pages)

## Data shape

```json
{
  "interval": "24h",
  "candidates": [{ "id": "...", "name": "...", "content": "..." }],
  "activeId": "...",
  "nextSwapAt": 1713600000000,
  "history": [{
    "id": "...",
    "name": "...",
    "content": "...",
    "startedAt": 1713500000000,
    "endedAt": 1713600000000,
    "daysActive": 1.0,
    "impressions": 12400,
    "follows": 9,
    "conversion": 0.73
  }]
}
```

## Interval → milliseconds

- `24h` → 86 400 000
- `48h` → 172 800 000
- `72h` → 259 200 000
- `7d`  → 604 800 000

## Conversion metric

```
conversion = follows * 1000 / impressions
```

Displayed to one decimal place. Rows sort by this descending. Winner row gets `border-left: 3px solid var(--neon-lime)`.

## UI sections

1. **Settings row** — interval dropdown, Export JSON, Import JSON
2. **Candidates** — grid of up to 5 cards with name + content + Set Active + Delete
3. **Active Rotation** — big card with countdown `HH:MM:SS` and `ROTATE NOW` button
4. **Results** — sortable table; top row highlighted lime
5. **Disclaimer** — "This tool tracks and recommends. You manually update your pinned post on X each rotation."

## Estimated build

4–6 hours. The data model and persistence are trivial; the polish is in the countdown animation, the rotation modal UX, and responsive card layout.

## Open questions / risks

- **Browser tab must stay open** for the countdown to tick. A tab-close → reopen reconciles against `Date.now()`, so correctness is fine, just no background notification.
- **No automatic pinning.** X API v2 does not expose a public "pin this tweet" write endpoint. This tool must stay manual — users pin themselves. The UI makes this clear.
- **One user, one device.** No cloud sync in v1. A JSON export/import covers most migration needs.

## Why it isn't LIVE in v0.1.0

The initial-release generation pipeline stream-timed out twice during the `index.html` build. The tool is queued for v0.2.0 so the complete spec can be implemented in a focused pass.
