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
    ("/case-studies/", "Case Studies"),
    ("/pricing/", "Pricing"),
    ("/faq/", "FAQ"),
    ("/about/", "About"),
]

LOGO_SVG = '''<svg width="{size}" height="{size}" viewBox="0 0 100 100" aria-hidden="true">
        <path d="M50 6 L90 78 Q50 58 10 78 Z" fill="none" stroke="#C9972B" stroke-width="{sw}" stroke-linejoin="round"/>
        <circle cx="50" cy="30" r="9" fill="#C9972B"/>
      </svg>'''


def head(title, description, canonical_path):
    return f'''<!doctype html>
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
    return f'''<div class="concept-banner"><b>CONCEPT</b> — multi-page structure for internal review, built from the locked rebuild brief. Not the production site.</div>

<div class="wrap">
  <header>
    <a class="brand" href="/">
      {LOGO_SVG.format(size=34, sw=7)}
      <span class="brand-word">Combat<span>Boost</span></span>
    </a>
    <div class="header-actions">
      <nav class="main" id="main-nav">
        <a class="btn btn-gold mobile-cta" href="/pricing/#call">Book a Strategy Call</a>
{nav_links}
      </nav>
      <a class="btn btn-gold" href="/pricing/#call">Book a Strategy Call</a>
      <button class="nav-toggle" id="nav-toggle" aria-label="Toggle menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>
</div>'''


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
          {LOGO_SVG.format(size=26, sw=8)}
          <span class="brand-word">Combat<span>Boost</span></span>
        </div>
        <p>Websites, review &amp; referral automation, and AI follow-up — built exclusively for martial arts schools.</p>
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
          <li><a href="/about/">About</a></li>
          <li><a href="/case-studies/">Case Studies</a></li>
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
    with open(full, "w") as f:
        f.write(content)
    print(f"  wrote {rel_path}  ({len(content):,} bytes)")


# ============================================================
# HOMEPAGE
# ============================================================
def build_homepage():
    import base64
    imgs = {}
    for key, fname in [
        ("before-clifton", "assets/images/before-clifton.jpg"),
        ("after-clifton", "assets/images/after-clifton.jpg"),
    ]:
        imgs[key] = f"/{fname}"

    body = f'''<section class="hero" id="top">
  <div class="wrap hero-grid">
    <div>
      <h1>Your Reviews Are Already<br>Bringing People In.<br><em>Your Website Is Losing Them.</em></h1>
      <p class="dek">We build the website, the review &amp; referral system, and the follow-up that turns the traffic you already have into booked intro classes — before you spend another dollar on ads.</p>
      <div class="actions">
        <a class="btn btn-gold" href="/pricing/#call">Book a Strategy Call</a>
        <a class="btn btn-ghost-dark" href="#how-it-works">See How It Works</a>
      </div>
      <p class="stat-line">Worked with <b>50+</b> martial arts schools. Real names, real numbers below ↓</p>
    </div>
    <div class="ba-compare">
      <div class="ba-label before"><span class="tag"></span>Before — the school's actual old site</div>
      <div class="ba-frame">
        <div class="ba-chrome"><span class="ba-dot"></span><span class="ba-dot"></span><span class="ba-dot"></span><span class="ba-url">cliftonmartialarts.com</span></div>
        <img src="{imgs['before-clifton']}" alt="A real client's old website before Combat Boost, live as of this build" loading="lazy">
      </div>
      <div class="ba-after">
        <div class="ba-label after"><span class="tag"></span>After — built by Combat Boost</div>
        <div class="ba-frame">
          <div class="ba-chrome"><span class="ba-dot"></span><span class="ba-dot"></span><span class="ba-dot"></span><span class="ba-url">cliftonmartialarts.com</span></div>
          <img src="{imgs['after-clifton']}" alt="The same school's site after the Combat Boost rebuild" loading="lazy">
        </div>
      </div>
      <p class="ba-cap">Real client, real rebuild — Clifton Martial Arts Academy, Clifton, NJ. <a href="/case-studies/" style="color:var(--gold-bright)">See more case studies →</a></p>
    </div>
  </div>
</section>

<div class="proof">
  <div class="wrap proof-inner">
    <div class="proof-lede"><b>50+</b><span>schools worked with —<br>including:</span></div>
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

<section class="quote-banner">
  <div class="wrap">
    <p class="q">My stress level has went down... the door's been swinging open, and I've been happy seeing the people come in.</p>
    <p class="attr">— <b>Dan Carey</b>, real client, on the change after launch</p>
  </div>
</section>

<section class="on-light" id="how-it-works">
  <div class="wrap">
    <div class="section-head">
      <h2>Fix the Four Things Actually Costing You Students.</h2>
      <p>Not four separate products — one connected system. Here's the honest before/after, including the past-member list most schools have written off.</p>
    </div>
    <div class="tableWrap">
      <table class="baTable">
        <thead>
          <tr><th>Area</th><th>Before</th><th>After</th></tr>
        </thead>
        <tbody>
          <tr>
            <td>Website</td>
            <td><span class="mark bad">Looks fine, converts almost nobody</span></td>
            <td><span class="mark good">Built to turn visitors into booked intros</span></td>
          </tr>
          <tr>
            <td>Reviews &amp; Referrals</td>
            <td><span class="mark bad">A handful of old reviews, no referral flow</span></td>
            <td><span class="mark good">Reviews and referrals requested automatically, after every win</span></td>
          </tr>
          <tr>
            <td>Follow-Up</td>
            <td><span class="mark bad">New leads texted back "when there's time"</span></td>
            <td><span class="mark good">Every lead followed up within minutes, every time</span></td>
          </tr>
          <tr class="reactivation-row">
            <td>Past Members</td>
            <td><span class="mark bad">Sitting cold in an old spreadsheet or CRM</span></td>
            <td><span class="mark good">Re-engaged on autopilot — some come back and re-enroll</span></td>
          </tr>
          <tr>
            <td>Your Time</td>
            <td><span class="mark bad">Chasing leads between classes</span></td>
            <td><span class="mark good">Teaching. The system chases for you</span></td>
          </tr>
        </tbody>
      </table>
    </div>
    <p style="margin-top:22px; font-size:14.5px; color:var(--tx-light-soft); max-width:60ch">On the "Follow-Up" row, in Dan Carey's own words: <i>"The communication, the system's pretty simple. I get an alert that someone's been signed up... it helps with welcoming people in."</i></p>
  </div>
</section>

<section id="what-happens-next">
  <div class="wrap">
    <div class="section-head">
      <p class="lede">The website gets people in the door. Here's what happens next.</p>
      <h2>Turn First Visits Into Long-Term Members.</h2>
    </div>
    <div class="feature-strip">
      <span>Review &amp; Referral Requests</span>
      <span>Automated New-Lead Follow-Up</span>
      <span>Past-Member Reactivation</span>
      <span>Managed Ads <i>(optional)</i></span>
    </div>
    <div class="neg-space">
      <p><b>No</b> more guessing which leads went cold.</p>
      <p><b>No</b> more manually chasing down phone numbers between classes.</p>
      <p><b>No</b> more losing a sign-up because the follow-up came a day too late.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap video-block">
    <div>
      <div class="video-card">
        <div class="play" aria-hidden="true"></div>
        <span class="vc-cap">▶ 2:14 — Dan Carey, real client (permission granted)</span>
      </div>
    </div>
    <div class="video-quote">
      <p class="q">"I think I waited too long <span>— but it was the right time when we were able to team up.</span> I would definitely make the investment, because it's going to come back to you."</p>
      <p class="attr">— Dan Carey, on deciding to sign up</p>
      <div class="woven-stat">
        <span class="ws-num">+9</span>
        <span class="ws-txt">past members reactivated on average per school, from one automated win-back sequence.</span>
      </div>
    </div>
  </div>
</section>

<section class="closing" id="cta">
  <div class="wrap">
    <h2>Ready to Stop Losing<br>the Traffic You Already Have?</h2>
    <p>See exactly what's included and book a call — no pricing number posted here, because every school's setup is a little different and we'd rather talk it through than post a number that doesn't fit you.</p>
    <div class="actions" style="justify-content:center; display:flex; gap:14px; flex-wrap:wrap">
      <a class="btn btn-gold" href="/pricing/#call">Book a Strategy Call</a>
      <a class="btn btn-ghost-dark" href="/case-studies/">See the Work First</a>
    </div>
  </div>
</section>'''
    write("index.html", page(
        "Combat Boost — Websites, Reviews & Follow-Up for Martial Arts Schools",
        "Combat Boost builds websites, review & referral automation, and AI follow-up for martial arts schools — worked with 50+ schools, before you spend another dollar on ads.",
        "/", "/", body))


# ============================================================
# PRICING
# ============================================================
def build_pricing():
    body = '''<section class="page-hero">
  <div class="wrap">
    <a class="crumb" href="/">&larr; Back to Home</a>
    <h1>One Flat Monthly Rate.<br>No Per-Location Surprises.</h1>
    <p class="dek">We don't publish a number here — every school's setup is a little different, and we'd rather walk you through your exact fit on a call than post a figure that doesn't apply to you. Here's exactly what's included either way.</p>
  </div>
</section>

<section class="on-light" style="padding-top:0">
  <div class="wrap">
    <div class="included-list">
      <div class="included-item">
        <h3>The Website</h3>
        <p>A real, built-to-convert website for your school — not a template with your logo dropped in. This is the core deliverable and where most of the build time goes.</p>
      </div>
      <div class="included-item">
        <h3>Reviews &amp; Referrals</h3>
        <p>Automated requests sent after every win, so your Google reviews and referrals grow on their own instead of depending on you remembering to ask.</p>
      </div>
      <div class="included-item">
        <h3>Follow-Up &amp; Reactivation</h3>
        <p>Every new lead followed up within minutes, and your existing past-member list re-engaged on autopilot — not left cold in an old spreadsheet or CRM.</p>
      </div>
      <div class="included-item">
        <h3>Managed Ads <span class="tag-optional">Optional Add-On</span></h3>
        <p>Once the site, reviews, and follow-up are converting what you already have, we'll run Google/Facebook ads for you if it makes sense — never the starting point.</p>
      </div>
    </div>

    <div style="margin-top:56px; max-width:640px">
      <h2 style="font-size:26px">Why no number?</h2>
      <p style="margin-top:14px; font-size:15.5px; color:var(--tx-light-soft)">Single-location schools, multi-location franchises, and schools coming off an existing website all need a slightly different scope of work — posting one flat number here would either overcharge the simple cases or undersell the complex ones. On the call, we'll tell you the real number for your specific school, honestly, before you commit to anything.</p>
    </div>
  </div>
</section>

<section class="closing" id="call">
  <div class="wrap">
    <h2>Get Your Exact Number.</h2>
    <p>15 minutes, no pressure — we'll look at your current site and tell you honestly whether a rebuild is the right move yet.</p>
    <div class="actions" style="justify-content:center; display:flex; gap:14px; flex-wrap:wrap">
      <a class="btn btn-gold" href="#">Book a Strategy Call</a>
      <a class="btn btn-ghost-dark" href="/case-studies/">See the Work First</a>
    </div>
  </div>
</section>'''
    write("pricing/index.html", page(
        "Pricing — Combat Boost",
        "What's included in Combat Boost's website, reviews & referrals, and follow-up & reactivation system for martial arts schools. Book a call for your exact rate.",
        "/pricing/", "/pricing/", body))


# ============================================================
# CASE STUDIES INDEX
# ============================================================
def build_case_studies_index():
    body = '''<section class="page-hero">
  <div class="wrap">
    <a class="crumb" href="/">&larr; Back to Home</a>
    <h1>A Few of the 50+.</h1>
    <p class="dek">Real schools we've worked with — single-location dojos and multi-location franchises alike. More full write-ups are added as client material comes in.</p>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">

    <div class="story-row">
      <img class="story-shot" src="/assets/images/casestudy-strikerlab.jpg" alt="Striker Lab Muay Thai Kickboxing — the actual site Combat Boost built">
      <div>
        <span class="story-tag">New Location</span>
        <h3>Striker Lab Muay Thai Kickboxing</h3>
        <p>A brand-new studio's first 90 days — the site was built and live before the doors even opened.</p>
        <a class="story-link" href="#">Full case study — coming soon</a>
      </div>
    </div>

    <div class="story-row">
      <div class="story-noshot">Real client<br>(video testimonial)</div>
      <div>
        <span class="story-tag">Real Client Story</span>
        <h3>Dan Carey</h3>
        <p>"My stress level has went down... the door's been swinging open, and I've been happy seeing the people come in." A real client on what changed after launch, in his own words.</p>
        <a class="story-link" href="/case-studies/dan-carey/">Read Dan's story →</a>
      </div>
    </div>

    <div class="story-row">
      <div class="story-noshot">Case study<br>coming soon</div>
      <div>
        <span class="story-tag">Multi-Location</span>
        <h3>Moore's Karate</h3>
        <p>13 locations across California, one consistent site and follow-up system across every one.</p>
        <a class="story-link" href="#">Full case study — coming soon</a>
      </div>
    </div>

    <div class="story-row">
      <div class="story-noshot">Case study<br>coming soon</div>
      <div>
        <span class="story-tag">Single Location, BJJ</span>
        <h3>Camal &amp; Cruz Judo &amp; BJJ</h3>
        <p>A one-location academy competing for attention against bigger, better-funded gyms nearby.</p>
        <a class="story-link" href="#">Full case study — coming soon</a>
      </div>
    </div>

  </div>
</section>

<section class="closing" id="call">
  <div class="wrap">
    <h2>Want to See More Like This?</h2>
    <p>Book a call and we'll walk you through more of the 50+, including ones closest to your school's size and situation.</p>
    <div class="actions" style="justify-content:center; display:flex; gap:14px; flex-wrap:wrap">
      <a class="btn btn-gold" href="/pricing/#call">Book a Strategy Call</a>
    </div>
  </div>
</section>'''
    write("case-studies/index.html", page(
        "Case Studies — Combat Boost",
        "Real martial arts schools Combat Boost has worked with — single-location dojos and multi-location franchises, with real client stories.",
        "/case-studies/", "/case-studies/", body))


# ============================================================
# CASE STUDY: DAN CAREY
# ============================================================
def build_case_study_dan_carey():
    body = '''<section class="page-hero">
  <div class="wrap" style="max-width:760px">
    <a class="crumb" href="/case-studies/">&larr; Back to Case Studies</a>
    <span class="story-tag">Real Client Story</span>
    <h1 style="margin-top:10px">Dan Carey</h1>
    <p class="dek">A real Combat Boost client, in his own words — permission granted to share his story here.</p>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap" style="max-width:760px">
    <div class="video-card" style="margin-bottom:36px">
      <div class="play" aria-hidden="true"></div>
      <span class="vc-cap">▶ 2:14 — Dan Carey, real client (permission granted)</span>
    </div>

    <p style="font-size:15.5px; color:var(--tx-dark-soft)">Before working with Combat Boost, Dan was doing what most school owners end up doing: running the school and chasing the marketing side of it himself, in whatever time was left over. Here's what he said changed after launch.</p>

    <p class="story-quote">"My stress level has went down... the door's been swinging open, and I've been happy seeing the people come in."</p>

    <p style="font-size:15.5px; color:var(--tx-dark-soft)">On the day-to-day system itself — the alerts and follow-up that run in the background once a new lead comes in:</p>

    <p class="story-quote">"The communication, the system's pretty simple. I get an alert that someone's been signed up... it helps with welcoming people in."</p>

    <p style="font-size:15.5px; color:var(--tx-dark-soft)">And on deciding to actually make the investment, after putting it off for a while:</p>

    <p class="story-quote">"I think I waited too long — but it was the right time when we were able to team up. I would definitely make the investment, because it's going to come back to you."</p>

    <div class="woven-stat" style="margin-top:40px">
      <span class="ws-num">+9</span>
      <span class="ws-txt">past members reactivated on average per school, from one automated win-back sequence — the same system running for Dan's school.</span>
    </div>
  </div>
</section>

<section class="closing" id="call">
  <div class="wrap">
    <h2>Want a Story Like This for Your School?</h2>
    <p>Book a call and we'll show you exactly what the system Dan's describing would look like for your school.</p>
    <div class="actions" style="justify-content:center; display:flex; gap:14px; flex-wrap:wrap">
      <a class="btn btn-gold" href="/pricing/#call">Book a Strategy Call</a>
      <a class="btn btn-ghost-dark" href="/case-studies/">See More Stories</a>
    </div>
  </div>
</section>'''
    write("case-studies/dan-carey/index.html", page(
        "Dan Carey — Case Study — Combat Boost",
        "A real Combat Boost client, in his own words, on what changed after launching his website, review & referral automation, and follow-up system.",
        "/case-studies/dan-carey/", "/case-studies/", body))


# ============================================================
# ABOUT
# ============================================================
def build_about():
    body = '''<section class="page-hero">
  <div class="wrap">
    <a class="crumb" href="/">&larr; Back to Home</a>
    <h1>We Only Work With Martial Arts Schools.</h1>
    <p class="dek">Not gyms in general, not "local businesses" — martial arts schools specifically.</p>
  </div>
</section>

<section class="on-light2" style="padding-top:0">
  <div class="wrap about-grid">
    <div>
      <img class="about-photo" src="/assets/images/about-photo.jpg" alt="A real Combat Boost client, mid-class" loading="lazy">
      <p class="about-cap">One of the 50+ schools we've worked with, mid-class.</p>
    </div>
    <div class="about-copy">
      <p style="font-size:15.5px; color:var(--tx-light-soft)">A belt-testing schedule, a trial-class funnel, and a parent's decision process don't look like anything else we could serve instead — so rather than build a generic small-business playbook and put a karate photo on top of it, we only work in this one industry.</p>
      <p style="font-size:15.5px; color:var(--tx-light-soft)">Everything on this site is built from what's actually worked across <span class="stat-inline">50+</span> real school launches — from single-location dojos to multi-location franchises. One system: the website, the review &amp; referral automation, and the follow-up, sold as one connected build, not separate add-ons.</p>
      <p style="font-size:15.5px; color:var(--tx-light-soft)">The core belief behind how we sequence the work: most schools are already getting real traffic — from Google, from reviews, from word of mouth. The website's job is to actually convert that traffic before spending anything on ads to get more of it.</p>
    </div>
  </div>
</section>

<section class="closing" id="call">
  <div class="wrap">
    <h2>Let's Talk About Your School.</h2>
    <p>Book a call and we'll tell you honestly where the biggest gap is for you right now.</p>
    <div class="actions" style="justify-content:center; display:flex; gap:14px; flex-wrap:wrap">
      <a class="btn btn-gold" href="/pricing/#call">Book a Strategy Call</a>
      <a class="btn btn-ghost-dark" href="/case-studies/">See the Work</a>
    </div>
  </div>
</section>'''
    write("about/index.html", page(
        "About — Combat Boost",
        "Combat Boost only works with martial arts schools — websites, review & referral automation, and follow-up, built from what's worked across 50+ real school launches.",
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
      <p>No — if ads are working for you, keep running them. Our point is sequencing, not opposition: fix what converts the traffic you already get first, then ads go further with every dollar. We also build and run ads ourselves once that foundation is in place — see Pricing for how that fits in.</p>
    </details>
    <details class="faq-item">
      <summary>I already have a website. Do I need a new one?</summary>
      <p>Usually, yes — most schools' sites were built once and never touched again. We'll tell you honestly on the call if a rebuild isn't the highest-leverage move for you yet.</p>
    </details>
    <details class="faq-item">
      <summary>How long does it take to launch?</summary>
      <p>Most schools are live within a few weeks of kickoff, site and automation together — not a six-month agency timeline.</p>
    </details>
    <details class="faq-item">
      <summary>What's actually included?</summary>
      <p>The website, the review &amp; referral automation, and the lead follow-up + past-member reactivation system — one build, one monthly rate, no separate tools to stitch together yourself. Full breakdown on the Pricing page.</p>
    </details>
    <details class="faq-item">
      <summary>Is there a contract?</summary>
      <p>We'll cover the specifics on the call — happy to be direct about it rather than bury it in fine print here.</p>
    </details>
    <details class="faq-item">
      <summary>Do you work with multi-location schools?</summary>
      <p>Yes — several of the 50+ schools we've worked with run multiple locations under one brand, including a 13-location California franchise. See Case Studies.</p>
    </details>
    <details class="faq-item">
      <summary>What if I'm not sure a rebuild is worth it yet?</summary>
      <p>Ask on the call — we'll give you a straight answer, even if that answer is "not yet." We'd rather be honest upfront than sign a client who isn't a fit.</p>
    </details>
  </div>
</section>

<section class="closing" id="call">
  <div class="wrap">
    <h2>Still Have a Question?</h2>
    <p>Ask it directly on a call — 15 minutes, no pressure.</p>
    <div class="actions" style="justify-content:center; display:flex; gap:14px; flex-wrap:wrap">
      <a class="btn btn-gold" href="/pricing/#call">Book a Strategy Call</a>
    </div>
  </div>
</section>'''
    write("faq/index.html", page(
        "FAQ — Combat Boost",
        "Answers to the most common questions about Combat Boost's website, review & referral automation, and follow-up system for martial arts schools.",
        "/faq/", "/faq/", body))


if __name__ == "__main__":
    print("Building Combat Boost multi-page site...")
    build_homepage()
    build_pricing()
    build_case_studies_index()
    build_case_study_dan_carey()
    build_about()
    build_faq()
    print("Done.")
