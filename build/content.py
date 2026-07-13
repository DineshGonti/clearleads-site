# -*- coding: utf-8 -*-
"""Page content + copy for ClearLeads. Consumed by build.py."""
import build as b
from build import (page, cta_band, faq_block, faq_schema, arrow, ICONS,
                   SERVICES, svc_icon_html, BOOK, SITE, NAME)

A = arrow()

# ------------------------------------------------------------------
# Reusable sections
# ------------------------------------------------------------------
def logos_strip():
    names = ["Northwind", "Vertex SaaS", "BluePeak", "Ledgerly", "Orbit HR", "Cascade"]
    return f'''<section class="section-tight bg-soft">
  <div class="container center">
    <p class="eyebrow" style="margin-bottom:22px">Trusted by revenue teams at growing B2B companies</p>
    <div class="logos">{''.join(f'<span>{n}</span>' for n in names)}</div>
  </div>
</section>'''

def stat_band(dark=True, items=None):
    items = items or [
        ("12,000+", "Meetings booked for clients"),
        ("38%", "Average positive reply lift"),
        ("14 days", "To first booked meetings"),
        ("4.9/5", "Client satisfaction rating"),
    ]
    cls = "bg-navy" if dark else "bg-soft"
    cells = "".join(
        f'<div class="stat"><div class="num">{n}</div><div class="lbl">{l}</div></div>'
        for n, l in items
    )
    return f'''<section class="{cls}"><div class="container"><div class="stats">{cells}</div></div></section>'''

def process_steps(prefix=""):
    steps = [
        ("Map your ICP & offer", "We define your ideal customer profile, sharpen your positioning, and build a targeted prospect list of decision-makers who fit."),
        ("Build the outbound engine", "We set up dedicated sending infrastructure, warm inboxes, write channel-specific copy, and configure LinkedIn — engineered for the inbox, not the spam folder."),
        ("Launch & book meetings", "Sequences go live across email and LinkedIn. We handle every reply, qualify interest, and book meetings straight onto your calendar."),
        ("Optimise & scale", "We report weekly on real numbers, A/B test messaging and lists, and scale what converts so your pipeline keeps compounding."),
    ]
    cells = ""
    for i, (t, d) in enumerate(steps, 1):
        cells += f'<div class="step"><div class="n">{i}</div><h3>{t}</h3><p>{d}</p></div>'
    return f'''<section>
  <div class="container">
    <div class="section-head"><span class="eyebrow">How it works</span>
      <h2>From zero to booked meetings in four steps</h2>
      <p>A transparent, done-for-you system. You approve the strategy — we run the machine and fill your calendar.</p></div>
    <div class="steps grid-4">{cells}</div>
    <div class="center mt-3"><a href="{prefix}how-it-works.html" class="btn btn-ghost">See the full process {A}</a></div>
  </div>
</section>'''

def testimonial_row():
    quotes = [
        ("ClearLeads booked 22 qualified meetings in our first month. Two are already in procurement. It paid for itself before the first invoice cleared.",
         "SM", "Sarah Mitchell", "VP Sales, Vertex SaaS"),
        ("We tried building outbound in-house for a year and stalled. ClearLeads had us live in two weeks and our reply rate tripled.",
         "DR", "David Reyes", "Founder, BluePeak"),
        ("The reporting is refreshingly honest — real numbers every week, no vanity metrics. Our SDR cost per meeting dropped by half.",
         "AK", "Aisha Khan", "Head of Growth, Ledgerly"),
    ]
    cells = ""
    for txt, ini, name, role in quotes:
        cells += f'''<div class="quote">
          <div class="stars">★★★★★</div>
          <p>“{txt}”</p>
          <div class="who"><div class="avatar">{ini}</div><div><b>{name}</b><small>{role}</small></div></div>
        </div>'''
    return f'''<section class="bg-soft">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Client results</span><h2>Teams that stopped chasing and started closing</h2></div>
    <div class="grid grid-3">{cells}</div>
  </div>
</section>'''

def why_us():
    items = [
        ("shield", "No long lock-in", "Month-to-month after an initial ramp. We earn the renewal with booked meetings, not contracts."),
        ("chart", "Transparent reporting", "A live dashboard and a weekly numbers call. You see every send, reply, and meeting — no black box."),
        ("target", "Only qualified meetings", "We book prospects that match your ICP and show real intent. No-shows and junk leads don't count."),
        ("bolt", "Live in ~14 days", "Infrastructure, copy, and lists ready in two weeks — not the two months an in-house build takes."),
    ]
    cells = ""
    for ico, t, d in items:
        cells += f'''<div class="card"><div class="ico">{ICONS[ico]}</div><h3>{t}</h3><p>{d}</p></div>'''
    return f'''<section>
  <div class="container">
    <div class="section-head"><span class="eyebrow">Why ClearLeads</span><h2>The outbound partner that acts like it's on your team</h2>
      <p>Everything is built to book qualified meetings and prove it with numbers you can trust.</p></div>
    <div class="grid grid-4">{cells}</div>
  </div>
</section>'''

def related_services(current):
    others = [s for s in SERVICES if s[0] != current][:3]
    cells = ""
    for slug, title, desc, _ in others:
        cells += f'''<a class="card" href="{slug}.html" style="text-decoration:none">
          {svc_icon_html(slug)}<h3>{title}</h3><p>{desc}</p>
          <span class="learn">Explore {A}</span></a>'''
    return f'''<section class="bg-soft">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Related services</span><h2>Build a complete outbound system</h2></div>
    <div class="grid grid-3">{cells}</div>
  </div>
</section>'''

# ------------------------------------------------------------------
# HOME
# ------------------------------------------------------------------
def build_home():
    svc_cards = ""
    for slug, title, desc, flag in SERVICES:
        tag = '<span class="flag-tag">Flagship</span>' if flag else ''
        cls = "card flag" if flag else "card"
        svc_cards += f'''<a class="{cls}" href="{slug}.html" style="text-decoration:none">
          {tag}{svc_icon_html(slug)}<h3>{title}</h3><p>{desc}</p>
          <span class="learn">Learn more {A}</span></a>'''

    faqs = [
        ("What does a B2B lead generation agency actually do?",
         "<p>A B2B lead generation agency runs outbound prospecting on your behalf — building targeted lists, writing and sending cold email and LinkedIn messages, and booking qualified sales meetings directly onto your calendar. ClearLeads owns the full top-of-funnel so your closers spend their time selling, not prospecting.</p>"),
        ("How is a “qualified meeting” defined?",
         "<p>A qualified meeting is a scheduled call with a decision-maker who matches your ideal customer profile and has expressed genuine interest in your offer. We agree the qualification criteria with you up front, and no-shows within our control are replaced free.</p>"),
        ("How quickly will I see booked meetings?",
         "<p>Most clients are live within 14 days and see their first booked meetings inside the first 2–4 weeks, once inbox warm-up and sequencing hit full volume. Pipeline compounds from there as we optimise messaging and lists.</p>"),
        ("Do I need long-term contracts?",
         "<p>No. After an initial ramp period we operate month-to-month. We'd rather keep your business by booking meetings than by locking you into a contract.</p>"),
        ("Which industries do you work with?",
         "<p>We focus on B2B companies with a defined ICP and a real sales motion — SaaS, agencies, professional services, recruiting, and B2B services. If you sell to other businesses and know who your buyer is, outbound can work for you.</p>"),
    ]
    body = f'''
<section class="hero hero-dark">
  <div class="container hero-inner">
    <div class="hero-grid">
      <div>
        <span class="eyebrow on-dark">B2B Lead Generation Agency</span>
        <h1>Book more qualified sales meetings — <span class="grad">without hiring an SDR team</span></h1>
        <p class="hero-sub">ClearLeads is a done-for-you outbound agency. We build the system, run cold email and LinkedIn outreach, and drop qualified meetings straight onto your calendar. You just show up and close.</p>
        <div class="hero-cta">
          <a href="{BOOK}" class="btn btn-primary btn-lg">Book a call {A}</a>
          <a href="results.html" class="btn btn-ghost on-dark btn-lg">See the results</a>
        </div>
        <div class="hero-trust"><span class="dot"></span> Live in ~14 days <span class="dot"></span> No long lock-in <span class="dot"></span> Only pay for qualified meetings</div>
      </div>
      <div class="hero-card">
        <div class="cap">This week · booked meetings</div>
        <div class="row"><div class="who"><div class="avatar">RT</div><div><b>R. Tanaka — CFO</b><small>Northwind · SaaS</small></div></div><span class="pill booked">Booked</span></div>
        <div class="row"><div class="who"><div class="avatar">JM</div><div><b>J. Miller — VP Ops</b><small>Cascade · Logistics</small></div></div><span class="pill booked">Booked</span></div>
        <div class="row"><div class="who"><div class="avatar">EP</div><div><b>E. Park — Head of IT</b><small>Orbit HR · HR Tech</small></div></div><span class="pill booked">Booked</span></div>
        <div class="row"><div class="who"><div class="avatar">LC</div><div><b>L. Chen — Director</b><small>Ledgerly · Fintech</small></div></div><span class="pill booked">Booked</span></div>
      </div>
    </div>
  </div>
</section>

{logos_strip()}

<section>
  <div class="container narrow">
    <div class="section-head left"><span class="eyebrow">What we do</span><h2>Qualified meetings, booked for you</h2></div>
    <p class="answer"><strong>ClearLeads is a B2B lead generation agency that books qualified sales meetings for you.</strong> We build targeted prospect lists, run cold email and LinkedIn outreach from your brand, handle every reply, and schedule interested decision-makers directly onto your calendar — so your team can focus entirely on closing revenue.</p>
  </div>
</section>

{stat_band()}

<section>
  <div class="container">
    <div class="section-head"><span class="eyebrow">Services</span><h2>Everything you need to fill the pipeline</h2>
      <p>Start with appointment setting, or plug in individual services to strengthen the outbound system you already run.</p></div>
    <div class="grid grid-3">{svc_cards}</div>
  </div>
</section>

{process_steps()}

<section class="bg-navy">
  <div class="container">
    <div class="split">
      <div class="txt">
        <span class="eyebrow on-dark">Proof, not promises</span>
        <h2>We report the numbers that actually matter</h2>
        <p>No vanity metrics. Every week you get a live view of sends, reply rates, and — the only number that pays the bills — meetings booked. Here's a snapshot from a typical SaaS engagement.</p>
        <a href="results.html" class="btn btn-primary mt-1">Read the case studies {A}</a>
      </div>
      <div class="panel">
        <div class="metric-row"><span class="k">Prospects contacted / mo</span><span class="v">3,200</span></div>
        <div class="metric-row"><span class="k">Positive reply rate</span><span class="v"><em>7.4%</em></span></div>
        <div class="metric-row"><span class="k">Qualified meetings booked / mo</span><span class="v"><em>24</em></span></div>
        <div class="metric-row"><span class="k">Cost per qualified meeting</span><span class="v">↓ 51%</span></div>
        <div class="metric-row"><span class="k">Pipeline influenced (Q1)</span><span class="v">$740k</span></div>
      </div>
    </div>
  </div>
</section>

{why_us()}
{testimonial_row()}
{faq_block(faqs)}
{cta_band()}
'''
    page("index.html",
         "ClearLeads | B2B Lead Generation Agency & Appointment Setting",
         "ClearLeads is a B2B lead generation agency that books qualified sales meetings on your calendar via done-for-you cold email and LinkedIn outreach. Live in 14 days. Book a call.",
         body, schemas=[faq_schema(faqs)], canonical=f"{SITE}/")

# ------------------------------------------------------------------
# SERVICES OVERVIEW
# ------------------------------------------------------------------
def build_services():
    cards = ""
    for slug, title, desc, flag in SERVICES:
        tag = '<span class="flag-tag">Flagship</span>' if flag else ''
        cls = "card flag" if flag else "card"
        cards += f'''<a class="{cls}" href="{slug}.html" style="text-decoration:none">
          {tag}{svc_icon_html(slug)}<h3>{title}</h3><p>{desc}</p>
          <span class="learn">Learn more {A}</span></a>'''
    faqs = [
        ("What's the difference between appointment setting and lead generation?",
         "<p>Lead generation is the broad practice of finding and engaging potential buyers. Appointment setting is the outcome-focused end of it: qualifying those prospects and booking them as sales meetings. ClearLeads does both, but we're measured on meetings booked, not leads collected.</p>"),
        ("Can I buy just one service, like lead lists?",
         "<p>Yes. Lead list building and data is a popular standalone entry point. You can also add cold email, LinkedIn, or database reactivation individually, or combine them into a full outbound system.</p>"),
        ("Do you replace or complement our in-house SDRs?",
         "<p>Either. Many clients use us as their entire outbound engine; others use us to add capacity, test new segments, or cover channels their SDRs don't run. We integrate with your CRM and calendar either way.</p>"),
    ]
    body = f'''
<div class="container crumb"><a href="index.html">Home</a> / Services</div>
<section class="hero">
  <div class="container hero-inner" style="padding-top:48px">
    <div class="narrow">
      <span class="eyebrow">Services</span>
      <h1>Outbound lead generation & sales development services</h1>
      <p class="lede mt-1">Outsourced SDR services for B2B teams. Pick the flagship appointment-setting offer, or assemble the exact outbound system your pipeline needs — every service is built to book qualified meetings.</p>
      <div class="hero-cta mt-2"><a href="{BOOK}" class="btn btn-primary btn-lg">Book a call {A}</a>
        <a href="how-it-works.html" class="btn btn-ghost btn-lg">How it works</a></div>
    </div>
  </div>
</section>
<section>
  <div class="container narrow">
    <p class="answer"><strong>ClearLeads offers outsourced sales development and appointment-setting services for B2B companies.</strong> Our services span appointment setting, done-for-you cold email, LinkedIn outreach, verified lead-list building, database reactivation, and one-time outbound system setup — delivered as a managed service and measured on qualified meetings booked.</p>
  </div>
</section>
<section class="section-tight">
  <div class="container"><div class="grid grid-3">{cards}</div></div>
</section>
{stat_band(dark=False)}
{why_us()}
{faq_block(faqs)}
{cta_band()}
'''
    page("services.html",
         "B2B Lead Generation & SDR Services | ClearLeads",
         "Outsourced SDR and lead generation services: appointment setting, cold email, LinkedIn outreach, lead lists, and database reactivation. Book qualified B2B meetings.",
         body, schemas=[faq_schema(faqs)])

# ------------------------------------------------------------------
# SERVICE PAGE TEMPLATE
# ------------------------------------------------------------------
def service_page(slug, title, h1, seo_title, meta, answer, included, metrics, whofor, faqs, price=None):
    inc = "".join(f'<li>{i}</li>' for i in included)
    met = "".join(
        f'<div class="metric-row"><span class="k">{k}</span><span class="v">{v}</span></div>' for k, v in metrics
    )
    who = "".join(f'<li>{w}</li>' for w in whofor)
    service_schema = {
        "@context": "https://schema.org", "@type": "Service",
        "serviceType": title, "name": f"{title} — {NAME}",
        "provider": {"@type": "Organization", "name": NAME, "url": SITE},
        "areaServed": "Global", "description": b.strip_tags(answer),
        "url": f"{SITE}/{slug}",
    }
    price_html = ""
    if price:
        price_html = f'''<div class="callout" style="margin-top:26px">
          <strong style="color:var(--ink)">Typical investment:</strong> {price}
          <a href="{BOOK}" style="margin-left:8px">Get a custom quote {A}</a></div>'''
    body = f'''
<div class="container crumb"><a href="index.html">Home</a> / <a href="services.html">Services</a> / {title}</div>
<section class="hero">
  <div class="container hero-inner" style="padding-top:46px;padding-bottom:56px">
    <div class="narrow">
      {svc_icon_html(slug)}
      <span class="eyebrow" style="margin-top:14px">{title}</span>
      <h1>{h1}</h1>
      <p class="lede mt-1">{meta}</p>
      <div class="hero-cta mt-2"><a href="{BOOK}" class="btn btn-primary btn-lg">Book a call {A}</a>
        <a href="results.html" class="btn btn-ghost btn-lg">See results</a></div>
    </div>
  </div>
</section>

<section>
  <div class="container narrow">
    <p class="answer">{answer}</p>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="split">
      <div class="txt">
        <span class="eyebrow">What's included</span>
        <h2>Done for you, end to end</h2>
        <ul class="checks mt-2">{inc}</ul>
        {price_html}
      </div>
      <div class="panel">
        <div class="cap" style="color:var(--muted);font-size:.8rem;letter-spacing:.04em;text-transform:uppercase;font-weight:700;margin-bottom:8px">Representative results</div>
        {met}
      </div>
    </div>
  </div>
</section>

{process_steps()}

<section class="bg-soft">
  <div class="container narrow">
    <span class="eyebrow">Who it's for</span>
    <h2>A great fit if…</h2>
    <ul class="checks mt-2">{who}</ul>
  </div>
</section>

{faq_block(faqs)}
{related_services(slug)}
{cta_band()}
'''
    page(f"{slug}.html", seo_title, meta, body,
         schemas=[service_schema, faq_schema(faqs)])

# ---- individual service content ----
def build_services_detail():
    service_page(
        "appointment-setting", "Appointment Setting",
        "Appointment setting services that book qualified B2B meetings",
        "Appointment Setting Services & Company | ClearLeads",
        "Done-for-you appointment setting services. We book qualified B2B sales meetings straight to your calendar via multi-channel outreach. Only pay for meetings that matter.",
        "<strong>Appointment setting is a done-for-you service where we book qualified sales meetings directly onto your calendar.</strong> ClearLeads identifies decision-makers who fit your ICP, reaches them across email and LinkedIn, handles every reply, qualifies interest against agreed criteria, and schedules the meeting — so your closers only ever talk to real prospects.",
        ["Ideal customer profile and target-account list built to spec",
         "Multi-channel outreach across cold email and LinkedIn",
         "Human reply handling — objections, questions, and scheduling",
         "Meetings booked straight to your calendar with full context notes",
         "No-show handling and automatic reschedules",
         "CRM sync and weekly reporting on meetings booked"],
        [("Qualified meetings / mo", "<em>20–30</em>"),
         ("Show-up rate", "82%"),
         ("Cost per meeting", "↓ 51%"),
         ("Time to first meeting", "2–4 wks")],
        ["You have a proven offer and a sales team that can close but no time to prospect.",
         "Your average deal size justifies a per-meeting or retainer investment.",
         "You sell to a definable B2B buyer with real budget authority.",
         "You want to grow pipeline without the cost and ramp of hiring SDRs."],
        [("How much does appointment setting cost?",
          "<p>Most B2B appointment-setting engagements run on a monthly retainer between roughly $2,000 and $6,000, sometimes with a per-meeting or performance component. Pricing depends on target volume, market complexity, and how many channels you run. We give you a fixed quote and a realistic meeting forecast on your strategy call. See our full breakdown in <a href='blog/how-much-does-appointment-setting-cost.html'>How much does appointment setting cost?</a></p>"),
         ("What counts as a qualified meeting?",
          "<p>A meeting with a decision-maker who matches your agreed ICP and has expressed genuine interest in your offer. We set the criteria — title, company size, budget, timeline — with you before launch, so every booked meeting is one worth taking.</p>"),
         ("What happens if a prospect no-shows?",
          "<p>We track show-ups and follow up to reschedule. No-shows caused by factors within our control are replaced at no extra cost, so you only pay for meetings that count.</p>"),
         ("Do the meetings appear on our own calendar?",
          "<p>Yes. We book directly into your calendar (Calendly, Google, or Outlook) with full context notes on the prospect and the conversation, so your rep walks in prepared.</p>"),
         ("Can you integrate with our CRM?",
          "<p>We sync activity and booked meetings to HubSpot, Salesforce, Pipedrive, and most major CRMs so your pipeline stays clean and attributable.</p>")],
        price="a monthly retainer, typically $2k–$6k depending on volume and channels.")

    service_page(
        "cold-email", "Done-For-You Cold Email",
        "Done-for-you cold email agency that lands in the inbox",
        "Cold Email Agency | Done-For-You Cold Email | ClearLeads",
        "Done-for-you cold email agency. We handle inbox setup, deliverability, copywriting, sending, and reply handling to book meetings — cold email for SaaS and B2B startups.",
        "<strong>Done-for-you cold email is a managed service covering everything from infrastructure to booked meetings.</strong> ClearLeads sets up dedicated sending domains and inboxes, warms them, writes and tests the copy, sends at scale, and handles every reply — engineered to land in the primary inbox and turn cold prospects into booked calls.",
        ["Dedicated domains and inboxes, fully warmed for deliverability",
         "SPF, DKIM, and DMARC configured correctly from day one",
         "Verified, ICP-matched prospect lists refreshed continuously",
         "Conversion-focused copy with ongoing A/B testing",
         "Sending, throttling, and inbox rotation managed for you",
         "Human reply handling that books the meeting"],
        [("Deliverability (inbox rate)", "<em>95%+</em>"),
         ("Positive reply rate", "4–8%"),
         ("Emails sent / mo", "3,000+"),
         ("Domains warmed", "included")],
        ["You want a predictable outbound channel without managing tooling.",
         "You've been burned by low deliverability or spam-foldered campaigns.",
         "You're a SaaS or B2B startup that needs pipeline fast.",
         "You have product-market fit and want to scale what's working."],
        [("How do you keep cold email out of spam?",
          "<p>We use dedicated domains separate from your main one, warm every inbox before sending, authenticate with SPF/DKIM/DMARC, keep volume-per-inbox low, and continuously monitor deliverability. Read our full method in <a href='blog/cold-email-deliverability.html'>Cold email deliverability: how we land in the inbox</a>.</p>"),
         ("Is cold email legal?",
          "<p>Yes, when done correctly. B2B cold outreach is permitted under CAN-SPAM (US) and, with a legitimate-interest basis and clear opt-out, under GDPR (EU). We include accurate sender identity and honour unsubscribe requests on every send.</p>"),
         ("Will you use my domain?",
          "<p>No — we register and warm dedicated lookalike domains so your primary domain's reputation is never put at risk. All replies still route to you and appear under your brand.</p>"),
         ("How many meetings can cold email book?",
          "<p>It varies by market and offer, but a well-run campaign sending ~3,000 quality emails a month typically produces 10–25 qualified conversations. We'll forecast realistically for your niche on the call.</p>"),
         ("Cold email or LinkedIn — which is better?",
          "<p>They work best together. Email gives reach and volume; LinkedIn adds trust and a second touch. See <a href='blog/cold-email-vs-linkedin-outreach.html'>Cold email vs LinkedIn outreach</a> for a full comparison.</p>")],
        price="a monthly retainer that includes all sending infrastructure and inbox warm-up.")

    service_page(
        "linkedin-outreach", "LinkedIn Outreach",
        "LinkedIn outreach that turns connections into sales meetings",
        "LinkedIn Outreach & Social Selling Services | ClearLeads",
        "Managed LinkedIn outreach and social selling for B2B. Targeted connection and messaging campaigns from your profile that book qualified meetings — a strong complement to cold email.",
        "<strong>LinkedIn outreach is a managed social-selling service that books meetings from your LinkedIn profile.</strong> ClearLeads targets the right decision-makers, sends personalised connection requests and message sequences from your account, and handles the conversation through to a booked meeting — adding a trusted, face-to-name channel alongside your cold email.",
        ["ICP-based targeting using LinkedIn Sales Navigator",
         "Optimisation of your profile to convert visitors",
         "Personalised connection requests and multi-step message sequences",
         "Safe daily sending limits that protect your account",
         "Reply handling and qualification by real people",
         "Meetings booked to your calendar with conversation context"],
        [("Connection accept rate", "<em>30–45%</em>"),
         ("Reply rate", "15–25%"),
         ("Meetings / mo", "8–15"),
         ("Account safety", "protected")],
        ["Your buyers are active and reachable on LinkedIn.",
         "You want a warmer, relationship-led channel to complement email.",
         "Your founders or reps want to build authority while booking meetings.",
         "You sell considered B2B products where trust shortens the cycle."],
        [("Is LinkedIn outreach safe for my account?",
          "<p>Yes. We stay well within LinkedIn's activity limits, use gradual ramp-up, and mimic natural human behaviour. Your account safety is never traded for volume.</p>"),
         ("Do you post content or just send messages?",
          "<p>Our core service is direct outreach and booking meetings. We can also advise on profile optimisation and light thought-leadership content to lift response rates, but messaging is where the meetings come from.</p>"),
         ("Do I need Sales Navigator?",
          "<p>It's strongly recommended for precise targeting and higher-quality lists. We'll help you set it up if you don't have it.</p>"),
         ("Can you run LinkedIn and cold email together?",
          "<p>Absolutely — multi-channel sequences that touch a prospect on both email and LinkedIn consistently book more meetings than either alone.</p>")],
        price="a monthly retainer per active sending profile.")

    service_page(
        "lead-lists", "Lead List Building & Data",
        "Verified lead lists and B2B data built to your ICP",
        "B2B Lead List Building & Data Services | ClearLeads",
        "Verified, targeted B2B lead lists built to your ideal customer profile. Accurate contact data with valid emails and direct info — a low-risk entry point to outbound.",
        "<strong>Lead list building is a service that delivers verified, ICP-matched prospect data ready for outreach.</strong> ClearLeads researches and compiles targeted lists of decision-makers — job title, company, verified business email, and LinkedIn — then triple-verifies every record so you launch campaigns on clean data instead of bounces.",
        ["Ideal customer profile defined with you",
         "Sourcing across premium B2B databases and manual research",
         "Verified business emails with low bounce guarantee",
         "Firmographic and role filters (industry, size, seniority, geo)",
         "Enrichment with LinkedIn URLs and key context fields",
         "Delivered as a clean CSV or synced to your CRM"],
        [("Email deliverability", "<em>&lt;3% bounce</em>"),
         ("Data accuracy", "97%+"),
         ("Turnaround", "3–5 days"),
         ("Fields per record", "10+")],
        ["You want to test outbound before committing to a full program.",
         "Your team can run outreach but needs reliable data to run it on.",
         "You're entering a new segment and need a targeted list fast.",
         "You're tired of bounce rates wrecking your sender reputation."],
        [("How accurate is the data?",
          "<p>We triple-verify every email and target 97%+ accuracy with under 3% bounce. Any records that slip through verification are replaced.</p>"),
         ("What fields do I get?",
          "<p>Typically full name, job title, company, company size, industry, verified business email, LinkedIn URL, and location — plus any custom fields your campaigns need.</p>"),
         ("Is the data GDPR-compliant?",
          "<p>We source business contact data on a legitimate-interest basis and provide only professional, role-based information. You remain the controller for how it's used in outreach.</p>"),
         ("Can this lead into a full campaign?",
          "<p>Yes — many clients start with a list, then have us run the outreach on it. It's the lowest-risk way to see how our data and process perform.</p>")],
        price="a per-list or per-verified-record fee, quoted to your criteria.")

    service_page(
        "database-reactivation", "Database Reactivation",
        "Database reactivation that revives cold and dormant leads",
        "Database Reactivation Services | ClearLeads",
        "Database reactivation services that revive old, cold, and dormant leads with fresh sequences — turning a list you already own into new booked meetings and pipeline.",
        "<strong>Database reactivation is a service that turns your dormant leads into new sales meetings.</strong> ClearLeads takes the old, cold, and unconverted contacts already in your CRM, cleans and re-verifies them, and runs fresh, relevant multi-channel sequences to re-engage buyers whose timing may finally be right — pipeline from a list you've already paid for.",
        ["Audit and cleansing of your existing database",
         "Re-verification of stale email and contact data",
         "Segmentation by past intent, source, and recency",
         "New messaging angles that give a reason to re-engage",
         "Multi-channel re-engagement across email and LinkedIn",
         "Booked meetings and a re-scored, usable list"],
        [("Dormant leads re-engaged", "<em>6–12%</em>"),
         ("Cost vs new leads", "↓ 60%"),
         ("Meetings from 'dead' list", "10–20"),
         ("List re-verified", "included")],
        ["You have thousands of old leads or trial users gathering dust.",
         "You've changed your offer, pricing, or ICP since you captured them.",
         "You want quick pipeline without paying for brand-new data.",
         "Your CRM is full of contacts nobody has touched in 6+ months."],
        [("Why reactivate instead of buying new leads?",
          "<p>Contacts already in your database know your brand and once showed interest, so they convert cheaper and faster than cold-sourced leads. Reactivation typically costs around 60% less per meeting.</p>"),
         ("Won't these leads be annoyed to hear from us?",
          "<p>Not when the message is relevant. We lead with a genuine reason to reconnect — a new capability, a changed price, a relevant result — and always honour opt-outs.</p>"),
         ("What if the data is really old?",
          "<p>We re-verify and cleanse first, dropping dead records and updating what we can, so you're only messaging reachable, valid contacts.</p>"),
         ("How fast does reactivation work?",
          "<p>Because there's no list-building lag, campaigns can launch within days and produce meetings in the first two to three weeks.</p>")],
        price="a fixed project fee based on database size, or a monthly retainer.")

    service_page(
        "outbound-system-setup", "Outbound System Setup",
        "Outbound system setup — your outreach machine, built once",
        "Outbound System Setup & Build | ClearLeads",
        "A one-time outbound system build: sending infrastructure, tooling, ICP, sequences, and playbooks. We set up your outreach machine so your team can run it in-house.",
        "<strong>Outbound system setup is a one-time build of the complete infrastructure your team needs to run outreach in-house.</strong> ClearLeads configures your domains, inboxes, tools, CRM, ICP, sequences, and reporting, then hands you a documented, ready-to-run outbound engine — ideal if you want to own the channel rather than outsource it.",
        ["Sending infrastructure: domains, inboxes, warm-up, authentication",
         "Tool stack selection and configuration",
         "ICP definition and target-account framework",
         "Battle-tested email and LinkedIn sequence templates",
         "CRM setup, pipeline stages, and reporting dashboards",
         "Playbooks and a training session for your team"],
        [("Setup time", "<em>2–3 wks</em>"),
         ("Handover", "docs + training"),
         ("Ready to send", "day one"),
         ("Ongoing fees", "none")],
        ["You want to build outbound in-house but skip the trial-and-error.",
         "You have (or are hiring) SDRs who need a system to run.",
         "You'd rather own the channel long-term than outsource it.",
         "You need it set up correctly once, without deliverability landmines."],
        [("What's the difference from your managed service?",
          "<p>Managed service means we run outbound for you every month. System setup is a one-time build: we construct and document everything, then hand it to your team to operate. No ongoing retainer.</p>"),
         ("Can you train our SDRs?",
          "<p>Yes. Handover includes written playbooks plus a live training session so your reps can run and optimise the system confidently.</p>"),
         ("What if we want help later?",
          "<p>Many setup clients bring us back for a managed program or a periodic optimisation review. There's no obligation either way.</p>"),
         ("How long until we're sending?",
          "<p>The full build takes about two to three weeks, mostly driven by inbox warm-up. After handover your team can send from day one.</p>")],
        price="a one-time project fee, scoped on the call.")

# ------------------------------------------------------------------
# HOW IT WORKS
# ------------------------------------------------------------------
def build_how():
    faqs = [
        ("How long until the system is live?",
         "<p>About 14 days. The main dependency is inbox warm-up, which can't be rushed without hurting deliverability. Strategy, lists, and copy are built in parallel during that window.</p>"),
        ("What do you need from us to start?",
         "<p>An intro call to define your ICP and offer, access or details for calendar and CRM, and a quick approval of the messaging. From there we run the machine.</p>"),
        ("How involved do we need to be?",
         "<p>Lightly. You approve strategy and messaging up front and take the meetings we book. We handle prospecting, sending, and reply management day to day, and report weekly.</p>"),
        ("How do you report progress?",
         "<p>You get a live dashboard plus a weekly numbers call covering sends, reply rates, and meetings booked — with next-step optimisations.</p>"),
    ]
    steps_full = [
        ("Discovery & ICP", "We run a kickoff to define your ideal customer profile, sharpen your positioning, and agree exactly what a 'qualified meeting' means for you. This is where good outbound is won or lost.",
         ["Ideal customer profile & target accounts", "Offer and messaging positioning", "Qualification criteria agreed", "Meeting forecast set"]),
        ("Build & infrastructure", "We stand up dedicated sending infrastructure, warm the inboxes, build your verified prospect list, and write channel-specific copy. Everything is engineered for the primary inbox.",
         ["Dedicated domains & inboxes warmed", "SPF/DKIM/DMARC authenticated", "Verified ICP prospect list", "Email & LinkedIn copy written and tested"]),
        ("Launch & book", "Sequences go live across email and LinkedIn. Our team handles every reply — questions, objections, scheduling — and books qualified meetings straight to your calendar with full context.",
         ["Multi-channel sequences live", "Human reply handling & qualification", "Meetings booked to your calendar", "Context notes for every meeting"]),
        ("Optimise & scale", "We report weekly on real numbers, A/B test copy and lists, retire what underperforms, and scale what converts — so cost per meeting drops and pipeline compounds month over month.",
         ["Weekly reporting & numbers call", "A/B testing of copy and lists", "Continuous deliverability monitoring", "Scale winning segments"]),
    ]
    blocks = ""
    for i, (t, d, pts) in enumerate(steps_full, 1):
        rev = " rev" if i % 2 == 0 else ""
        checks = "".join(f'<li>{p}</li>' for p in pts)
        blocks += f'''<section class="{'bg-soft' if i%2 else ''}">
  <div class="container">
    <div class="split{rev}">
      <div class="txt">
        <div class="step" style="display:inline-block"><div class="n">{i}</div></div>
        <h2>{t}</h2><p class="lede" style="font-size:1.08rem">{d}</p>
      </div>
      <div class="panel"><ul class="checks">{checks}</ul></div>
    </div>
  </div>
</section>'''
    body = f'''
<div class="container crumb"><a href="index.html">Home</a> / How It Works</div>
<section class="hero">
  <div class="container hero-inner" style="padding-top:48px">
    <div class="narrow">
      <span class="eyebrow">How it works</span>
      <h1>How ClearLeads books qualified meetings for you</h1>
      <p class="lede mt-1">A transparent, four-stage system. You approve the strategy and take the meetings — we build the engine, run the outreach, and prove it with weekly numbers.</p>
      <div class="hero-cta mt-2"><a href="{BOOK}" class="btn btn-primary btn-lg">Book a call {A}</a></div>
    </div>
  </div>
</section>
<section class="section-tight">
  <div class="container narrow">
    <p class="answer"><strong>ClearLeads books meetings in four stages: discovery, build, launch, and optimise.</strong> We define your ICP and offer, stand up warmed sending infrastructure with verified lists and copy, launch multi-channel outreach with human reply handling, and then report and optimise weekly — typically going live within 14 days.</p>
  </div>
</section>
{blocks}
{stat_band()}
{faq_block(faqs)}
{cta_band()}
'''
    page("how-it-works.html",
         "How It Works | ClearLeads Appointment Setting Process",
         "See how ClearLeads books qualified B2B meetings: discovery and ICP, infrastructure build, multi-channel launch, and weekly optimisation. Live in about 14 days.",
         body, schemas=[faq_schema(faqs)])

# ------------------------------------------------------------------
# RESULTS
# ------------------------------------------------------------------
def build_results():
    cases = [
        ("Vertex SaaS", "Series A · Sales SaaS",
         "Stalled at flat pipeline with two reps spending half their week prospecting.",
         "Full appointment-setting program across email + LinkedIn, targeting RevOps leaders.",
         [("Qualified meetings in 90 days", "68"), ("Positive reply rate", "7.4%"), ("Pipeline influenced", "$740k")]),
        ("BluePeak", "Boutique consultancy",
         "A year of failed in-house outbound; deliverability in the gutter.",
         "New sending infrastructure, re-warmed domains, and done-for-you cold email.",
         [("Time to live", "12 days"), ("Reply rate vs before", "3×"), ("Meetings / month", "19")]),
        ("Ledgerly", "Fintech · SMB",
         "High SDR cost per meeting and no clear reporting on what worked.",
         "Outsourced SDR service with weekly numbers calls and continuous testing.",
         [("Cost per meeting", "↓ 51%"), ("Show-up rate", "84%"), ("Meetings / quarter", "57")]),
    ]
    cards = ""
    for name, tag, prob, sol, mets in cases:
        m = "".join(f'<div class="metric-row"><span class="k">{k}</span><span class="v"><em>{v}</em></span></div>' for k, v in mets)
        cards += f'''<div class="card">
          <div class="tag-row"><span class="tag">{tag}</span></div>
          <h3>{name}</h3>
          <p><strong style="color:var(--ink)">Challenge:</strong> {prob}</p>
          <p><strong style="color:var(--ink)">What we did:</strong> {sol}</p>
          <div style="margin-top:auto">{m}</div>
        </div>'''
    body = f'''
<div class="container crumb"><a href="index.html">Home</a> / Results</div>
<section class="hero">
  <div class="container hero-inner" style="padding-top:48px">
    <div class="narrow">
      <span class="eyebrow">Results & case studies</span>
      <h1>Real pipeline, real numbers</h1>
      <p class="lede mt-1">We're measured on one thing: qualified meetings booked. Here's what that has looked like for B2B teams that stopped prospecting and started closing.</p>
      <div class="hero-cta mt-2"><a href="{BOOK}" class="btn btn-primary btn-lg">Book a call {A}</a></div>
    </div>
  </div>
</section>
{stat_band()}
<section>
  <div class="container">
    <div class="section-head"><span class="eyebrow">Case studies</span><h2>Selected client outcomes</h2>
      <p>Representative results from B2B appointment-setting and cold email programs. Your forecast is set on the strategy call.</p></div>
    <div class="grid grid-3">{cards}</div>
  </div>
</section>
{testimonial_row()}
<section class="bg-navy">
  <div class="container narrow center">
    <span class="eyebrow on-dark">A note on numbers</span>
    <h2>We forecast honestly and report weekly</h2>
    <p>Outbound results vary by market, offer, and deal size. We won't promise a number we can't defend — instead we give you a realistic forecast up front and show the actual sends, replies, and meetings every single week.</p>
    <a href="{BOOK}" class="btn btn-primary btn-lg mt-1">Get your forecast {A}</a>
  </div>
</section>
{cta_band()}
'''
    page("results.html",
         "Results & Case Studies | ClearLeads B2B Lead Generation",
         "ClearLeads case studies: qualified meetings booked, reply-rate lifts, and lower cost per meeting for B2B SaaS, consulting, and fintech teams. See the numbers.",
         body)

# ------------------------------------------------------------------
# ABOUT
# ------------------------------------------------------------------
def build_about():
    values = [
        ("target", "Meetings over metrics", "We're paid to book qualified meetings, not to inflate open rates. Every decision ladders up to pipeline."),
        ("shield", "Radical transparency", "Real numbers, every week. If something isn't working we tell you — then we fix it."),
        ("bolt", "Speed with craft", "Live in about 14 days, but never at the expense of deliverability or message quality."),
    ]
    vcells = "".join(f'<div class="card"><div class="ico">{ICONS[i]}</div><h3>{t}</h3><p>{d}</p></div>' for i, t, d in values)
    faqs = [
        ("Where is ClearLeads based?",
         "<p>We're a distributed B2B lead generation team serving clients across North America, Europe, and Asia, with operational roots in India. Outbound is run in your prospects' time zones.</p>"),
        ("Who will run my campaigns?",
         "<p>A dedicated strategist plus reply-handling specialists — not an anonymous queue. You'll know your team and speak with them on the weekly call.</p>"),
        ("Why the name ClearLeads?",
         "<p>Because outbound is usually a black box. We built the opposite: clear targeting, clear messaging, and clear reporting on the only metric that matters — booked meetings.</p>"),
    ]
    body = f'''
<div class="container crumb"><a href="index.html">Home</a> / About</div>
<section class="hero">
  <div class="container hero-inner" style="padding-top:48px">
    <div class="narrow">
      <span class="eyebrow">About ClearLeads</span>
      <h1>We build pipeline for B2B teams that would rather be closing</h1>
      <p class="lede mt-1">ClearLeads exists because most companies know outbound works but don't have the time, tooling, or patience to run it well. So we run it for them — and we report every number along the way.</p>
      <div class="hero-cta mt-2"><a href="{BOOK}" class="btn btn-primary btn-lg">Book a call {A}</a></div>
    </div>
  </div>
</section>
<section>
  <div class="container narrow">
    <p class="answer"><strong>ClearLeads is a B2B lead generation agency specialising in appointment setting and outbound outreach.</strong> We help B2B companies book qualified sales meetings through done-for-you cold email and LinkedIn campaigns, combining verified data, strong messaging, and honest weekly reporting so clients get pipeline they can trust.</p>
    <h2 class="mt-3">Our story</h2>
    <p>ClearLeads started with a simple frustration: talented sales teams stuck doing their own prospecting, and outbound "experts" hiding behind vanity metrics. We'd seen how much pipeline a well-built outbound system could produce — and how rarely it was actually built well.</p>
    <p>So we assembled a team obsessed with two things: landing in the primary inbox, and booking meetings worth taking. No black boxes, no meaningless dashboards. Just clear targeting, clear messaging, and a weekly call where we show you exactly what happened and what's next.</p>
    <p>Today we run outbound for B2B SaaS, consultancies, agencies, and service businesses across the globe — and we're still measured on the same single number: qualified meetings booked.</p>
  </div>
</section>
<section class="bg-soft">
  <div class="container">
    <div class="section-head"><span class="eyebrow">What we believe</span><h2>Three principles behind every campaign</h2></div>
    <div class="grid grid-3">{vcells}</div>
  </div>
</section>
{stat_band()}
{faq_block(faqs)}
{cta_band()}
'''
    page("about.html",
         "About ClearLeads | B2B Lead Generation Agency",
         "ClearLeads is a B2B lead generation and appointment-setting agency built on verified data, strong messaging, and honest weekly reporting. Meet the team behind your pipeline.",
         body, schemas=[faq_schema(faqs)])

# ------------------------------------------------------------------
# CONTACT / BOOK
# ------------------------------------------------------------------
def build_contact():
    faqs = [
        ("What happens on the call?",
         "<p>A focused 30 minutes: we learn your offer and ICP, tell you honestly whether outbound is a fit, outline the plan, and give you a realistic meeting forecast and quote. No pressure and no obligation.</p>"),
        ("How much does it cost to work with ClearLeads?",
         "<p>Most managed programs run on a monthly retainer between roughly $2,000 and $6,000 depending on volume and channels; lead lists and one-time builds are quoted separately. You'll get a fixed quote on the call.</p>"),
        ("How soon can we start?",
         "<p>Onboarding usually begins within a few days of the call, and campaigns go live in about 14 days once inboxes are warmed.</p>"),
    ]
    body = f'''
<div class="container crumb"><a href="index.html">Home</a> / Book a call</div>
<section class="hero hero-dark">
  <div class="container hero-inner" style="padding-top:56px;padding-bottom:56px">
    <div class="narrow">
      <span class="eyebrow on-dark">Book a call</span>
      <h1>Let's fill your calendar with qualified meetings</h1>
      <p class="hero-sub">Grab a 30-minute strategy call. We'll map your ICP, tell you honestly whether outbound fits, and give you a realistic forecast and quote — no pressure, no long contracts.</p>
    </div>
  </div>
</section>
<section>
  <div class="container">
    <p class="answer" style="max-width:760px;margin:0 auto 40px"><strong>Booking a call with ClearLeads takes about 30 minutes.</strong> We'll discuss your ideal customer, your offer, and your goals, then show you the plan and a realistic meeting forecast. You'll leave the call knowing exactly what outbound could produce for you and what it would cost — whether or not you work with us.</p>
    <div class="book-grid">
      <div>
        <h2>Pick a time</h2>
        <p class="lede" style="font-size:1.05rem">Choose a slot that suits you and we'll send a calendar invite with a short intake form.</p>
        <div class="calendly-holder" id="book">
          <div class="inner">
            <div class="cal-ico">{ICONS['calendar']}</div>
            <h3>Calendly booking widget</h3>
            <p style="color:var(--muted)">Embed your Calendly link here to make this the primary conversion point. Replace the placeholder with your scheduling embed.</p>
            <a href="https://calendly.com/clearleads/strategy-call" class="btn btn-primary mt-1">Open scheduler {A}</a>
          </div>
        </div>
      </div>
      <div>
        <h2>Prefer to send a note?</h2>
        <p class="lede" style="font-size:1.05rem">Tell us a little about your goals and we'll reply within one business day.</p>
        <form class="lead mt-2" onsubmit="event.preventDefault();this.innerHTML='<div class=&quot;callout&quot;><strong>Thanks — we\\'ll be in touch within one business day.</strong></div>';">
          <div><label for="name">Name</label><input id="name" name="name" required placeholder="Jane Doe"></div>
          <div><label for="email">Work email</label><input id="email" type="email" name="email" required placeholder="jane@company.com"></div>
          <div><label for="company">Company</label><input id="company" name="company" placeholder="Company Inc."></div>
          <div><label for="service">What are you interested in?</label>
            <select id="service" name="service">
              <option>Appointment Setting</option>
              <option>Done-For-You Cold Email</option>
              <option>LinkedIn Outreach</option>
              <option>Lead List Building &amp; Data</option>
              <option>Database Reactivation</option>
              <option>Outbound System Setup</option>
              <option>Not sure yet</option>
            </select></div>
          <div><label for="msg">Anything we should know?</label><textarea id="msg" name="msg" rows="4" placeholder="Our ICP is… our goal is…"></textarea></div>
          <button class="btn btn-primary btn-lg" type="submit">Request a call {A}</button>
        </form>
      </div>
    </div>
  </div>
</section>
<section class="bg-soft">
  <div class="container center">
    <div class="grid grid-3" style="max-width:820px;margin:0 auto">
      <div><div class="stat"><div class="num" style="font-size:1.4rem">hello@clearleads.co</div><div class="lbl">Email us</div></div></div>
      <div><div class="stat"><div class="num" style="font-size:1.4rem">Mon–Fri</div><div class="lbl">We reply within 1 business day</div></div></div>
      <div><div class="stat"><div class="num" style="font-size:1.4rem">clearleads.co</div><div class="lbl">B2B Lead Generation</div></div></div>
    </div>
  </div>
</section>
{faq_block(faqs)}
'''
    page("contact.html",
         "Book a Call | ClearLeads B2B Lead Generation",
         "Book a free 30-minute strategy call with ClearLeads. We'll map your ICP, forecast qualified meetings, and give you a fixed quote — no pressure, no long contracts.",
         body, schemas=[faq_schema(faqs)])

# ------------------------------------------------------------------
# BLOG INDEX + ARTICLES
# ------------------------------------------------------------------
ARTICLES = [
    ("how-much-does-appointment-setting-cost", "How much does appointment setting cost in 2026?",
     "A clear breakdown of appointment-setting pricing models, real price ranges, and how to work out your cost per meeting.", "Pricing"),
    ("cold-email-vs-linkedin-outreach", "Cold email vs LinkedIn outreach: which books more meetings?",
     "How the two biggest outbound channels compare on reach, reply rates, cost, and when to use each — or both.", "Strategy"),
    ("cold-email-deliverability", "Cold email deliverability: how we land in the inbox",
     "The exact setup — domains, warm-up, authentication, and sending discipline — that keeps cold email out of spam.", "Deliverability"),
]

def build_blog_index():
    cards = ""
    for slug, title, excerpt, tag in ARTICLES:
        cards += f'''<a class="card" href="{slug}.html" style="text-decoration:none">
          <div class="tag-row"><span class="tag">{tag}</span></div>
          <h3>{title}</h3><p>{excerpt}</p><span class="learn">Read article {A}</span></a>'''
    body = f'''
<div class="container crumb"><a href="../index.html">Home</a> / Blog</div>
<section class="hero">
  <div class="container hero-inner" style="padding-top:48px">
    <div class="narrow">
      <span class="eyebrow">Resources</span>
      <h1>Outbound & lead generation, explained</h1>
      <p class="lede mt-1">Practical guides on appointment setting, cold email, LinkedIn outreach, and building B2B pipeline — written to actually answer the question, not pad it out.</p>
    </div>
  </div>
</section>
<section class="section-tight">
  <div class="container"><div class="grid grid-3">{cards}</div></div>
</section>
{cta_band(prefix="../")}
'''
    page("blog/index.html",
         "Blog | B2B Lead Generation & Outbound Guides | ClearLeads",
         "Practical guides on appointment setting, cold email, LinkedIn outreach, and B2B pipeline. Learn how outbound really works from the ClearLeads team.",
         body, prefix="../", canonical=f"{SITE}/blog/")

def article(slug, seo_title, meta, h1, tag, read, dek, answer, sections_html, faqs, related=None):
    art_schema = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": h1, "description": meta,
        "author": {"@type": "Organization", "name": NAME},
        "publisher": {"@type": "Organization", "name": NAME, "url": SITE},
        "mainEntityOfPage": f"{SITE}/blog/{slug}", "datePublished": "2026-01-15",
        "dateModified": "2026-06-01",
    }
    rel = related or []
    rel_cards = ""
    for rslug, rtitle in rel:
        rel_cards += f'<a class="card" href="{rslug}.html" style="text-decoration:none"><h3>{rtitle}</h3><span class="learn">Read {A}</span></a>'
    rel_html = f'''<section class="bg-soft"><div class="container">
      <div class="section-head"><span class="eyebrow">Keep reading</span><h2>Related guides</h2></div>
      <div class="grid grid-2" style="max-width:820px;margin:0 auto">{rel_cards}</div></div></section>''' if rel else ""
    faq_html = faq_block(faqs) if faqs else ""
    body = f'''
<div class="container crumb"><a href="../index.html">Home</a> / <a href="index.html">Blog</a> / {tag}</div>
<article>
<section style="padding-bottom:24px">
  <div class="container article">
    <div class="tag-row"><span class="tag">{tag}</span></div>
    <h1>{h1}</h1>
    <p class="meta">By the ClearLeads team · Updated June 2026 · {read} min read</p>
    <p class="lede">{dek}</p>
  </div>
</section>
<section style="padding-top:0">
  <div class="container article">
    <p class="answer">{answer}</p>
    {sections_html}
    <div class="callout mt-3">
      <strong style="color:var(--ink)">Want the short version for your business?</strong>
      <p class="mb-0 mt-1">Book a 30-minute call and we'll give you a realistic forecast and a fixed quote. <a href="../{BOOK}">Book a call →</a></p>
    </div>
  </div>
</section>
</article>
{faq_html}
{rel_html}
{cta_band(prefix="../")}
'''
    page(f"blog/{slug}.html", seo_title, meta, body,
         schemas=[art_schema] + ([faq_schema(faqs)] if faqs else []),
         prefix="../")

def build_articles():
    # 1) Appointment setting cost
    sections = '''
<h2>The three ways appointment setting is priced</h2>
<p>Almost every agency uses one of three pricing models. Knowing which you're being quoted matters more than the headline number.</p>
<table>
<tr><th>Model</th><th>Typical range</th><th>Best when</th></tr>
<tr><td>Monthly retainer</td><td>$2,000–$6,000 / mo</td><td>You want predictable volume and full-funnel ownership</td></tr>
<tr><td>Pay-per-meeting</td><td>$100–$400 / meeting</td><td>You want to pay purely for output (watch qualification rules)</td></tr>
<tr><td>Hybrid (base + per-meeting)</td><td>$1,500 base + $75–$150 / meeting</td><td>You want aligned incentives and some cost predictability</td></tr>
</table>
<p>A pure retainer aligns the agency with building a durable system; pay-per-meeting shifts risk to the agency but can incentivise loosely-qualified bookings unless the criteria are airtight. Hybrids try to get the best of both.</p>
<h2>What actually drives the price</h2>
<ul>
<li><strong>Target volume.</strong> More meetings means more sending infrastructure, data, and reply handling.</li>
<li><strong>Market difficulty.</strong> Reaching CFOs at enterprises costs more per meeting than reaching founders at startups.</li>
<li><strong>Channels.</strong> Email-only is cheaper than a multi-channel email + LinkedIn program.</li>
<li><strong>Data.</strong> Niche or hard-to-source ICPs raise list-building cost.</li>
</ul>
<h2>How to calculate your real cost per meeting</h2>
<p>Divide the total monthly cost by qualified meetings booked. A $4,000 retainer that produces 20 qualified meetings is $200 per meeting. Then compare that to what a meeting is worth: if your average deal is $15,000 and you close 1 in 5 meetings, each meeting is worth $3,000 in expected revenue — making $200 an easy trade.</p>
<div class="callout"><strong style="color:var(--ink)">Rule of thumb:</strong> if your cost per qualified meeting is under 10% of your average deal value, outbound is almost always worth scaling.</div>
<h2>Watch-outs when comparing quotes</h2>
<ul>
<li>Is inbox infrastructure and warm-up <em>included</em>, or billed separately?</li>
<li>How is a "qualified meeting" defined, and who replaces no-shows?</li>
<li>Is there a long lock-in, or month-to-month after ramp?</li>
<li>Are you paying for leads, or for booked meetings? They're not the same.</li>
</ul>
'''
    faqs = [
        ("How much does appointment setting cost per month?",
         "<p>Most B2B appointment-setting retainers run between $2,000 and $6,000 per month, depending on meeting volume, market difficulty, and how many channels you use. Pay-per-meeting deals typically range from $100 to $400 per qualified meeting.</p>"),
        ("Is pay-per-meeting cheaper than a retainer?",
         "<p>Not necessarily. Pay-per-meeting shifts risk to the agency but can cost more per booking and can incentivise loose qualification. A retainer usually produces a lower cost per meeting once the system matures — provided volume is there.</p>"),
        ("What's a good cost per qualified meeting?",
         "<p>If your cost per qualified meeting is under about 10% of your average deal value, the economics work well. For a $15,000 average deal, anything under roughly $1,500 per meeting is healthy, and most programs come in far below that.</p>"),
    ]
    article("how-much-does-appointment-setting-cost",
            "How Much Does Appointment Setting Cost in 2026? | ClearLeads",
            "Appointment setting costs $2,000–$6,000/mo on retainer or $100–$400 per meeting. See pricing models, what drives cost, and how to calculate your cost per meeting.",
            "How much does appointment setting cost in 2026?",
            "Pricing", 6,
            "Pricing models, real ranges, and how to work out whether the numbers make sense for your business.",
            "<strong>Appointment setting typically costs $2,000–$6,000 per month on a retainer, or $100–$400 per qualified meeting on a pay-per-meeting model.</strong> The right number depends on your target volume, how hard your market is to reach, and how many channels you run. The metric that matters most is cost per qualified meeting measured against your average deal value.",
            sections, faqs,
            related=[("cold-email-vs-linkedin-outreach", "Cold email vs LinkedIn outreach: which books more meetings?"),
                     ("cold-email-deliverability", "Cold email deliverability: how we land in the inbox")])

    # 2) Cold email vs LinkedIn
    sections2 = '''
<h2>Reach and volume</h2>
<p>Cold email wins on raw scale. A well-run program can contact thousands of prospects a month across multiple inboxes. LinkedIn is capped by platform limits — realistically 20–30 new connections a day per profile — so its ceiling is lower but its touches are warmer.</p>
<h2>Reply rates and trust</h2>
<p>LinkedIn messages usually see higher reply rates (15–25%) because there's a face, a profile, and social proof attached. Cold email reply rates are lower per message (4–8% positive) but the far larger volume often produces more total conversations.</p>
<table>
<tr><th>Factor</th><th>Cold email</th><th>LinkedIn outreach</th></tr>
<tr><td>Monthly reach</td><td>Very high (1,000s)</td><td>Limited (100s)</td></tr>
<tr><td>Reply rate</td><td>4–8% positive</td><td>15–25%</td></tr>
<tr><td>Trust / warmth</td><td>Lower</td><td>Higher</td></tr>
<tr><td>Cost to scale</td><td>Low per contact</td><td>Higher per contact</td></tr>
<tr><td>Setup complexity</td><td>Higher (deliverability)</td><td>Lower</td></tr>
</table>
<h2>Cost per meeting</h2>
<p>Because email scales cheaply, its cost per meeting is usually lower at volume. LinkedIn costs more per touch but can convert considered, high-value buyers who would ignore a cold email — so on big deals its cost per meeting can be very competitive.</p>
<h2>The real answer: use both</h2>
<p>The framing "email vs LinkedIn" is a trap. The best-performing outbound sequences touch a prospect on both channels: an email lands, a LinkedIn connection reinforces it, a follow-up references the earlier touch. Multi-channel sequences consistently book more meetings than either channel run alone, because different buyers respond to different first touches.</p>
<div class="callout"><strong style="color:var(--ink)">Bottom line:</strong> lead with email for reach, layer LinkedIn for trust, and sequence them together. That combination beats any single channel.</div>
'''
    faqs2 = [
        ("Which books more meetings, cold email or LinkedIn?",
         "<p>At volume, cold email usually books more total meetings because it reaches far more prospects. LinkedIn books fewer but often higher-trust meetings. Running both in a coordinated sequence beats either channel alone.</p>"),
        ("Is LinkedIn outreach better for high-value deals?",
         "<p>Often yes. For considered, high-ticket B2B purchases, the trust and personalisation of LinkedIn can convert buyers who would ignore a cold email — making its cost per meeting competitive despite lower volume.</p>"),
        ("Can you run cold email and LinkedIn at the same time?",
         "<p>Yes, and you should. Coordinated multi-channel sequences — an email plus a LinkedIn touch that reference each other — reliably outperform single-channel outreach.</p>"),
    ]
    article("cold-email-vs-linkedin-outreach",
            "Cold Email vs LinkedIn Outreach: Which Books More Meetings? | ClearLeads",
            "Cold email offers scale and lower cost per meeting; LinkedIn offers higher reply rates and trust. Compare both channels and learn why a combined sequence wins.",
            "Cold email vs LinkedIn outreach: which books more meetings?",
            "Strategy", 5,
            "How the two biggest outbound channels compare — and why the smartest teams stop choosing between them.",
            "<strong>Cold email books more meetings at scale thanks to far greater reach, while LinkedIn outreach earns higher reply rates and trust per message.</strong> Email offers the lowest cost per meeting at volume; LinkedIn converts considered, high-value buyers. The highest-performing programs run both channels together in a coordinated sequence rather than picking one.",
            sections2, faqs2,
            related=[("how-much-does-appointment-setting-cost", "How much does appointment setting cost in 2026?"),
                     ("cold-email-deliverability", "Cold email deliverability: how we land in the inbox")])

    # 3) Deliverability
    sections3 = '''
<h2>Why cold email lands in spam</h2>
<p>Spam placement is rarely about the words in one email. It's about sender reputation: sending from an unwarmed domain, missing authentication, blasting too much volume from one inbox, or triggering spam complaints. Fix the reputation and placement follows.</p>
<h2>The setup that keeps you in the inbox</h2>
<ol>
<li><strong>Use dedicated domains.</strong> Never send cold email from your primary domain. Register separate lookalike domains so your main reputation is never at risk.</li>
<li><strong>Warm every inbox.</strong> Ramp sending gradually over 2–3 weeks so mailbox providers learn the inbox is a real human, not a blaster.</li>
<li><strong>Authenticate properly.</strong> Configure SPF, DKIM, and DMARC on every sending domain. Missing records are an instant credibility hit.</li>
<li><strong>Keep volume-per-inbox low.</strong> Spread sending across multiple inboxes rather than pushing high volume through one. Low and steady beats high and spiky.</li>
<li><strong>Send to verified lists.</strong> Bounces destroy reputation. Triple-verify data and keep bounce rates under 3%.</li>
<li><strong>Write like a human.</strong> Short, specific, low-link messages that earn replies. Engagement is itself a positive deliverability signal.</li>
</ol>
<h2>Monitor, don't set-and-forget</h2>
<p>Deliverability drifts. We monitor inbox placement, reply rates, and spam signals continuously, rotate inboxes, and pull back volume the moment metrics dip — before it becomes a problem you can see in booked meetings.</p>
<div class="callout"><strong style="color:var(--ink)">The one-line version:</strong> dedicated warmed domains + full authentication + low per-inbox volume + verified lists + human copy = the primary inbox.</div>
'''
    faqs3 = [
        ("Why does my cold email go to spam?",
         "<p>Usually because of poor sender reputation: an unwarmed domain, missing SPF/DKIM/DMARC authentication, too much volume from one inbox, or high bounce rates from unverified lists. Fixing the setup fixes placement.</p>"),
        ("How long does inbox warm-up take?",
         "<p>About two to three weeks. Warm-up gradually increases sending volume so mailbox providers recognise the inbox as legitimate. Skipping it is the fastest way into the spam folder.</p>"),
        ("Should I send cold email from my main domain?",
         "<p>No. Always use dedicated, separately-registered lookalike domains so that any reputation impact never touches your primary domain and its normal business email.</p>"),
    ]
    article("cold-email-deliverability",
            "Cold Email Deliverability: How to Land in the Inbox | ClearLeads",
            "Cold email deliverability comes down to warmed dedicated domains, SPF/DKIM/DMARC, low per-inbox volume, and verified lists. Here's the exact setup that avoids spam.",
            "Cold email deliverability: how we land in the inbox",
            "Deliverability", 6,
            "The infrastructure and sending discipline that decides whether your outreach is ever seen.",
            "<strong>Cold email deliverability depends on sender reputation, not clever wording.</strong> Landing in the primary inbox requires dedicated warmed domains, full SPF/DKIM/DMARC authentication, low sending volume per inbox, rigorously verified lists, and human-sounding copy that earns replies. Get those right and monitor them continuously, and spam placement stops being your bottleneck.",
            sections3, faqs3,
            related=[("cold-email-vs-linkedin-outreach", "Cold email vs LinkedIn outreach: which books more meetings?"),
                     ("how-much-does-appointment-setting-cost", "How much does appointment setting cost in 2026?")])

# ------------------------------------------------------------------
# sitemap + robots
# ------------------------------------------------------------------
def build_meta_files():
    urls = ["", "services.html", "how-it-works.html", "results.html", "about.html", "contact.html", "blog/"]
    urls += [f"{s}.html" for s, *_ in SERVICES]
    urls += [f"blog/{s}.html" for s, *_ in ARTICLES]
    items = ""
    for u in urls:
        loc = f"{SITE}/{u}" if u else f"{SITE}/"
        pri = "1.0" if u == "" else ("0.9" if u.endswith(".html") and "blog/" not in u else "0.7")
        items += f"  <url><loc>{loc}</loc><changefreq>monthly</changefreq><priority>{pri}</priority></url>\n"
    sitemap = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{items}</urlset>'''
    (b.OUT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    robots = f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n"
    (b.OUT / "robots.txt").write_text(robots, encoding="utf-8")
    # CNAME — tells GitHub Pages which custom domain serves this site
    domain = SITE.replace("https://", "").replace("http://", "").rstrip("/")
    (b.OUT / "CNAME").write_text(domain + "\n", encoding="utf-8")
    print(f"wrote sitemap.xml, robots.txt, CNAME ({domain})")

def build_404():
    """Self-contained branded 404 (inline styles so it renders at any URL depth)."""
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found | {NAME}</title>
<meta name="robots" content="noindex">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%232563EB'/%3E%3Cpath d='M9 16.5l4 4 10-10' stroke='white' stroke-width='2.6' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">
<style>
  *{{box-sizing:border-box}}
  body{{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;
    font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:#D9E2F2;padding:24px;
    background:radial-gradient(1000px 500px at 80% -10%,rgba(6,182,212,.25),transparent 60%),
      radial-gradient(800px 500px at 0% 110%,rgba(37,99,235,.35),transparent 55%),
      linear-gradient(160deg,#0A1B3D,#0E2350);}}
  .wrap{{max-width:520px}}
  .logo{{width:56px;height:56px;margin:0 auto 26px;display:block}}
  .code{{font-size:5rem;font-weight:800;letter-spacing:-.04em;line-height:1;margin:0;color:#fff;
    background:linear-gradient(100deg,#5FA0FF,#22D3EE);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}}
  h1{{color:#fff;font-size:1.6rem;margin:14px 0 8px;letter-spacing:-.02em}}
  p{{color:#B7C4DC;font-size:1.05rem;margin:0 0 28px}}
  a.btn{{display:inline-flex;align-items:center;gap:8px;background:#2563EB;color:#fff;text-decoration:none;
    font-weight:600;padding:14px 28px;border-radius:999px;box-shadow:0 8px 20px rgba(37,99,235,.35)}}
  a.btn:hover{{background:#1D4FD7}}
  .links{{margin-top:22px;font-size:.95rem}}
  .links a{{color:#7FB0FF;text-decoration:none;margin:0 10px}}
  .links a:hover{{text-decoration:underline}}
</style>
</head>
<body>
  <div class="wrap">
    <svg class="logo" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
      <rect width="32" height="32" rx="8" fill="url(#g)"/>
      <path d="M9 16.5l4 4 10-10" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
      <defs><linearGradient id="g" x1="0" y1="0" x2="32" y2="32" gradientUnits="userSpaceOnUse">
        <stop stop-color="#2563EB"/><stop offset="1" stop-color="#06B6D4"/></linearGradient></defs>
    </svg>
    <p class="code">404</p>
    <h1>This page took a wrong turn</h1>
    <p>The page you're looking for doesn't exist or has moved. Let's get you back to booking meetings.</p>
    <a class="btn" href="/">Back to home →</a>
    <div class="links">
      <a href="/services.html">Services</a>·
      <a href="/results.html">Results</a>·
      <a href="/blog/index.html">Blog</a>·
      <a href="/contact.html">Book a call</a>
    </div>
  </div>
</body>
</html>'''
    (b.OUT / "404.html").write_text(doc, encoding="utf-8")
    print("wrote 404.html")

# ------------------------------------------------------------------
def build():
    build_home()
    build_services()
    build_services_detail()
    build_how()
    build_results()
    build_about()
    build_contact()
    build_blog_index()
    build_articles()
    build_meta_files()
    build_404()
