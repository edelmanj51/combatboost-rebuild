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
- **51 real schools served** — always use **"50+ Schools"** as the headline
  stat. Never substitute any other school-count number from any other
  source, template, or estimate.
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
- Pricing ($297/mo) is **deliberately never shown** on the homepage or on
  the dedicated `/pricing` page itself — `/pricing` shows no number by
  design, keeping "Book a Call" as the path to that conversation. Do not
  add a price display or a pricing-gated lead form without an explicit,
  separate request — that's future work requiring form/backend handling
  outside this repo's current static-HTML, no-interactivity scope.

## Positioning (locked)

The core argument: **recover the traffic/demand you already have, before
paying for more.** This is a sequencing argument, not an anti-ads stance —
managed ads are a real, sold add-on.

The sequence: **Google presence → website conversion → follow-up →
reactivation of anyone who didn't convert → THEN paid ads make sense**,
because ads just amplify whatever conversion rate already exists. Bad
foundation + paid traffic = more traffic converting at the same low rate.

## Visual System (locked — extracted from Academy Blast's live site, adapted)

- **Palette**: near-black + gold/amber accent. NOT navy. NOT purple/violet.
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
  **mixed-case, never uppercase**.
- **Border-radius discipline**: `0px` everywhere — sections, cards,
  containers, tables — **except** buttons (fully round), pill/proof
  components (`20px`, not fully round), and small circular icon/avatar
  badges (fully round — e.g. the `/pricing` included-list icons; same
  logic as Academy Blast's own round pill-avatar). No exceptions beyond
  these three without flagging it first.
- **Shadow discipline**: exactly one subtle shadow style exists sitewide,
  used only on the pill/proof component. No shadows on buttons, cards, or
  anything else.
- **No hero photo** (per the photography limitation above) — hero visual
  weight comes from a real, verified stat-pill row instead. Currently: a
  single pill, "50+ Schools Worked With" — do not add a second pill unless
  a genuinely new, verified, company-wide aggregate becomes available.

## Ban List (applies everywhere, always)

No emoji as UI decoration. No clip-art or generic AI-style illustrations.
No purely decorative card/button borders. No purple/violet accent. No
ALL-CAPS on nav links or body copy (headlines are the confirmed exception).
No oversized or baseline-misaligned decorative icons. No middle-dot-joined
label strings ("Label A · Label B · Label C"). No generic uniform
"SaaS-card-kit" look (identical rounded cards, one border-radius everywhere,
matching soft grey drop-shadows on every card, gradient washes as pure
decoration). Never use any stat, client count, years-in-business, or number
sourced from an unrelated business/template — only the verified facts above.

## Current Site Structure (as of this file's last update)

Static multi-page site, no client-side router, no bundler. `build.py`
(local authoring script, not deployed) stitches shared head/nav/footer
around each page's body and writes flat HTML into the repo; Cloudflare
Pages serves those files as-is (Framework preset: None, no build command,
output directory `/`).

- `/` — Homepage, exactly 5 sections: hero (no photo, single stat-pill) →
  logo trust bar → before/after sequencing table (Website / Reviews &
  Referrals / Follow-Up / Reactivation) → testimonial (Dan Carey video +
  quote) → final CTA. Do not add a 6th section without flagging it first —
  this count was deliberately capped, including against Academy Blast's own
  real page having 13 sections.
- `/pricing/` — What's included, no price shown, "Book a Strategy Call" CTA.
- `/results/` — All the real proof assets listed above, data-driven from
  `CALENDAR_ITEMS` / `TESTIMONIALS` lists in `build.py`.
- `/about/` — Company story, one real client photo.
- `/faq/` — Static Q&A.

`/pricing`'s included-list now carries a small round icon per row (added
via a targeted craft pass, spec extracted from NextKick's real feature-grid
component — icon style, sizing, and alignment documented in the
border-radius exception above). There is otherwise still **no icon-based
feature/benefit card grid anywhere on the site** — the homepage's
feature-strip from an earlier round remains dead CSS, unused, deliberately
plain text with no icon boxes.

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
