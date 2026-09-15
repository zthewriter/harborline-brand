#!/usr/bin/env python3
"""Render Harborline brand PNGs from the published colour tokens."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"

HULL_NAVY = (18, 38, 58)
BOOT_TOPPING_RED = (140, 47, 47)
SUPERSTRUCTURE_WHITE = (242, 244, 246)
SIGNAL_YELLOW = (224, 165, 18)
DECK_GREY = (91, 107, 122)
PURE_WHITE = (255, 255, 255)

FONT_DIR = Path("/System/Library/Fonts/Supplemental")
DIN = FONT_DIR / "DIN Condensed Bold.ttf"
ARIAL = FONT_DIR / "Arial.ttf"
ARIAL_BOLD = FONT_DIR / "Arial Bold.ttf"
ARIAL_NARROW_BOLD = FONT_DIR / "Arial Narrow Bold.ttf"


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size)


def _arm(
    draw: ImageDraw.ImageDraw,
    start: tuple[float, float],
    end: tuple[float, float],
    thickness: float,
    color: tuple[int, int, int],
) -> None:
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    length = math.hypot(dx, dy)
    ux, uy = dx / length, dy / length
    px, py = -uy * thickness / 2, ux * thickness / 2
    draw.polygon(
        [
            (start[0] + px, start[1] + py),
            (end[0] + px, end[1] + py),
            (end[0] - px, end[1] - py),
            (start[0] - px, start[1] - py),
        ],
        fill=color,
    )


def draw_chevron(
    draw: ImageDraw.ImageDraw,
    cx: float,
    cy: float,
    height: float,
    color: tuple[int, int, int],
    thickness: float | None = None,
) -> None:
    """Single chevron, apex uppermost, matching livery specification LIV-4."""
    width = height * 1.15
    stroke = thickness if thickness is not None else height * 0.22
    apex = (cx, cy - height / 2)
    left = (cx - width / 2, cy + height / 2)
    right = (cx + width / 2, cy + height / 2)
    # Overshoot the apex so the two arms meet as a clean peak.
    # Each arm starts behind the apex along that arm's own direction.
    overshoot = stroke * 0.35
    left_dir = (left[0] - apex[0], left[1] - apex[1])
    right_dir = (right[0] - apex[0], right[1] - apex[1])
    left_len = math.hypot(*left_dir)
    right_len = math.hypot(*right_dir)
    left_start = (
        apex[0] - (left_dir[0] / left_len) * overshoot,
        apex[1] - (left_dir[1] / left_len) * overshoot,
    )
    right_start = (
        apex[0] - (right_dir[0] / right_len) * overshoot,
        apex[1] - (right_dir[1] / right_len) * overshoot,
    )
    _arm(draw, left_start, left, stroke, color)
    _arm(draw, right_start, right, stroke, color)


def save(image: Image.Image, name: str) -> None:
    path = ASSETS / name
    image.save(path, "PNG", optimize=True)
    print(f"wrote {path.relative_to(ROOT)} ({image.size[0]}x{image.size[1]})")


def logo_icon() -> None:
    size = 1024
    image = Image.new("RGB", (size, size), HULL_NAVY)
    draw = ImageDraw.Draw(image)
    draw_chevron(draw, size / 2, size / 2 - 20, 520, SIGNAL_YELLOW, 118)
    save(image, "logo-icon.png")


def logo_mark_light() -> None:
    size = 1024
    image = Image.new("RGB", (size, size), SUPERSTRUCTURE_WHITE)
    draw = ImageDraw.Draw(image)
    draw_chevron(draw, size / 2, size / 2 - 20, 520, HULL_NAVY, 118)
    save(image, "logo-mark-light.png")


def chevron_yellow() -> None:
    size = 512
    image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw_chevron(draw, size / 2, size / 2, 320, SIGNAL_YELLOW, 72)
    save(image, "chevron-yellow.png")


def chevron_navy() -> None:
    size = 512
    image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw_chevron(draw, size / 2, size / 2, 320, HULL_NAVY, 72)
    save(image, "chevron-navy.png")


def wordmark(bg: tuple[int, int, int], fg: tuple[int, int, int], chevron: tuple[int, int, int], name: str) -> None:
    width, height = 1600, 420
    image = Image.new("RGB", (width, height), bg)
    draw = ImageDraw.Draw(image)
    draw_chevron(draw, 210, 210, 210, chevron, 48)
    word = font(DIN, 168)
    draw.text((390, 118), "HARBORLINE", font=word, fill=fg)
    small = font(ARIAL, 28)
    draw.text((396, 292), "FERRIES", font=small, fill=chevron)
    save(image, name)


def email_header() -> None:
    width, height = 1200, 240
    image = Image.new("RGB", (width, height), HULL_NAVY)
    draw = ImageDraw.Draw(image)
    draw_chevron(draw, 96, 120, 88, SIGNAL_YELLOW, 20)
    word = font(DIN, 78)
    draw.text((170, 58), "HARBORLINE", font=word, fill=PURE_WHITE)
    small = font(ARIAL, 18)
    draw.text((174, 150), "FERRIES", font=small, fill=SIGNAL_YELLOW)
    save(image, "email-header.png")


def email_footer() -> None:
    width, height = 1200, 160
    image = Image.new("RGB", (width, height), HULL_NAVY)
    draw = ImageDraw.Draw(image)
    draw_chevron(draw, 64, 80, 52, SIGNAL_YELLOW, 12)
    label = font(ARIAL_BOLD, 22)
    draw.text((120, 40), "Harborline Ferries", font=label, fill=PURE_WHITE)
    meta = font(ARIAL, 17)
    draw.text((120, 86), "Kelsall Quay   ·   Nethergill   ·   Tolquin Pier   ·   Braewick Slip", font=meta, fill=SIGNAL_YELLOW)
    save(image, "email-footer.png")


def brand_kit() -> None:
    width, height = 1600, 1100
    image = Image.new("RGB", (width, height), PURE_WHITE)
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, width, 150), fill=HULL_NAVY)
    title = font(DIN, 54)
    draw.text((64, 36), "HARBORLINE FERRIES", font=title, fill=PURE_WHITE)
    sub = font(ARIAL, 22)
    draw.text((66, 100), "Brand colours  ·  Specification LIV-4  ·  Applies to all customer materials", font=sub, fill=SIGNAL_YELLOW)

    swatches = [
        ("Hull Navy", "#12263A", "Primary. Headers, wordmark ground, email masthead.", HULL_NAVY, PURE_WHITE),
        ("Signal Yellow", "#E0A512", "Action. Buttons, chevron on navy, vessel names.", SIGNAL_YELLOW, HULL_NAVY),
        ("Superstructure White", "#F2F4F6", "Page and letter ground. Body sits on this, not pure white.", SUPERSTRUCTURE_WHITE, HULL_NAVY),
        ("Deck Grey", "#5B6B7A", "Supporting text, captions, rules, secondary labels.", DECK_GREY, PURE_WHITE),
        ("Boot Topping Red", "#8C2F2F", "Warning and cancellation only. Never decorative.", BOOT_TOPPING_RED, PURE_WHITE),
    ]

    top = 210
    row_h = 150
    for i, (name, hex_code, use, fill, text) in enumerate(swatches):
        y = top + i * row_h
        draw.rectangle((64, y, 214, y + 110), fill=fill)
        draw.rectangle((64, y, 214, y + 110), outline=HULL_NAVY if fill == SUPERSTRUCTURE_WHITE else fill, width=2)
        name_font = font(ARIAL_NARROW_BOLD if ARIAL_NARROW_BOLD.exists() else ARIAL_BOLD, 36)
        hex_font = font(ARIAL_BOLD, 24)
        use_font = font(ARIAL, 22)
        draw.text((250, y + 12), name, font=name_font, fill=HULL_NAVY)
        draw.text((250, y + 56), hex_code, font=hex_font, fill=fill if fill != SUPERSTRUCTURE_WHITE else DECK_GREY)
        draw.text((460, y + 56), use, font=use_font, fill=DECK_GREY)

    note = font(ARIAL, 18)
    draw.text(
        (64, 1000),
        "Funnel mark: a single navy chevron, apex uppermost. Wordmark: HARBORLINE in capitals, never Harbourline, never Harbor Line.",
        font=note,
        fill=DECK_GREY,
    )
    save(image, "brand-kit.png")


def write_svgs() -> None:
    chevron_path = (
        '<polyline points="18,82 50,22 82,82" fill="none" '
        'stroke="{color}" stroke-width="16" stroke-linejoin="miter" stroke-linecap="butt"/>'
    )
    icon = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" aria-label="Harborline chevron">
  <rect width="100" height="100" fill="#12263A"/>
  {chevron_path.format(color="#E0A512")}
</svg>
"""
    mark = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" aria-label="Harborline chevron on light">
  <rect width="100" height="100" fill="#F2F4F6"/>
  {chevron_path.format(color="#12263A")}
</svg>
"""
    wordmark = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 140" role="img" aria-label="Harborline Ferries">
  <rect width="640" height="140" fill="#12263A"/>
  <polyline points="28,108 70,36 112,108" fill="none" stroke="#E0A512" stroke-width="14" stroke-linejoin="miter"/>
  <text x="140" y="82" fill="#FFFFFF" font-family="Arial Narrow, Arial, sans-serif" font-size="54" font-weight="700" letter-spacing="4">HARBORLINE</text>
  <text x="142" y="112" fill="#E0A512" font-family="Arial, sans-serif" font-size="14" letter-spacing="6">FERRIES</text>
</svg>
"""
    (ASSETS / "logo-icon.svg").write_text(icon)
    (ASSETS / "logo-mark-light.svg").write_text(mark)
    (ASSETS / "logo-wordmark.svg").write_text(wordmark)
    print("wrote SVG marks")


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    logo_icon()
    logo_mark_light()
    chevron_yellow()
    chevron_navy()
    wordmark(HULL_NAVY, PURE_WHITE, SIGNAL_YELLOW, "logo-wordmark.png")
    wordmark(SUPERSTRUCTURE_WHITE, HULL_NAVY, HULL_NAVY, "logo-wordmark-light.png")
    email_header()
    email_footer()
    brand_kit()
    write_svgs()


if __name__ == "__main__":
    main()
