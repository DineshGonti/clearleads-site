#!/usr/bin/env python3
"""Generates assets/logo.png and assets/og-image.png (social share card).
Run once (or after a brand change): python3 make_images.py (needs Pillow)."""
import pathlib
from PIL import Image, ImageDraw, ImageFont

OUT = pathlib.Path(__file__).resolve().parents[1] / "assets"
OUT.mkdir(exist_ok=True)
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"
BLUE, CYAN = (37, 99, 235), (6, 182, 212)

def gradient(w, h, a, b):
    img = Image.new("RGB", (w, h))
    px = img.load()
    for y in range(h):
        for x in range(w):
            t = (x + y) / (w + h)
            px[x, y] = tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))
    return img

def logo(size):
    """Rounded gradient square with a white check mark (matches the SVG logo)."""
    s = size * 4  # supersample for smooth edges
    g = gradient(s, s, BLUE, CYAN).convert("RGBA")
    mask = Image.new("L", (s, s), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, s, s], radius=s // 4, fill=255)
    g.putalpha(mask)
    d = ImageDraw.Draw(g)
    k = s / 32
    d.line([(9 * k, 16.5 * k), (13 * k, 20.5 * k), (23 * k, 10.5 * k)],
           fill="white", width=int(2.6 * k), joint="curve")
    for x, y in [(9, 16.5), (23, 10.5)]:
        r = 1.3 * k
        d.ellipse([x * k - r, y * k - r, x * k + r, y * k + r], fill="white")
    return g.resize((size, size), Image.LANCZOS)

def og_image():
    w, h = 1200, 630
    img = gradient(w, h, (10, 27, 61), (14, 35, 80)).convert("RGBA")
    img.alpha_composite(logo(96), (80, 80))
    d = ImageDraw.Draw(img)
    d.text((196, 98), "ClearLeads", font=ImageFont.truetype(FONT_BOLD, 54), fill="white")
    title = ImageFont.truetype(FONT_BOLD, 66)
    d.text((80, 240), "Qualified B2B sales meetings,", font=title, fill="white")
    d.text((80, 322), "booked on your calendar.", font=title, fill=(95, 200, 255))
    d.text((80, 440), "Appointment setting · Cold email · LinkedIn outreach",
           font=ImageFont.truetype(FONT_REG, 34), fill=(183, 196, 220))
    d.text((80, 520), "clearleads.co", font=ImageFont.truetype(FONT_BOLD, 32), fill=(127, 176, 255))
    img.convert("RGB").save(OUT / "og-image.png", optimize=True)

if __name__ == "__main__":
    logo(512).save(OUT / "logo.png", optimize=True)
    logo(180).save(OUT / "apple-touch-icon.png", optimize=True)
    og_image()
    print("wrote assets/logo.png, assets/apple-touch-icon.png, assets/og-image.png")
