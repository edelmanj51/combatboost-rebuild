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

### Redacting a new calendar screenshot before adding it

Every calendar screenshot on the Results page has been redacted with a
consistent ImageMagick recipe: crop out the left nav sidebar, then
pixelate everything below the day-of-week header row (leaves the school
name/date/weekday labels crisp, makes every appointment name illegible).
The always-run recipe, given a raw GHL calendar screenshot of width W
and height H:

```
convert raw.png \
  \( -clone 0 -crop $((W-170))x$((H-155))+170+155 +repage -scale 6% -scale 1667% \) \
  -geometry +170+155 -compose over -composite \
  -crop ${W}x${H}+170+0 +repage \
  redacted.png
```

Raw, unredacted originals live in `raw-drive-assets/` locally (never
committed — see `.gitignore`) alongside this exact pipeline; run it on
a new screenshot, drop the result into `assets/images/results/`, and add
one entry to `CALENDAR_ITEMS` in `build.py` per the pattern above.

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
  alongside it. **Note:** Vimeo's privacy settings only allow this embed
  to render on whitelisted domains — it renders blank on `localhost`
  during local preview; add the production domain in Vimeo's own embed
  settings once deployed.
- Results page — all 13 calendar screenshots, the Site Performance
  before/after, the Google Maps heatmap, all 4 growth-over-time charts,
  and the client text message are now real, pulled from the client's
  Drive folder (redacted per the recipe above where needed). Only 1 real
  testimonial (Dan Carey's) exists — the Drive folder contained one
  client-text screenshot, not the 3 separate additional written
  testimonials the original brief described, so no other testimonial
  slots were fabricated to fill that gap.
- A few stats were corrected against what the actual screenshots show,
  rather than kept as the brief's approximate paraphrase: the PageSpeed
  image shows *Mobile* scores (31→99), not Desktop; the reviews-over-time
  chart peaks at 46 total in 2026 (not a clean "before→after" — the
  underlying series isn't monotonic); the two contract-signing charts
  peak at 17 and 18 respectively (not a single "15→20").

Flagged, not built, per the brief: a self-serve "Free Website Health
Check" lead-magnet tool (see the HTML comment above the footer in
`build.py`).
