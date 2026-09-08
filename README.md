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
/results/                      Results — aggregate proof, one page
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

**Why /results is one page, not an index + sub-pages** (unlike the
earlier /case-studies draft): there are no individual client story arcs
to tell yet — what exists is aggregate proof (calendars, search-ranking
before/afters, PageSpeed before/afters, growth charts, testimonials).
Renamed and restructured per direction to match that reality.

## Editing

`build.py` is a **local authoring convenience only** — it is not run by
Cloudflare Pages and isn't part of the deployed site. It stitches the
shared header/footer (defined once in `build.py`) around each page's
body content (also in `build.py`) and writes the final, already-static
HTML files straight into the repo. To make a content change:

1. Edit the relevant `build_*()` function in `build.py`, or
   `assets/styles.css` directly for styling.
2. Run `python3 build.py` to regenerate all pages.
3. Commit the regenerated `index.html` files along with `build.py`.

### Adding a new Results proof item (this page will keep growing)

The Results page is entirely data-driven — no page markup needs to
change to add a new item:

- **A new calendar screenshot:** add one entry to the `CALENDAR_ITEMS`
  list near the top of `build.py` — `{"school": "...", "badge": "...",
  "img": "/assets/images/....jpg", "featured": True or False}`.
  `featured: True` shows it in the main grid; `False` puts it behind the
  "See more" expand.
- **A new written or video testimonial:** add one entry to the
  `TESTIMONIALS` list the same way.
- **A new Site Performance / Search Visibility / Growth stat or chart:**
  these are currently hand-written in `build_results()` since each is a
  one-off named metric (not a repeating list like calendars) — copy the
  existing `.stat-compare-item` or `.proof-pending` block pattern for a
  new one.

Then run `python3 build.py` and commit.

### Once Google Drive access is connected

Every screenshot referenced in the brief (12 calendar shots, the
PageSpeed before/after, the Google Maps heatmap, the growth charts, the
client text message, and 3 of the 4 written/video testimonials) is
still a labeled placeholder — Drive wasn't authenticated in the session
that built this. To finish the page:

1. Pull the real files from the Drive folder, redact any visible
   student names/personal info in the calendar screenshots (school names
   are fine to show), and drop them into `assets/images/`.
2. In `build.py`, change each relevant `"img": None` to the real file
   path in `CALENDAR_ITEMS`, and swap the `proof-pending` placeholder
   `<div>`s in `build_results()` for real `<img>` tags for the
   Performance/Visibility/Growth screenshots.
3. Transcribe the real text-message screenshot's content into the
   `.text-bubble` in `build_results()`, and the 3 additional written
   testimonials' real quotes into `TESTIMONIALS`.
4. Run `python3 build.py` and commit.

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
- About-section photo: a real photo from an actual Combat Boost client.
- Results page video: a real, working Vimeo embed of Dan Carey's
  testimonial (permission granted), with his real pull-quotes as text
  alongside it.

**Blocked on Google Drive access** (not authenticated this session —
run `/mcp` and connect "claude.ai Google Drive" to unblock): all 12
calendar screenshots, the Site Performance before/after image, the
Google Maps heatmap image, the 3 growth-over-time charts, the client
text-message screenshot's actual content, and 3 of the 4
written/video testimonials' actual quotes. Every one of these is a
clearly labeled "pending" placeholder on the live page right now, not
invented content — see "Once Google Drive access is connected" above
for exactly how to finish each one.

The real numbers you provided *were* used as actual stat text on the
page already (not blocked on Drive, since they were given directly):
mobile load 6.9s → 1.0s, desktop PageSpeed 30s → 96–99, Google reviews
58 → 103, active contracts 15 → 20.

Flagged, not built, per the brief: a self-serve "Free Website Health
Check" lead-magnet tool (see the HTML comment above the footer in
`build.py`).
