#!/usr/bin/env python3
"""ClearLeads static site generator.
Outputs SEO/AEO-optimized static HTML for clearleads.co."""
import os, json, html, pathlib

SITE = "https://clearleads.co"
NAME = "ClearLeads"
CSS_VER = "7"   # bump to bust the stylesheet cache on deploy
OUT = pathlib.Path(__file__).resolve().parents[1]
BOOK = "contact.html"      # book-a-call conversion page

LOGO_SVG = (
    '<svg class="logo" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
    '<rect width="32" height="32" rx="8" fill="url(#lg)"/>'
    '<path d="M9 16.5l4 4 10-10" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'
    '<defs><linearGradient id="lg" x1="0" y1="0" x2="32" y2="32" gradientUnits="userSpaceOnUse">'
    '<stop stop-color="#2563EB"/><stop offset="1" stop-color="#06B6D4"/></linearGradient></defs></svg>'
)

# ---- service catalog (drives nav dropdown, home cards, sitemap) ----
SERVICES = [
    ("appointment-setting",  "Appointment Setting",     "Qualified sales meetings booked straight to your calendar.", True),
    ("cold-email",           "Done-For-You Cold Email", "Inbox setup, deliverability, copy, sending & reply handling.", False),
    ("linkedin-outreach",    "LinkedIn Outreach",       "Targeted social selling that complements your email channel.", False),
    ("lead-lists",           "Lead List Building & Data","Verified, targeted prospect lists built to your ICP.", False),
    ("database-reactivation","Database Reactivation",   "Revive old and cold leads with fresh, relevant sequences.", False),
    ("outbound-system-setup","Outbound System Setup",   "A one-time build of your entire outreach machine.", False),
]

# small inline icons
ICONS = {
    "calendar":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>',
    "mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
    "linkedin":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v6h-4v-6a2 2 0 0 0-4 0v6h-4v-10h4v1.5"/><rect x="2" y="9" width="4" height="11"/><circle cx="4" cy="4" r="2"/></svg>',
    "list":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/></svg>',
    "refresh":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 0 1 15-6.7L21 8M21 3v5h-5M21 12a9 9 0 0 1-15 6.7L3 16M3 21v-5h5"/></svg>',
    "settings":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>',
    "target":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
    "shield":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    "chart":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18M7 15l3-4 3 2 4-6"/></svg>',
    "bolt":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 3 14h7l-1 8 10-12h-7l1-8z"/></svg>',
}
SVC_ICON = {
    "appointment-setting":"calendar","cold-email":"mail","linkedin-outreach":"linkedin",
    "lead-lists":"list","database-reactivation":"refresh","outbound-system-setup":"settings",
}

def chev():
    return '<svg class="chev" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg>'

def arrow():
    return '<svg class="arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

# ---------- shared chrome (prefix = "" for root pages, "../" for /blog pages) ----------
def header(prefix=""):
    dd = "".join(
        f'<a href="{prefix}{s}.html">{t}<span>{d}</span></a>' for s,t,d,_ in SERVICES
    )
    return f'''<header class="site-header">
  <div class="container nav">
    <a class="brand" href="{prefix or './'}">{LOGO_SVG}ClearLeads</a>
    <button class="menu-toggle" aria-label="Menu" onclick="document.getElementById('nav').classList.toggle('open')">
      <svg viewBox="0 0 24 24" fill="none" stroke="#0B1220" stroke-width="2" stroke-linecap="round"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
    </button>
    <nav class="nav-links" id="nav">
      <div class="has-dd"><a href="{prefix}services.html">Services ▾</a>
        <div class="dd-menu">{dd}</div>
      </div>
      <a href="{prefix}how-it-works.html">How It Works</a>
      <a href="{prefix}results.html">Results</a>
      <a href="{prefix}about.html">About</a>
      <a href="{prefix}blog/">Blog</a>
      <a href="{prefix}{BOOK}" class="btn btn-primary nav-mobile-cta">Book a call</a>
    </nav>
    <span class="nav-spacer"></span>
    <div class="nav-cta">
      <a href="{prefix}{BOOK}" class="btn btn-primary">Book a call {arrow()}</a>
    </div>
  </div>
</header>'''

def footer(prefix=""):
    svc = "".join(f'<li><a href="{prefix}{s}.html">{t}</a></li>' for s,t,_,_ in SERVICES)
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="foot-grid">
      <div class="foot-brand">
        <a class="brand" href="{prefix or './'}">{LOGO_SVG}ClearLeads</a>
        <p>Outbound lead generation and appointment setting for B2B teams. We book qualified sales meetings straight to your calendar. You close the deals.</p>
      </div>
      <div><h2 class="foot-h">Services</h2><ul>{svc}</ul></div>
      <div><h2 class="foot-h">Company</h2><ul>
        <li><a href="{prefix}how-it-works.html">How It Works</a></li>
        <li><a href="{prefix}results.html">Results</a></li>
        <li><a href="{prefix}about.html">About</a></li>
        <li><a href="{prefix}blog/">Blog</a></li>
        <li><a href="{prefix}{BOOK}">Contact</a></li>
      </ul></div>
      <div><h2 class="foot-h">Get started</h2><ul>
        <li><a href="{prefix}{BOOK}">Book a call</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="{prefix}results.html">Case studies</a></li>
      </ul></div>
    </div>
    <div class="foot-bottom">
      <span>© 2026 ClearLeads. All rights reserved.</span>
      <span>clearleads.co · B2B Lead Generation Agency</span>
    </div>
  </div>
</footer>'''

def cta_band(prefix="",
             title="Ready to fill your calendar with qualified meetings?",
             sub="Book a 30-minute strategy call. We'll map your ICP, show you the plan, and give you a realistic meeting forecast. No pressure, no long contracts.",
             btn="Book your strategy call"):
    return f'''<section class="cta-band">
  <div class="container">
    <div class="box">
      <div class="container narrow" style="padding:0">
        <h2>{title}</h2>
        <p>{sub}</p>
        <div class="btns">
          <a href="{prefix}{BOOK}" class="btn btn-accent btn-lg">{btn} {arrow()}</a>
          <a href="{prefix}results.html" class="btn btn-ghost on-dark btn-lg">See results</a>
        </div>
      </div>
    </div>
  </div>
</section>'''

def faq_block(items, heading="Frequently asked questions", intro=None):
    rows = ""
    for q,a in items:
        rows += f'<details><summary>{q}{chev()}</summary><div class="a">{a}</div></details>'
    intro_html = f'<p>{intro}</p>' if intro else ''
    return f'''<section class="bg-soft">
  <div class="container">
    <div class="section-head"><span class="eyebrow">FAQ</span><h2>{heading}</h2>{intro_html}</div>
    <div class="faq">{rows}</div>
  </div>
</section>'''

def faq_schema(items):
    return {
        "@context":"https://schema.org","@type":"FAQPage",
        "mainEntity":[{"@type":"Question","name":q,
            "acceptedAnswer":{"@type":"Answer","text":strip_tags(a)}} for q,a in items]
    }

def strip_tags(s):
    import re
    return re.sub(r"<[^>]+>","",s).strip()

EMAIL = "dinesh@clearleads.co"
OG_IMAGE = f"{SITE}/assets/og-image.png"
# Add real profile URLs here once they exist (LinkedIn, Clutch, G2…); they feed
# Organization.sameAs, which search engines and LLMs use to confirm the entity.
SAME_AS = []

ORG_SCHEMA = {
    "@context":"https://schema.org","@type":"Organization","@id":f"{SITE}/#org",
    "name":NAME,"url":f"{SITE}/","logo":f"{SITE}/assets/logo.png","image":OG_IMAGE,
    "email":EMAIL,"slogan":"Qualified B2B sales meetings, booked on your calendar.",
    "description":"ClearLeads is a B2B lead generation and appointment setting agency. We book qualified sales meetings for B2B companies through done-for-you cold email and LinkedIn outreach, verified lead lists, and database reactivation.",
    "areaServed":"Worldwide",
    "knowsAbout":["B2B lead generation","Appointment setting","Outsourced SDR","Cold email outreach",
                  "Email deliverability","LinkedIn outreach","Sales prospecting","Lead list building",
                  "Database reactivation","Outbound sales"],
    "contactPoint":{"@type":"ContactPoint","contactType":"sales","email":EMAIL,
                    "url":f"{SITE}/{BOOK}","availableLanguage":"English"},
    **({"sameAs":SAME_AS} if SAME_AS else {}),
}
WEBSITE_SCHEMA = {
    "@context":"https://schema.org","@type":"WebSite","@id":f"{SITE}/#website",
    "url":f"{SITE}/","name":NAME,"inLanguage":"en","publisher":{"@id":f"{SITE}/#org"},
}

def breadcrumb_schema(crumbs):
    """crumbs: [(name, path), ...] after Home; path relative to site root."""
    items = [("Home", "")] + list(crumbs)
    return {"@context":"https://schema.org","@type":"BreadcrumbList",
            "itemListElement":[{"@type":"ListItem","position":i,"name":n,"item":f"{SITE}/{p}"}
                               for i,(n,p) in enumerate(items,1)]}

def page(slug, title, desc, body, schemas=None, active="", prefix="", canonical=None,
         crumbs=None, og_type="website", published=None, modified=None):
    schemas = schemas or []
    schemas = [ORG_SCHEMA] + ([WEBSITE_SCHEMA] if slug == "index.html" else []) \
              + ([breadcrumb_schema(crumbs)] if crumbs else []) + schemas
    schema_html = "\n".join(
        f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas
    )
    canon = canonical or f"{SITE}/{slug}"
    art_meta = ""
    if og_type == "article":
        art_meta = (f'\n<meta property="article:published_time" content="{published}">'
                    f'\n<meta property="article:modified_time" content="{modified}">')
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
<meta name="theme-color" content="#0A1B3D">
<link rel="canonical" href="{canon}">
<link rel="alternate" type="text/plain" title="LLM summary" href="{SITE}/llms.txt">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:site_name" content="{NAME}">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="ClearLeads: qualified B2B sales meetings, booked on your calendar">{art_meta}
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{OG_IMAGE}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}css/styles.css?v={CSS_VER}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%232563EB'/%3E%3Cpath d='M9 16.5l4 4 10-10' stroke='white' stroke-width='2.6' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">
<link rel="apple-touch-icon" href="{prefix}assets/apple-touch-icon.png">
{schema_html}
</head>
<body>
{header(prefix)}
<main>
{body}
</main>
{footer(prefix)}
<script>
// mobile menu auto-close on resize
window.addEventListener('resize',function(){{if(window.innerWidth>720){{document.getElementById('nav').classList.remove('open');}}}});
</script>
</body>
</html>'''
    path = OUT / (slug if slug.endswith(".html") else slug)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(doc, encoding="utf-8")
    print("wrote", path.relative_to(OUT))

# convenience
def svc_icon_html(slug):
    return f'<div class="ico">{ICONS[SVC_ICON[slug]]}</div>'

# ============================================================
# Build pages (imported from content module below)
# ============================================================
if __name__ == "__main__":
    import content
    content.build()
    print("\nBuild complete.")
