#!/usr/bin/env python3
"""
Local authoring convenience only — NOT part of the deployed site and not
run by Cloudflare Pages. Stitches a shared header/footer around each
page's unique body content and writes the final, already-static HTML
files directly into the repo (index.html, pricing/index.html, etc.).
Cloudflare Pages just serves those files as-is — Framework preset: None,
build command: empty, output directory: /.

Run: python3 build.py
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

NAV_ITEMS = [
    ("/", "Home"),
    ("/#how-it-works", "How It Works"),
    ("/results/", "Results"),
    ("/pricing/", "Pricing"),
    ("/faq/", "FAQ"),
    # About intentionally unlinked for now (nav and footer both) — the
    # page file stays in the repo, just not linked anywhere until it's
    # revisited. Do not delete about/index.html or build_about().
]

# Real logo mark (figure + upward arrow + growth-chart frame), pulled
# directly from the live combatboost.ai site rather than redrawn — see
# PROJECT.md's "Real logo asset" note. Native asset is 194x240 (w x h);
# height is the only thing callers set, width follows the real ratio.
LOGO_ASSET_RATIO = 194 / 240


def logo_mark(height):
    width = round(height * LOGO_ASSET_RATIO)
    return f'<img src="/assets/images/logo-mark.png" alt="" width="{width}" height="{height}" aria-hidden="true">'


# Shared icon set for the included-list/included-icon component (NextKick
# spec extraction, adapted — see PROJECT.md's border-radius exception).
# Defined once here so /pricing and the homepage's "What's Included"
# section render the identical component, not two hand-copied versions.
_SVG_OPEN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
ICON_WEBSITE = f'{_SVG_OPEN}<rect x="3" y="4" width="18" height="16" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/></svg>'
ICON_STAR = f'{_SVG_OPEN}<polygon points="12 2.5 14.8 8.6 21.5 9.4 16.6 14 18 20.6 12 17.2 6 20.6 7.4 14 2.5 9.4 9.2 8.6"/></svg>'
ICON_MESSAGE = f'{_SVG_OPEN}<path d="M4 5h16v11H8l-4 4V5z"/></svg>'
ICON_MEGAPHONE = f'{_SVG_OPEN}<path d="M3 11v2a2 2 0 0 0 2 2h1l3 5V4l-3 5H5a2 2 0 0 0-2 2z"/><path d="M14 8a4 4 0 0 1 0 8"/><path d="M17 5a8 8 0 0 1 0 14"/></svg>'


def included_item(icon, title_html, body_html):
    return f'''      <div class="included-item">
        <div class="included-icon-row">
          <span class="included-icon">{icon}</span>
          <h3>{title_html}</h3>
        </div>
        <p>{body_html}</p>
      </div>'''


def head(title, description, canonical_path):
    return f'''<!doctype html>
<meta charset="utf-8">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://combatboost.ai{canonical_path}">
<link rel="stylesheet" href="/assets/styles.css">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@600;700;800&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap">'''


def header(active_href):
    links = []
    for href, label in NAV_ITEMS:
        current = ' aria-current="page"' if href == active_href else ''
        links.append(f'      <a href="{href}"{current}>{label}</a>')
    nav_links = "\n".join(links)
    return f'''<div class="concept-banner"><b>CONCEPT</b>: multi-page structure for internal review, built from the locked rebuild brief. Not the production site.</div>

<header>
  <div class="wrap header-inner">
    <a class="brand" href="/">
      {logo_mark(34)}
      <span class="brand-word">Combat<span>Boost</span></span>
    </a>
    <div class="header-actions">
      <nav class="main" id="main-nav">
        <a class="btn btn-primary mobile-cta" href="/pricing/#call">Book a Strategy Call</a>
{nav_links}
      </nav>
      <a class="btn btn-primary" href="/pricing/#call">Book a Strategy Call</a>
      <button class="nav-toggle" id="nav-toggle" aria-label="Toggle menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>'''


FOOTER = f'''<!-- PRIORITY 6, NOT BUILT THIS PASS: a self-serve "Free Website Health Check"
     lead magnet (enter your URL, get a scored report) — similar to Monstro's
     Health Check Analyzer and 97Display's Website Audit tool. Strong fit
     since Joe already runs this kind of audit manually on cold prospects.
     Flagged for a future pass, not attempted here. -->

<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-about">
        <div class="brand" style="margin-bottom:4px">
          {logo_mark(26)}
          <span class="brand-word">Combat<span>Boost</span></span>
        </div>
        <p>Websites, review &amp; referral automation, and AI follow-up. Built exclusively for martial arts schools.</p>
      </div>
      <div>
        <h5>Product</h5>
        <ul class="foot-links">
          <li><a href="/#how-it-works">The Website</a></li>
          <li><a href="/#how-it-works">Reviews &amp; Referrals</a></li>
          <li><a href="/#how-it-works">Follow-Up &amp; Reactivation</a></li>
          <li><a href="/pricing/">Ads (Add-On)</a></li>
        </ul>
      </div>
      <div>
        <h5>Company</h5>
        <ul class="foot-links">
          <li><a href="/results/">Results</a></li>
          <li><a href="/pricing/">Pricing</a></li>
          <li><a href="/faq/">FAQ</a></li>
        </ul>
      </div>
      <div>
        <h5>Contact</h5>
        <ul class="foot-links">
          <li>support@combatboost.ai</li>
          <li>516-957-3100</li>
          <li>26 Broadway, STE 934<br>New York, NY 10004</li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© 2026 JPE Enterprises LLC, DBA Combat Boost. All rights reserved.</span>
      <span><a href="#">Privacy Policy</a> &nbsp;·&nbsp; <a href="#">Terms of Use</a></span>
    </div>
  </div>
</footer>
<script src="/assets/nav.js"></script>'''


def page(title, description, canonical_path, active_href, body):
    return f'''{head(title, description, canonical_path)}

{header(active_href)}

{body}

{FOOTER}
'''


def write(rel_path, content):
    full = os.path.join(ROOT, rel_path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  wrote {rel_path}  ({len(content):,} bytes)")


# ============================================================
# HOMEPAGE
# ============================================================
def build_homepage():
    body = '''<section class="hero" id="top">
  <div class="wrap hero-content">
    <h1>You're Not Losing to Competitors.<br>You're Losing Traffic You <em>Already Have</em>.</h1>
    <p class="dek">People are already searching for a school like yours. Your website, your follow-up, or your old leads are letting them walk. Fix that before you spend a dollar on ads.</p>
    <div class="actions">
      <a class="btn btn-primary" href="/pricing/#call">Book a Strategy Call</a>
      <a class="btn btn-ghost-light" href="#how-it-works">See How It Works</a>
    </div>
    <div class="proof-pills">
      <div class="proof-pill"><span class="pp-num">50+</span><span class="pp-txt">Schools Worked With</span></div>
      <div class="proof-pill"><span class="pp-num">50,000+</span><span class="pp-txt">Lead Conversations</span></div>
      <div class="proof-pill"><span class="pp-num">48-Hour</span><span class="pp-txt">Launch</span></div>
    </div>
  </div>
</section>

<div class="proof">
  <div class="wrap proof-inner">
    <div class="proof-lede"><b>50+</b><span>martial arts schools<br>worked with, including:</span></div>
    <div class="logo-row">
      <div class="logo-word">Premier<br><small>Martial Arts</small></div>
      <div class="logo-word">ATA<br><small>American Taekwondo Assoc.</small></div>
      <div class="logo-word">Moore's Karate<br><small>13 CA locations</small></div>
      <div class="logo-word">Ahn's Taekwondo<br><small>4 locations</small></div>
      <div class="logo-word">Camal &amp; Cruz<br><small>Judo &amp; BJJ</small></div>
      <div class="logo-word">Striker Lab<br><small>Muay Thai Kickboxing</small></div>
    </div>
  </div>
</div>

<section id="problem">
  <div class="wrap">
    <div class="section-head">
      <h2>You Don't Have a Traffic Problem.<br>You Have a Conversion Problem.</h2>
      <p>Here's what that actually looks like, day to day:</p>
    </div>
    <ul class="problem-list">
      <li><span class="problem-mark">&#10005;</span>A parent finds you on Google, opens your site on their phone, and leaves before it even loads.</li>
      <li><span class="problem-mark">&#10005;</span>You've got a school parents love, but only a handful of reviews to show for it.</li>
      <li><span class="problem-mark">&#10005;</span>A trial-class lead texts in at 9pm and doesn't hear back until you're free the next afternoon.</li>
      <li><span class="problem-mark">&#10005;</span>A member quits, and nobody ever reaches back out to see if they'd come back.</li>
    </ul>
    <p class="problem-closing">None of these are separate problems. They're the same traffic. The parent who found you, the lead who almost booked, the member who almost stayed. All falling through the same cracks, one after another. Fix the sequence, and all four stop happening at once. That's the difference between patching one symptom and fixing the actual system.</p>
  </div>
</section>

<section class="on-light" id="process">
  <div class="wrap">
    <div class="section-head">
      <h2>From First Call to Live Site, Here's Exactly What Happens.</h2>
    </div>
    <div class="process-steps">
      <div class="process-step">
        <span class="process-badge">1</span>
        <h3>Book a Strategy Call</h3>
        <p>We look at your actual website, search presence, and current follow-up process, and tell you honestly where the biggest gap actually is. Not a generic audit: a specific one based on your school. If a full rebuild isn't the right move yet, we'll tell you that too.</p>
      </div>
      <div class="process-step">
        <span class="process-badge">2</span>
        <h3>We Build Your System</h3>
        <p>Your website, review &amp; referral automation, and follow-up &amp; reactivation get built and connected as one system, live in as fast as 48 hours. Nothing launches in disconnected pieces; it's built to work together from day one.</p>
      </div>
      <div class="process-step">
        <span class="process-badge">3</span>
        <h3>Leads Start Converting</h3>
        <p>You keep teaching. The system follows up with new leads within minutes, requests reviews after every win, and reaches out to old leads and inactive members one real conversation at a time. All running automatically in the background.</p>
      </div>
    </div>
  </div>
</section>

<section id="whats-included">
  <div class="wrap">
    <div class="section-head">
      <h2>One System. Four Connected Parts.</h2>
    </div>
    <div class="included-list">
''' + '\n'.join([
        included_item(ICON_WEBSITE, "The Website",
            "Not a template with your logo dropped in: a real, mobile-first site built around one job. Turning the parent researching schools at 9pm into a booked intro class."),
        included_item(ICON_STAR, "Reviews &amp; Referrals",
            "Every sign-up, promotion, or good class automatically triggers a review or referral request, so your reputation grows on its own instead of depending on you remembering to ask."),
        included_item(ICON_MESSAGE, "Follow-Up &amp; Reactivation",
            "New leads get followed up within minutes. Leads and past members already sitting in your database get reached out to personally, one real conversation at a time, not a mass blast, typically recovering 2&ndash;4% of that list."),
        included_item(ICON_MEGAPHONE, 'Managed Ads <span class="tag-optional">Optional</span>',
            "Ads amplify whatever conversion rate already exists. Once your site, reviews, and follow-up are proven to convert, paid traffic becomes worth paying for. Not before."),
    ]) + '''
    </div>
    <p class="included-teaser-link"><a href="/pricing/">Full breakdown, plus what's included at every stage &rarr; See Pricing</a></p>
  </div>
</section>

<section class="on-light" id="how-it-works">
  <div class="wrap">
    <div class="section-head">
      <h2>It's One Sequence, Not Four Fixes.</h2>
      <p>Google search &rarr; your website &rarr; your follow-up &rarr; nothing falls through the cracks.</p>
    </div>
    <div class="tableWrap">
      <table class="baTable">
        <thead>
          <tr><th>Area</th><th>Before</th><th>After</th></tr>
        </thead>
        <tbody>
          <tr>
            <td>Website</td>
            <td><span class="mark bad">Looks fine. Converts nobody.</span></td>
            <td><span class="mark good">Built to turn visits into booked intros.</span></td>
          </tr>
          <tr>
            <td>Reviews &amp; Referrals</td>
            <td><span class="mark bad">A few old reviews. No referral system.</span></td>
            <td><span class="mark good">Requested automatically, after every win.</span></td>
          </tr>
          <tr>
            <td>Follow-Up</td>
            <td><span class="mark bad">New leads texted back "when there's time."</span></td>
            <td><span class="mark good">Every lead followed up within minutes.</span></td>
          </tr>
          <tr class="reactivation-row">
            <td>Reactivation</td>
            <td><span class="mark bad">Old leads and inactive members, sitting cold.</span></td>
            <td><span class="mark good">Re-engaged 1:1. Real conversations, not mass texts.</span></td>
          </tr>
        </tbody>
      </table>
    </div>

    <p class="reactivation-callout">Cold leads and inactive members don't respond to a mass text. They respond to a real, personal 1:1 conversation. That's the actual mechanism, not a bigger blast.</p>

    <div class="reactivation-note">
      <p>Reactivation campaigns typically recover <b>2–4%</b> of a school's existing dead-lead and inactive-member list. A list of 500 typically returns <b>10–20</b> booked appointments. A list of 1,000 typically returns <b>20–40</b>, no added ad spend.</p>
    </div>
  </div>
</section>

<section id="proof-story">
  <div class="wrap video-block">
    <div>
      <div class="video-embed-wrap">
        <iframe src="https://player.vimeo.com/video/1224788450?h=171cc92b25&title=0&byline=0&portrait=0"
                frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen loading="lazy"
                title="Dan Carey, real Combat Boost client, video testimonial"></iframe>
      </div>
    </div>
    <div class="video-quote">
      <p class="lede" style="margin-bottom:8px">Here's what that sequence looks like for one real school, start to finish. Not a hypothetical: an actual client.</p>
      <p class="q">"I absolutely would recommend it... I think I waited too long. <span>But it was the right time when we were able to team up.</span> I would definitely make the investment because it's going to come back to you. It really doesn't take too long for you to see the benefit."</p>
      <p class="attr">Dan Carey, real client</p>
    </div>
  </div>
</section>

<section class="on-light" id="comparison">
  <div class="wrap">
    <div class="section-head">
      <h2>Combat Boost vs. Typical Agency.</h2>
    </div>
    <div class="tableWrap">
      <table class="baTable">
        <thead>
          <tr><th>Area</th><th>Combat Boost</th><th>Typical Agency</th></tr>
        </thead>
        <tbody>
          <tr>
            <td>Contract Terms</td>
            <td class="cmp-us">No Long-Term Contracts</td>
            <td class="cmp-them">Standard locked contracts</td>
          </tr>
          <tr>
            <td>Pricing</td>
            <td class="cmp-us">One flat monthly rate</td>
            <td class="cmp-them">Custom quotes, scope creep</td>
          </tr>
          <tr>
            <td>Built For</td>
            <td class="cmp-us">Martial arts schools, exclusively</td>
            <td class="cmp-them">Not specialized to your industry</td>
          </tr>
          <tr>
            <td>Launch Speed</td>
            <td class="cmp-us">48-Hour Launch</td>
            <td class="cmp-them">Typically weeks to months</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section id="faq-summary">
  <div class="wrap" style="max-width:820px">
    <div class="section-head">
      <h2>Quick Answers Before You Book.</h2>
    </div>
    <div class="faq-summary-list">
      <div class="faq-summary-item">
        <h3>Do I need to stop running ads?</h3>
        <p>No. Sequencing, not opposition. Fix the foundation first, then ads go further.</p>
      </div>
      <div class="faq-summary-item">
        <h3>How long does it take to launch?</h3>
        <p>Most schools are live within 48 hours of kickoff, site and automation together.</p>
      </div>
      <div class="faq-summary-item">
        <h3>Is there a contract?</h3>
        <p>No long-term contracts. You're not locked into a term you can't get out of if the system isn't working for you.</p>
      </div>
      <div class="faq-summary-item">
        <h3>What's actually included?</h3>
        <p>The website, the review and referral automation, and the follow-up and reactivation system. One build, one monthly rate.</p>
      </div>
      <div class="faq-summary-item">
        <h3>Do you work with multi-location schools?</h3>
        <p>Yes. Several of the 50+ schools we've worked with run multiple locations under one brand, including a 13-location California franchise.</p>
      </div>
    </div>
    <p class="included-teaser-link"><a href="/faq/">More questions? See the Full FAQ &rarr;</a></p>
  </div>
</section>

<section class="closing" id="cta">
  <div class="wrap">
    <h2>Stop Losing Traffic<br>You Already Have.</h2>
    <p>One flat plan covers the whole sequence: website, reviews, follow-up, reactivation. No tiers to guess between, no ad spend required to get started. Ads come later, once the foundation's proven to convert what you already have.</p>
    <div class="actions" style="justify-content:center; display:flex; gap:14px; flex-wrap:wrap">
      <a class="btn btn-primary" href="/pricing/#call">Book a Strategy Call</a>
    </div>
  </div>
</section>'''
    write("index.html", page(
        "Combat Boost | Websites, Reviews & Follow-Up for Martial Arts Schools",
        "Combat Boost builds websites, review & referral automation, and AI follow-up for martial arts schools. Worked with 50+ schools, before you spend another dollar on ads.",
        "/", "/", body))


# ============================================================
# PRICING
# ============================================================
def build_pricing():
    body = '''<section class="page-hero">
  <div class="wrap">
    <a class="crumb" href="/">&larr; Back to Home</a>
    <h1>Simple, Straightforward Pricing.</h1>
    <p class="dek">$297/month covers the full system: your website, reviews &amp; referrals, and follow-up &amp; reactivation. Facebook and Google ad management, plus multi-location setups, are quoted separately based on what your school actually needs.</p>
    <div class="proof-pills" style="margin-top:30px">
      <div class="proof-pill"><span class="pp-num">50+</span><span class="pp-txt">Schools Worked With</span></div>
      <div class="proof-pill"><span class="pp-num">50,000+</span><span class="pp-txt">Lead Conversations</span></div>
      <div class="proof-pill"><span class="pp-num">48-Hour</span><span class="pp-txt">Launch</span></div>
      <div class="proof-pill"><span class="pp-num">Zero</span><span class="pp-txt">Ad Spend Required</span></div>
      <div class="proof-pill"><span class="pp-num">30-Day</span><span class="pp-txt">Money-Back Guarantee</span></div>
    </div>
  </div>
</section>

<section class="on-light" style="padding-top:0">
  <div class="wrap">
    <div class="included-list">
''' + '\n'.join([
        included_item(ICON_WEBSITE, "The Website",
            "A real, built-to-convert website for your school. Not a template with your logo dropped in. This is the core deliverable and where most of the build time goes."),
        included_item(ICON_STAR, "Reviews &amp; Referrals",
            "Automated requests sent after every win, so your Google reviews and referrals grow on their own instead of depending on you remembering to ask."),
        included_item(ICON_MESSAGE, "Follow-Up &amp; Reactivation",
            "Every new lead followed up within minutes, and your existing past-member list re-engaged on autopilot. Not left cold in an old spreadsheet or CRM."),
        included_item(ICON_MEGAPHONE, 'Managed Ads <span class="tag-optional">Quoted Separately</span>',
            "Once the site, reviews, and follow-up are converting what you already have, we'll run Google/Facebook ads for you if it makes sense. Never the starting point."),
    ]) + '''
    </div>
  </div>
</section>

<section id="pricing-faq">
  <div class="wrap" style="max-width:820px">
    <div class="section-head">
      <h2>Questions About Pricing.</h2>
    </div>
    <details class="faq-item" open>
      <summary>Is there a contract?</summary>
      <p>No long-term contracts. You're not locked into a term you can't get out of if the system isn't working for you.</p>
    </details>
    <details class="faq-item">
      <summary>What's actually included?</summary>
      <p>The website, the review &amp; referral automation, and the lead follow-up and past-member reactivation system. One build, one monthly rate, no separate tools to stitch together yourself.</p>
    </details>
    <details class="faq-item">
      <summary>Do I need to stop running ads?</summary>
      <p>No. If ads are working for you, keep running them. Our point is sequencing, not opposition: fix what converts the traffic you already get first, then ads go further with every dollar.</p>
    </details>
    <details class="faq-item">
      <summary>What if it's not working for my school?</summary>
      <p>You're covered by our 30-day money-back guarantee. If it's not working for your school in the first 30 days, we'll refund it.</p>
    </details>
  </div>
</section>

<section class="closing" id="call">
  <div class="wrap">
    <h2>Get Started.</h2>
    <p>15 minutes, no pressure. We'll look at your current site and tell you honestly whether a rebuild is the right move for your school right now.</p>
    <div class="actions" style="justify-content:center; display:flex; gap:14px; flex-wrap:wrap">
      <a class="btn btn-primary" href="#">Book a Strategy Call</a>
      <a class="btn btn-ghost-dark" href="/results/">See the Results</a>
    </div>
  </div>
</section>'''
    write("pricing/index.html", page(
        "Pricing | Combat Boost",
        "$297/month covers the full Combat Boost system: website, reviews & referrals, and follow-up & reactivation for martial arts schools. Ads and multi-location setups quoted separately.",
        "/pricing/", "/pricing/", body))


# ============================================================
# RESULTS — data-driven, repeatable-card pattern.
#
# This page is built entirely from the lists below. To add a new proof
# item as more results come in, append one entry to the relevant list —
# CALENDAR_ITEMS, PAGESPEED, SEARCH_VISIBILITY, GROWTH_ITEMS, or
# TESTIMONIALS — and re-run `python3 build.py`. No page markup needs to
# change. `img: None` renders an honest "screenshot pending" placeholder
# tile instead of a broken image, so items can be added the moment real
# assets land (once Drive access is connected) without a rebuild.
# ============================================================

CALENDAR_ITEMS = [
    # (school, badge, img_path_or_None, featured) — all images real, pulled from the
    # client's Drive folder and redacted (student names/personal info pixelated;
    # school names, dates, and appointment density left intact).
    {"school": "Pensacola ATA",                          "badge": "$0 Ad Spend", "img": "/assets/images/results/calendar-pensacola-1.png", "featured": True},
    {"school": "Premier Martial Arts, Pembroke Pines",   "badge": "$0 Ad Spend", "img": "/assets/images/results/calendar-premier-pembroke.png", "featured": True},
    {"school": "Alliance Jiu Jitsu",                      "badge": "$0 Ad Spend", "img": "/assets/images/results/calendar-alliance-jiujitsu.png", "featured": True},
    {"school": "Black Belt World, Toronto",               "badge": "$0 Ad Spend", "img": "/assets/images/results/calendar-blackbelt-toronto.png", "featured": True},
    {"school": "Kick It Taekwondo, August", "badge": "Fully Booked", "img": "/assets/images/results/calendar-kickit-august.png", "featured": True, "note": "Same school, 5 months later. See the March starting point below."},
    {"school": "Kick It Taekwondo, March",  "badge": "Starting Point", "img": "/assets/images/results/calendar-kickit-march.png", "featured": False},
    {"school": "Kick It Taekwondo, March (2nd calendar)",  "badge": "Starting Point", "img": "/assets/images/results/calendar-kickit-march-2.png", "featured": False},
    {"school": "Kick It Taekwondo, August (2nd calendar)", "badge": "Fully Booked", "img": "/assets/images/results/calendar-kickit-august-2.png", "featured": False},
    {"school": "Fort Walton ATA",                         "badge": "$0 Ad Spend", "img": "/assets/images/results/calendar-fortwalton.png", "featured": False},
    {"school": "Crestview ATA",                           "badge": "$0 Ad Spend", "img": "/assets/images/results/calendar-crestview-1.png", "featured": False},
    {"school": "Crestview ATA (2nd month)",               "badge": "$0 Ad Spend", "img": "/assets/images/results/calendar-crestview-2.png", "featured": False},
    {"school": "Camal & Cruz Judo & BJJ",                 "badge": "$0 Ad Spend", "img": "/assets/images/results/calendar-camalcruz.png", "featured": False},
    {"school": "Pensacola ATA (2nd month)",               "badge": "$0 Ad Spend", "img": "/assets/images/results/calendar-pensacola-2.png", "featured": False},
]

TESTIMONIALS = [
    {
        "name": "Dan Carey", "kind": "Video", "primary": True,
        "quote": "I think I waited too long, but it was the right time when we were able to team up. I would definitely make the investment, because it's going to come back to you.",
    },
]


def calendar_card(item):
    note = f'<p class="proof-note">{item["note"]}</p>' if item.get("note") else ""
    if item["img"]:
        media = f'<img class="proof-shot" src="{item["img"]}" alt="{item["school"]} booking calendar">'
    else:
        media = f'<div class="proof-pending">Screenshot pending<br><span>awaiting Drive access</span></div>'
    return f'''      <div class="proof-card">
        {media}
        <div class="proof-card-body">
          <span class="proof-badge">{item["badge"]}</span>
          <h3>{item["school"]}</h3>
          {note}
        </div>
      </div>'''


def build_results():
    featured = [c for c in CALENDAR_ITEMS if c["featured"]]
    more = [c for c in CALENDAR_ITEMS if not c["featured"]]
    featured_html = "\n".join(calendar_card(c) for c in featured)
    more_html = "\n".join(calendar_card(c) for c in more)

    body = f'''<section class="page-hero">
  <div class="wrap">
    <a class="crumb" href="/">&larr; Back to Home</a>
    <h1>The Results, Not Just the Pitch.</h1>
    <p class="dek">Real calendars, real search rankings, real load times, real client messages. From real schools, worked with across 50+ launches. This page grows every time a new one comes in.</p>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap" style="max-width:820px">
    <div class="video-embed-wrap">
      <iframe src="https://player.vimeo.com/video/1224788450?h=171cc92b25&title=0&byline=0&portrait=0"
              frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen loading="lazy"
              title="Dan Carey, real Combat Boost client, video testimonial"></iframe>
    </div>
    <p class="story-quote">"{TESTIMONIALS[0]["quote"]}"</p>
    <p class="testimonial-name">Dan Carey, real client (permission granted)</p>
  </div>
</section>

<section class="on-light" id="calendars">
  <div class="wrap">
    <div class="section-head">
      <h2>Real Calendars, Real Appointments.</h2>
      <p>Booking calendars from real schools we've worked with. Most of these filled up on $0 ad spend, powered entirely by the site converting traffic that was already there. Student names and personal info are redacted; school names are real.</p>
    </div>
    <div class="proof-grid">
{featured_html}
    </div>
    <details class="proof-more">
      <summary>See {len(more)} more real calendars</summary>
      <div class="proof-grid" style="margin-top:24px">
{more_html}
      </div>
    </details>
  </div>
</section>

<section id="performance">
  <div class="wrap">
    <div class="section-head">
      <h2>Site Performance: Before &amp; After.</h2>
      <p>A real client's website (a martial arts school in Middle River, MD), measured on Google PageSpeed Insights before and after the rebuild. Mobile scores shown.</p>
    </div>
    <div class="stat-compare">
      <div class="stat-compare-item">
        <span class="sc-label">Mobile Load Time (First Contentful Paint)</span>
        <div class="sc-nums"><span class="sc-before">6.9s</span><span class="sc-arrow">→</span><span class="sc-after">1.0s</span></div>
      </div>
      <div class="stat-compare-item">
        <span class="sc-label">Mobile Performance Score</span>
        <div class="sc-nums"><span class="sc-before">31</span><span class="sc-arrow">→</span><span class="sc-after">99</span></div>
      </div>
    </div>
    <img class="proof-wide" src="/assets/images/results/site-performance.png" alt="Google PageSpeed Insights score for a real client's site, before and after the Combat Boost rebuild" style="margin-top:28px">
  </div>
</section>

<section class="on-light2" id="search-visibility">
  <div class="wrap">
    <div class="section-head">
      <h2>Search Visibility: Before &amp; After.</h2>
      <p>Up Top Martial Arts Academy: Google Maps ranking density and review count, before and after.</p>
    </div>
    <div class="stat-compare">
      <div class="stat-compare-item">
        <span class="sc-label">Google Reviews</span>
        <div class="sc-nums"><span class="sc-before">58</span><span class="sc-arrow">→</span><span class="sc-after">103</span></div>
      </div>
      <div class="stat-compare-item">
        <span class="sc-label">Google Rating</span>
        <div class="sc-nums"><span class="sc-before">4.9</span><span class="sc-arrow">→</span><span class="sc-after">5.0</span></div>
      </div>
    </div>
    <img class="proof-wide" src="/assets/images/results/search-heatmap.png" alt="Up Top Martial Arts Academy's Google Maps ranking heatmap, before and after. More green pins, closer to the pin, means ranking higher for nearby searches" style="margin-top:28px">
  </div>
</section>

<section id="growth">
  <div class="wrap">
    <div class="section-head">
      <h2>Growth Over Time, Not Just One Before/After.</h2>
      <p>Sustained results across a full client relationship: reviews, web traffic, and new contracts signed, tracked over time rather than a single snapshot.</p>
    </div>
    <div class="stat-compare" style="margin-bottom:28px">
      <div class="stat-compare-item">
        <span class="sc-label">Total Google Reviews, Reached in 2026</span>
        <div class="sc-nums"><span class="sc-after">46</span></div>
      </div>
      <div class="stat-compare-item">
        <span class="sc-label">Website Clicks From Google Business Profile, in 90 Days</span>
        <div class="sc-nums"><span class="sc-after">128</span></div>
      </div>
    </div>
    <div class="growth-grid">
      <img class="proof-wide" src="/assets/images/results/growth-reviews.png" alt="Total Google reviews by year for a real client, climbing sharply in 2026">
      <img class="proof-wide" src="/assets/images/results/growth-traffic.png" alt="Website clicks from a real client's Google Business Profile, June to August 2026">
      <img class="proof-wide" src="/assets/images/results/growth-billing-1.png" alt="New contracts signed by month for a real client, peaking at 17 in July">
      <img class="proof-wide" src="/assets/images/results/growth-billing-2.png" alt="New contracts signed by month for a second real client, peaking at 18 in May">
    </div>
  </div>
</section>

<section class="closing" id="call">
  <div class="wrap">
    <h2>Want Results Like These?</h2>
    <p>Book a call and we'll show you what this would look like for your school specifically.</p>
    <div class="actions" style="justify-content:center; display:flex; gap:14px; flex-wrap:wrap">
      <a class="btn btn-primary" href="/pricing/#call">Book a Strategy Call</a>
    </div>
  </div>
</section>'''
    write("results/index.html", page(
        "Results | Combat Boost",
        "Real booking calendars, real search visibility gains, real site performance improvements, and real client testimonials from Combat Boost's 50+ martial arts school clients.",
        "/results/", "/results/", body))


# ============================================================
# ABOUT
# ============================================================
def build_about():
    body = '''<section class="page-hero">
  <div class="wrap">
    <a class="crumb" href="/">&larr; Back to Home</a>
    <h1>We Only Work With Martial Arts Schools.</h1>
    <p class="dek">Not gyms in general, not "local businesses." Martial arts schools specifically.</p>
  </div>
</section>

<section class="on-light2" style="padding-top:0">
  <div class="wrap about-grid">
    <div>
      <img class="about-photo" src="/assets/images/about-photo.jpg" alt="A real Combat Boost client, mid-class" loading="lazy">
      <p class="about-cap">One of the 50+ schools we've worked with, mid-class.</p>
    </div>
    <div class="about-copy">
      <p style="font-size:15.5px; color:var(--tx-dark-soft)">A belt-testing schedule, a trial-class funnel, and a parent's decision process don't look like anything else we could serve instead. So rather than build a generic small-business playbook and put a karate photo on top of it, we only work in this one industry.</p>
      <p style="font-size:15.5px; color:var(--tx-dark-soft)">Everything on this site is built from what's actually worked across <span class="stat-inline">50+</span> real school launches, from single-location dojos to multi-location franchises. One system: the website, the review &amp; referral automation, and the follow-up, sold as one connected build, not separate add-ons.</p>
      <p style="font-size:15.5px; color:var(--tx-dark-soft)">The core belief behind how we sequence the work: most schools are already getting real traffic, from Google, from reviews, from word of mouth. The website's job is to actually convert that traffic before spending anything on ads to get more of it.</p>
    </div>
  </div>
</section>

<section class="closing" id="call">
  <div class="wrap">
    <h2>Let's Talk About Your School.</h2>
    <p>Book a call and we'll tell you honestly where the biggest gap is for you right now.</p>
    <div class="actions" style="justify-content:center; display:flex; gap:14px; flex-wrap:wrap">
      <a class="btn btn-primary" href="/pricing/#call">Book a Strategy Call</a>
      <a class="btn btn-ghost-dark" href="/results/">See the Results</a>
    </div>
  </div>
</section>'''
    write("about/index.html", page(
        "About | Combat Boost",
        "Combat Boost only works with martial arts schools: websites, review & referral automation, and follow-up, built from what's worked across 50+ real school launches.",
        "/about/", "/about/", body))


# ============================================================
# FAQ
# ============================================================
def build_faq():
    body = '''<section class="page-hero">
  <div class="wrap" style="max-width:820px">
    <a class="crumb" href="/">&larr; Back to Home</a>
    <h1>Straight Answers.</h1>
    <p class="dek">The questions we actually get asked on strategy calls, answered here first.</p>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap" style="max-width:820px">
    <details class="faq-item" open>
      <summary>Do I need to stop running ads?</summary>
      <p>No. If ads are working for you, keep running them. Our point is sequencing, not opposition: fix what converts the traffic you already get first, then ads go further with every dollar. We also build and run ads ourselves once that foundation is in place. See Pricing for how that fits in.</p>
    </details>
    <details class="faq-item">
      <summary>I already have a website. Do I need a new one?</summary>
      <p>Usually, yes. Most schools' sites were built once and never touched again. We'll tell you honestly on the call if a rebuild isn't the highest-leverage move for you yet.</p>
    </details>
    <details class="faq-item">
      <summary>How long does it take to launch?</summary>
      <p>Most schools are live within 48 hours of kickoff, site and automation together. Not a six-month agency timeline.</p>
    </details>
    <details class="faq-item">
      <summary>What's actually included?</summary>
      <p>The website, the review &amp; referral automation, and the lead follow-up and past-member reactivation system. One build, one monthly rate, no separate tools to stitch together yourself. Full breakdown on the Pricing page.</p>
    </details>
    <details class="faq-item">
      <summary>Is there a contract?</summary>
      <p>No long-term contracts. You're not locked into a term you can't get out of if the system isn't working for you.</p>
    </details>
    <details class="faq-item">
      <summary>Do you work with multi-location schools?</summary>
      <p>Yes. Several of the 50+ schools we've worked with run multiple locations under one brand, including a 13-location California franchise. See Results.</p>
    </details>
    <details class="faq-item">
      <summary>What if I'm not sure a rebuild is worth it yet?</summary>
      <p>Ask on the call. We'll give you a straight answer, even if that answer is "not yet." We'd rather be honest upfront than sign a client who isn't a fit.</p>
    </details>
  </div>
</section>

<section class="closing" id="call">
  <div class="wrap">
    <h2>Still Have a Question?</h2>
    <p>Ask it directly on a call. 15 minutes, no pressure.</p>
    <div class="actions" style="justify-content:center; display:flex; gap:14px; flex-wrap:wrap">
      <a class="btn btn-primary" href="/pricing/#call">Book a Strategy Call</a>
    </div>
  </div>
</section>'''
    write("faq/index.html", page(
        "FAQ | Combat Boost",
        "Answers to the most common questions about Combat Boost's website, review & referral automation, and follow-up system for martial arts schools.",
        "/faq/", "/faq/", body))


if __name__ == "__main__":
    print("Building Combat Boost multi-page site...")
    build_homepage()
    build_pricing()
    build_results()
    build_about()
    build_faq()
    print("Done.")
