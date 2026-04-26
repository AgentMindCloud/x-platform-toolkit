#!/usr/bin/env python3
"""Generate 1200x630 OG poster PNGs for x-platform-toolkit.

Produces:
  docs/posters/og-default.png            — repo-level card (root README + fallback)
  docs/posters/og-tool-NN-<slug>.png     — one per tool (20)

Run:
  pip install pillow cairosvg
  python scripts/rasterize_posters.py
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Optional

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
TOOLS_DIR = ROOT / "tools"
OUT_DIR = ROOT / "docs" / "posters"
OUT_DIR.mkdir(parents=True, exist_ok=True)

W, H = 1200, 630
BG = (10, 10, 15)
FG = (235, 248, 255)
MUTED = (161, 161, 170)
DIM = (82, 82, 91)
NEON_CYAN = (34, 211, 238)
NEON_PURPLE = (168, 85, 247)
NEON_MAGENTA = (236, 72, 153)
NEON_LIME = (163, 230, 53)
LIVE = NEON_LIME
SPEC = NEON_PURPLE


def find_font(candidates: list[str], size: int) -> ImageFont.FreeTypeFont:
    for c in candidates:
        try:
            return ImageFont.truetype(c, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


SANS_BOLD = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
]
SANS_REG = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
]
MONO = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf",
    "/System/Library/Fonts/Menlo.ttc",
]


def wrap(text: str, font: ImageFont.FreeTypeFont, max_width: int, draw: ImageDraw.ImageDraw) -> list[str]:
    words = text.split()
    lines: list[str] = []
    cur = ""
    for w in words:
        candidate = f"{cur} {w}".strip()
        if draw.textlength(candidate, font=font) <= max_width:
            cur = candidate
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_gradient_bar(img: Image.Image, y: int, h: int, c1: tuple[int, int, int], c2: tuple[int, int, int]) -> None:
    px = img.load()
    for x in range(W):
        t = x / max(W - 1, 1)
        r = int(c1[0] + (c2[0] - c1[0]) * t)
        g = int(c1[1] + (c2[1] - c1[1]) * t)
        b = int(c1[2] + (c2[2] - c1[2]) * t)
        for yy in range(y, y + h):
            px[x, yy] = (r, g, b)


def render_poster(
    out_path: Path,
    eyebrow: str,
    title: str,
    tagline: str,
    accent: tuple[int, int, int],
    badge: Optional[str] = None,
    badge_color: Optional[tuple[int, int, int]] = None,
) -> None:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    draw_gradient_bar(img, 0, 4, NEON_CYAN, NEON_PURPLE)
    draw_gradient_bar(img, H - 4, 4, NEON_PURPLE, NEON_MAGENTA)

    f_eyebrow = find_font(MONO, 22)
    f_title_lg = find_font(SANS_BOLD, 96)
    f_title_md = find_font(SANS_BOLD, 76)
    f_tagline = find_font(SANS_REG, 30)
    f_footer = find_font(MONO, 18)
    f_badge = find_font(MONO, 18)

    pad_x = 80
    cur_y = 90

    draw.text((pad_x, cur_y), eyebrow.upper(), fill=accent, font=f_eyebrow)
    cur_y += 50

    f_title = f_title_lg
    if draw.textlength(title, font=f_title) > W - pad_x * 2:
        f_title = f_title_md
    title_lines = wrap(title, f_title, W - pad_x * 2, draw)
    for line in title_lines:
        draw.text((pad_x, cur_y), line, fill=FG, font=f_title)
        bbox = draw.textbbox((pad_x, cur_y), line, font=f_title)
        cur_y = bbox[3] + 8

    cur_y += 24
    tagline_lines = wrap(tagline, f_tagline, W - pad_x * 2, draw)[:3]
    for line in tagline_lines:
        draw.text((pad_x, cur_y), line, fill=MUTED, font=f_tagline)
        bbox = draw.textbbox((pad_x, cur_y), line, font=f_tagline)
        cur_y = bbox[3] + 6

    if badge:
        bg_color = badge_color or accent
        bw = int(draw.textlength(badge, font=f_badge)) + 28
        bh = 36
        bx = W - pad_x - bw
        by = 90
        draw.rounded_rectangle((bx, by, bx + bw, by + bh), radius=6, fill=bg_color)
        text_color = (10, 10, 15)
        tx = bx + 14
        ty = by + (bh - f_badge.size) // 2 - 2
        draw.text((tx, ty), badge, fill=text_color, font=f_badge)

    footer = "x-platform-toolkit  ·  Apache 2.0  ·  part of the grok-install family"
    fw = draw.textlength(footer, font=f_footer)
    draw.text(((W - fw) / 2, H - 50), footer, fill=DIM, font=f_footer)

    img.save(out_path, "PNG", optimize=True)
    print(f"  wrote {out_path.relative_to(ROOT)}")


def extract_tagline(readme: Path) -> str:
    if not readme.exists():
        return ""
    for line in readme.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s.startswith("> ") and not s.startswith("> ["):
            return s[2:].strip()
    return ""


def display_name(slug: str) -> str:
    """Pull the authoritative H1 from tools/<slug>/README.md, falling back to slug-derived."""
    readme = TOOLS_DIR / slug / "README.md"
    if readme.exists():
        text = readme.read_text(encoding="utf-8").splitlines()
        in_fm = False
        fm_seen = 0
        for line in text:
            if line.strip() == "---":
                fm_seen += 1
                in_fm = fm_seen == 1
                continue
            if (fm_seen >= 2 or fm_seen == 0) and line.startswith("# "):
                heading = line[2:].strip()
                if " · " in heading:
                    heading = heading.split(" · ", 1)[1]
                return heading
    parts = slug.split("-", 1)
    name = parts[1] if len(parts) == 2 and parts[0].isdigit() else slug
    return " ".join(w.capitalize() for w in name.split("-"))


def is_live(tool_dir: Path) -> bool:
    return (tool_dir / "index.html").exists()


def main() -> None:
    print("Generating posters in", OUT_DIR.relative_to(ROOT))

    render_poster(
        OUT_DIR / "og-default.png",
        eyebrow="x-platform-toolkit · 20 tools",
        title="20 tools X never built",
        tagline="Open-source analytics, AI writing, monetization, and automation for X creators. Apache 2.0 · self-hostable · ToS-respecting.",
        accent=NEON_CYAN,
        badge="APACHE 2.0",
        badge_color=NEON_CYAN,
    )

    tool_dirs = sorted(d for d in TOOLS_DIR.iterdir() if d.is_dir())
    for d in tool_dirs:
        slug = d.name
        m = re.match(r"^(\d{2})-(.+)$", slug)
        if not m:
            print(f"  skip (no NN- prefix): {slug}")
            continue
        num = m.group(1)
        nice = display_name(slug)
        tagline = extract_tagline(d / "README.md") or f"Tool {num} — see the spec."
        live = is_live(d)
        accent = NEON_LIME if live else NEON_PURPLE
        badge = "LIVE" if live else "SPEC'D"
        out = OUT_DIR / f"og-tool-{slug}.png"
        render_poster(
            out,
            eyebrow=f"Tool {num} · x-platform-toolkit",
            title=nice,
            tagline=tagline,
            accent=accent,
            badge=badge,
            badge_color=accent,
        )

    print(f"Done. {len(list(OUT_DIR.glob('og-*.png')))} posters written.")


if __name__ == "__main__":
    main()
