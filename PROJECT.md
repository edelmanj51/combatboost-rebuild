# Combat Boost Rebuild — Project Reference

**Read this file in full before making any design or copy change to this
repo.** It exists so no future session has to be re-briefed on locked facts,
positioning, or the visual system from scratch. If a request conflicts with
anything below, flag the conflict before proceeding — do not silently
override anything marked locked.

---

## Business Facts (locked, real, verified — never deviate)

- Combat Boost is an AI marketing agency working **exclusively** with
  martial arts schools. Flat pricing: **$297/month**. Legal entity: **JPE
  Enterprises** (site footer reads "JPE Enterprises LLC, DBA Combat Boost").
- **Six confirmed stats — the only numbers/timeframes used anywhere on the
  site:**
  - **"50+ Schools Worked With"** (51 real schools served). Never
    substitute any other school-count number.
  - **"50,000+ Lead Conversations"** — conversations handled with leads,
    not a claim about leads acquired or ad spend. Do not blur this
    distinction in copy.
  - **"48-Hour Launch"** — confirmed real average/typical kickoff-to-live
    turnaround. The earlier "72 hours" figure and any "a few weeks"
    phrasing are both superseded — never use either.
  - **"No Long-Term Contracts"** — real, qualitative. State it plainly and
    directly everywhere it appears (Comparison table, FAQ, Pricing) — do
    not hedge this into "we'll cover it on the call" language.
  - **"Zero Ad Spend Required"** — the core system works without paid
    ads; ads are a separately-quoted add-on, never the starting point.
  - **"30-Day Money-Back Guarantee"** — confirmed real, active policy
    (added Sep 2026). Safe to state confidently on the Pricing page.
  Do not use any number, timeframe, or claim beyond these six anywhere on
  the site.
- **6 named client logos**, in this exact order: Premier Martial Arts, ATA
  (American Taekwondo Association), Moore's Karate, Ahn's Taekwondo Academy,
  Camal and Cruz Judo & BJJ, Striker Lab Muay Thai Kickboxing.
- **1 real video testimonial** (Dan Carey, Vimeo — embed URL
  `https://player.vimeo.com/video/1224788450?h=171cc92b25`; renders blank on
  `localhost` due to Vimeo's domain whitelist, works on whitelisted
  production domains). **1 real written pull-quote**, same person. Do not
  fabricate additional testimonials, star ratings, or a review-aggregate
  number — none exist beyond this one.
- Real proof assets on hand: ~13 GHL calendar screenshots across 9 schools
  (student info redacted, school names real); 1 PageSpeed before/after —
  **single school**, 6.9s→1.0s load, 31→99 mobile score; 1 reviews
  before/after — **single school** (Up Top Martial Arts Academy), 58→103
  reviews; 2 contract-signing growth charts; 1 web-traffic chart; 1 client
  text-message screenshot. **Single-school metrics belong on the Results
  page, attached to their specific school — never presented as a
  company-wide average or typical result.**
- **Reactivation math** (real, calculable, safe as a worked example):
  campaigns typically recover **2–4%** of a school's existing dead-lead /
  inactive-member database. A list of 500 typically returns 10–20 booked
  appointments; a list of 1,000 typically returns 20–40 — no added ad
  spend. Always frame with "typically," never as a guarantee.
- **Photography limitation**: very little real photography of clients or
  physical schools exists. Do not build layouts that depend on large
  real-photo treatments carrying visual weight. Reserve actual photography
  for the Results page, where the real assets already live.
- **Pricing history note**: earlier rounds of this project deliberately
  hid the $297/mo number on both the homepage and `/pricing` itself
  ("we don't publish a number here"). That decision was reversed (Sep
  2026) — `/pricing` now states $297/month plainly and confidently in its
  own headline/subhead. The homepage still never shows the number (its
  CTAs stay "Book a Strategy Call," not a price) — that split is
  intentional, not an oversight. Do not add a pricing-gated lead form
  without an explicit, separate request — that's future work requiring
  form/backend handling outside this repo's current static-HTML,
  no-interactivity scope.
- **Real logo asset**: pulled directly from the live production site
  (combatboost.ai) rather than redrawn. Full lockup (mark + wordmark) saved
  locally at `/tmp/logo-cropped.png` during extraction; the icon mark alone
  (figure + upward arrow + growth-chart frame, black + brand blue,
  transparent background) lives in the repo at
  `assets/images/logo-mark.png`. The wordmark text ("CombatBoost.ai") stays
  live HTML/CSS type in `build.py`'s `LOGO_SVG`/header markup for
  responsive sizing — only the pictorial mark is the real asset; typesetting
  the wordmark in the site's own web font is not "redrawing the logo."
  A full redraw/vectorization of the mark itself remains separate, future,
  unstarted work.

## Positioning (locked)

The core argument: **recover the traffic/demand you already have, before
paying for more.** This is a sequencing argument, not an anti-ads stance —
managed ads are a real, sold add-on.

The sequence: **Google presence → website conversion → follow-up →
reactivation of anyone who didn't convert → THEN paid ads make sense**,
because ads just amplify whatever conversion rate already exists. Bad
foundation + paid traffic = more traffic converting at the same low rate.

## Visual System

- **Palette (changed — see history note below)**: **white/light is now the
  dominant background across the site.** Near-black is reserved for
  contrast bands only — nav bar, logo trust-bar strip, footer, and at most
  one deliberate dark section per page for rhythm (mirrors Academy Blast's
  own real pattern: mostly light, dark used sparingly for specific bands,
  never as the base theme). Accent color: **blue** — sampled directly from
  the real logo asset, `#1163B7` (a rich, medium-dark blue; deliberately
  not a bright/saturated "tech" blue). A lighter `--blue-bright` variant
  exists for emphasis text on dark bands, the same role `--gold-bright`
  used to play. **No gold/amber anywhere. No purple/violet, ever** (that
  rule never changed). Text: dark/near-black on light sections, light/white
  on dark contrast bands.
- **Layout**: single container, max-width ~1216px (`.wrap`), all-flexbox —
  no CSS grid.
- **Section rhythm**: `80px 0` padding on standard content sections (see
  `section{padding:...}` in `assets/styles.css` — currently `96px 0`
  desktop / `64px 0` mobile as this repo's own working value; treat `80px 0`
  as the reference-site finding to weigh against, not a hard override of
  what's already tuned here).
- **Typography**: uppercase **Big Shoulders Display** for all headlines,
  with **negative letter-spacing** (`-.02em` sitewide — deliberately gentler
  than Academy Blast's literal ratio since Big Shoulders is already
  condensed; going tighter starts crowding the caps). Nav links are
  **mixed-case, never uppercase**. Unchanged by the color-system update.
- **Border-radius discipline**: `0px` everywhere — sections, cards,
  containers, tables — **except** buttons (fully round), pill/proof
  components (`20px`, not fully round), and small circular icon/avatar
  badges (fully round — e.g. the `/pricing` included-list icons; same
  logic as Academy Blast's own round pill-avatar). No exceptions beyond
  these three without flagging it first. Unchanged by the color-system
  update.
- **Shadow discipline**: exactly one subtle shadow style exists sitewide,
  used only on the pill/proof component. No shadows on buttons, cards, or
  anything else. Unchanged by the color-system update.
- **Hero visual weight**: no large real-photo hero treatment (per the
  photography limitation above) — carried instead by a real, verified
  stat-pill row. **Now 3 pills**: "50+ Schools Worked With," "50,000+ Lead
  Conversations," "48-Hour Launch," in that order. "No Long-Term Contracts"
  does **not** get a 4th pill — it lives in the Comparison table's Contract
  Terms row instead, to avoid redundancy.

### History note — near-black+gold → white+blue

The site launched this rebuild on a near-black+gold palette (extracted and
adapted from Academy Blast, locked across many earlier rounds). That
palette is now retired sitewide in favor of white-primary+blue, to align
with Combat Boost's actual real brand (the live combatboost.ai logo is
black + blue, not gold). Nothing else in the Visual System section changed
— container, spacing, typography, radius, and shadow discipline all carry
over unchanged; only the color values themselves are different.

## Ban List (applies everywhere, always)

No emoji as UI decoration. No clip-art or generic AI-style illustrations.
No purely decorative card/button borders. **No purple/violet accent. No
gold/amber anywhere** (retired along with the old palette — see history
note above). No ALL-CAPS on nav links or body copy (headlines are the
confirmed exception). No oversized or baseline-misaligned decorative icons.
No middle-dot-joined label strings ("Label A · Label B · Label C"). No
generic uniform "SaaS-card-kit" look (identical rounded cards, one
border-radius everywhere, matching soft grey drop-shadows on every card,
gradient washes as pure decoration). Never use any stat, client count,
years-in-business, or number sourced from an unrelated business/template —
only the six confirmed facts above. **No em dashes anywhere in site copy**
(added Sep 2026, standing rule for this and all future passes) — rewrite
using periods, colons, or plain sentence structure instead. This applies to
every string a visitor can read (headlines, body copy, meta titles/
descriptions, alt text) — not to code comments in `build.py`/`styles.css`,
nor to HTML comments embedded in output (e.g. the Priority-6 dev note in
`FOOTER`), both of which are developer-facing planning notes, not
rendered/visible site copy.

## Current Site Structure (as of this file's last update)

Static multi-page site, no client-side router, no bundler. `build.py`
(local authoring script, not deployed) stitches shared head/nav/footer
around each page's body and writes flat HTML into the repo; Cloudflare
Pages serves those files as-is (Framework preset: None, no build command,
output directory `/`).

**Done**: the white-primary/blue-accent color system and the real logo
asset are live across all 5 existing pages (see the color-system history
note above). The homepage is built out to its full locked 10-section
structure — Hero (3 stat-pills) → Logo Trust Bar → Problem → 3-Step
Process → What's Included → Before/After Table → Testimonial → Comparison
(Combat Boost vs. Typical Agency) → FAQ (summary) → Final CTA — with a
full content-depth/visual-polish pass matching `/pricing`'s treatment
(multi-sentence copy per item, not one-liners; icon/badge components, not
plain bullets). This was a deliberate reversal of the earlier "keep it to
5, don't pad it out to match a competitor" decision — flagged and
confirmed with the site owner before building, given how much weight that
earlier decision carried.

The homepage's "What's Included" section reuses the *exact* `included_item()`
component/icon set `/pricing` uses (factored into shared constants in
`build.py` — `ICON_WEBSITE`/`ICON_STAR`/`ICON_MESSAGE`/`ICON_MEGAPHONE`),
not a second hand-built version — keep it that way if either page's copy
changes again. The homepage FAQ summary intentionally does **not** use the
collapsible `<details>` accordion `/faq` uses — a 3-question teaser reads
as broken/empty collapsed-by-default, so it's always-visible plain text
instead; only the full `/faq` page should use the accordion pattern.

**Still pending**: a new **Blog** page. It will carry general educational
content only — no fabricated stats or client stories; every claim on it
must still trace to the four confirmed facts above.

- `/` — Homepage (expanding to 10 sections per above).
- `/pricing/` — What's included, no price shown, "Book a Strategy Call" CTA.
  Included-list carries a small round icon per row (NextKick-derived craft
  pass — icon style/sizing documented in the border-radius exception
  above).
- `/results/` — All the real proof assets listed above, data-driven from
  `CALENDAR_ITEMS` / `TESTIMONIALS` lists in `build.py`.
- `/about/` — Company story, one real client photo.
- `/faq/` — Static Q&A (homepage gets a shorter FAQ *summary* section
  linking here — do not duplicate the full list on the homepage).
- `/blog/` — New, in progress.

"How It Works" is a **homepage anchor** (`/#how-it-works`), not a separate
page — do not treat it as one when building nav or footer links.

## Instruction for All Future Sessions

Read this file in full before making any design or copy change to this
repo. If a request conflicts with anything locked here, flag the conflict
before proceeding rather than silently overriding it. Update this file
whenever a locked fact, the section list, or the visual system changes —
it should always reflect the current, real state of the repo, not a
snapshot from whenever it was last edited.

## Standing Self-Audit (run after every build/edit, before presenting)

1. Re-read this file in full.
2. Check the changed page(s) against every item in the Ban List above.
3. Check that hero/hierarchy elements (alignment, letter-spacing,
   border-radius, shadow usage) match the Visual System section exactly —
   not a "close enough" approximation.
4. Check that every number, stat, or claim on the page traces back to a
   fact listed in this file — flag anything that doesn't.
5. Report any drift found, and fix it, before showing the result.
