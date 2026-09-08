# Combat Boost — Homepage Rebuild Concept

A homepage concept for the combatboost.ai rebuild, built from the locked
rebuild brief (near-black + gold, real client proof, before/after
comparison table, no AI-page-builder patterns).

This is a single static HTML file — no build step, no framework, no
dependencies. All images (the real before/after client screenshots, the
case-study screenshot, the client photo) are inlined as base64 data URIs
directly in `index.html`, so the whole site is one file.

## Deploying to Cloudflare Pages

- **Framework preset:** None
- **Build command:** (leave empty)
- **Build output directory:** `/`

That's it — connect this repo in the Cloudflare Pages dashboard and it
deploys as-is.

## Status

This is a **concept for internal review**, not the final production site —
see the banner at the top of the page. Real assets used so far:

- Hero before/after: Clifton Martial Arts Academy's actual live old site
  (cliftonmartialarts.com) vs. the actual Combat Boost rebuild.
- Case-study screenshot: the actual live Striker Lab Muay Thai Kickboxing
  build.
- About-section photo: a real photo from an actual Combat Boost client.
- Video testimonial: real client (Dan Carey, permission granted) — no
  actual video file is embedded yet, just the pull-quotes and a
  placeholder player frame.

Still open/placeholder, flagged inline in the page's own build history:
client "logos" are text wordmarks (no real logo files on hand), and the
case-study write-ups are teasers only (no verified per-client results data
yet).
