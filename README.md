# Combat Boost — Homepage Rebuild Concept

A multi-page site concept for the combatboost.ai rebuild, built from the
locked rebuild brief (near-black + gold, real client proof, before/after
comparison table, no AI-page-builder patterns, real dedicated pages).

## Structure

Real, separate static pages — no client-side router, no SPA. Each nav
item is a genuine URL with its own `index.html`:

```
/                              Homepage — persuasive core only
/pricing/                      Full pricing/what's-included breakdown
/case-studies/                 Case studies index (story rows)
/case-studies/dan-carey/       Individual case study page
/about/                        Full About page
/faq/                          Full FAQ page
/assets/styles.css             Shared stylesheet, all pages
/assets/nav.js                 Shared mobile-nav toggle script
/assets/images/                Real client screenshots/photos
```

**Why plain multi-page HTML instead of React Router:** the brief asked
for "React Router or equivalent." A client-side SPA router would need a
JS framework, a bundler, and a build step just to produce what a static
host already does natively — and it would work against the site's own
core pitch (search/SEO-driven traffic), since an SPA needs extra work to
make each route crawlable and fast on first load. Plain files at real
paths are simpler, faster, more reliable, and is how every competitor
site referenced in this project (EFC, Monstro, 97Display, New Member
Ninja) actually ships. Every nav link is still a real, distinct,
bookmarkable, crawlable URL — which was the actual requirement.

## Editing

`build.py` is a **local authoring convenience only** — it is not run by
Cloudflare Pages and isn't part of the deployed site. It stitches the
shared header/footer (defined once in `build.py`) around each page's
body content (also in `build.py`) and writes the final, already-static
HTML files straight into the repo. To make a content change:

1. Edit the relevant `build_*()` function in `build.py`, or
   `assets/styles.css` directly for styling.
2. Run `python3 build.py` to regenerate all 6 pages.
3. Commit the regenerated `index.html` files along with `build.py`.

Adding a new individual case-study page (e.g. a second real client
story) means adding one new `build_case_study_<name>()` function
following the `build_case_study_dan_carey()` pattern, and one new
`<div class="story-row">` entry in `build_case_studies_index()` linking
to it — no other page needs to change.

## Deploying to Cloudflare Pages

- **Framework preset:** None
- **Build command:** (leave empty)
- **Build output directory:** `/`

Connect this repo in the Cloudflare Pages dashboard and it deploys the
committed static files as-is.

## Status

This is a **concept for internal review**, not the final production
site — see the banner at the top of every page. Real assets used so far:

- Hero before/after: Clifton Martial Arts Academy's actual live old site
  (cliftonmartialarts.com) vs. the actual Combat Boost rebuild.
- Case-study screenshot: the actual live Striker Lab Muay Thai
  Kickboxing build.
- About-section photo: a real photo from an actual Combat Boost client.
- Video testimonial: real client (Dan Carey, permission granted) — no
  actual video file is embedded yet, just the pull-quotes and a
  placeholder player frame, on both the homepage and his individual
  case-study page.

Still open/placeholder, flagged inline in the pages themselves: client
"logos" in the proof strip are text wordmarks (no real logo files on
hand yet); Moore's Karate and Camal & Cruz's case-study rows are
"coming soon" teasers with no verified per-client results data yet; the
"+9 reactivated" stat is labeled as an illustrative average, not a
verified per-client number.

Flagged, not built, per the brief: a self-serve "Free Website Health
Check" lead-magnet tool (see the HTML comment above the footer in
`build.py`).
