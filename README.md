# ClearLeads website (clearleads.co)

A fast, static, SEO/AEO-optimized marketing site for ClearLeads — a B2B lead
generation & appointment-setting agency. Built per the *ClearLeads Website
Strategy* brief.

## What's here

| Page | File | Targets |
|------|------|---------|
| Home | `index.html` | "B2B lead generation agency", "hire lead generation agency" |
| Services overview | `services.html` | "outsourced SDR / sales development services" |
| Appointment Setting (flagship) | `appointment-setting.html` | "appointment setting services / company" |
| Cold Email | `cold-email.html` | "cold email agency", "done-for-you cold email" |
| LinkedIn Outreach | `linkedin-outreach.html` | "linkedin outreach services" |
| Lead Lists & Data | `lead-lists.html` | "b2b lead list building" |
| Database Reactivation | `database-reactivation.html` | "database reactivation" |
| Outbound System Setup | `outbound-system-setup.html` | "outbound system build" |
| How It Works | `how-it-works.html` | process / delivery |
| Results | `results.html` | case studies, proof |
| About | `about.html` | credibility |
| Contact / Book a call | `contact.html` | "hire", Calendly embed (primary conversion) |
| Blog index | `blog/index.html` | resources hub |
| Articles | `blog/*.html` | 3 FAQ-rich, AEO-optimized guides |
| `sitemap.xml`, `robots.txt` | — | crawlability |

## SEO / AEO built in
- Unique `<title>` (~55 chars) + meta description per page, canonical + Open Graph.
- One intent-matched `<h1>`; H2s for sub-topics.
- **Direct-answer blocks** (40–60 words) opening every key page — the passages LLMs cite.
- **FAQ sections** with **FAQPage JSON-LD** on every key page.
- **Organization** + **Service** + **Article** JSON-LD.
- Clean URLs (`/appointment-setting`), internal linking, mobile-first, HTTPS-ready.
- "Book a call" CTA in header, mid-page, and footer everywhere.

## Editing & rebuilding
The HTML is **generated** — don't hand-edit the `.html` files; edit the source and rebuild:

- Copy, pages, per-service data → `build/content.py`
- Layout, shared header/footer/SEO, schema → `build/build.py`
- Styles → `css/styles.css` (bump `CSS_VER` in `build/build.py` after CSS changes)

```bash
cd build && python3 build.py      # regenerates all pages + sitemap/robots
```

## Preview locally
```bash
python3 -m http.server 5051 --directory .
# open http://localhost:5051
```

## Deploy
It's fully static — drop the folder on Netlify, Vercel, Cloudflare Pages, S3, or any host.

### Before launch — replace placeholders
1. **Calendly** — swap the placeholder in `contact.html` (`build_contact()` in content.py) for your real scheduling embed.
2. **Contact form** — wire the form to a backend/form service (currently shows a client-side thank-you).
3. **Social proof** — replace sample logos, testimonials, and case-study numbers with real ones as you get them.
4. **Off-site authority (AEO)** — create Clutch / G2 / Trustpilot profiles and update the `sameAs` links in `ORG_SCHEMA` (build.py).
5. **`dinesh@clearleads.co`** is the public contact email (`EMAIL` in `build/build.py`).
6. Add an OG image at `assets/` and reference it, and a real favicon PNG.
