# Harborline design system

Use these colors, type, and marks for every customer-facing piece. They come from vessel livery specification LIV-4. Do not invent a second palette.

## Color

Always write the color by its Harborline name, then the hex.

| Name | Hex | Use |
|---|---|---|
| Hull Navy | `#12263A` | Primary. Headers, the wordmark ground, the email masthead, text on Signal Yellow. |
| Signal Yellow | `#E0A512` | Action. Buttons, the chevron on navy, vessel names on the hull. |
| Superstructure White | `#F2F4F6` | Page and letter ground. Body text sits on this, not on pure white. |
| Deck Grey | `#5B6B7A` | Supporting text, captions, rules, secondary labels. |
| Boot Topping Red | `#8C2F2F` | Warning and cancellation only. Never decorative. Never a button. |

### Pairings that are allowed

- Hull Navy ground, Superstructure White text, Signal Yellow chevron and button.
- Superstructure White ground, Hull Navy body, Deck Grey supporting text, Signal Yellow button with Hull Navy label.
- Signal Yellow button, Hull Navy label. Never white label on yellow.

### Pairings that are refused

- Signal Yellow text on Superstructure White. The contrast fails.
- Boot Topping Red as a header, a logo color, or a call to action.
- Pure black `#000000` or a generic blue. If you need dark, use Hull Navy.
- A second yellow, a second navy, or a "warmer" red.

The brand kit image at `assets/brand-kit.png` shows the five swatches in this order. If a piece needs a picture of the colors, use that file. Do not re-draw them.

## The chevron

The company mark is a **single chevron, apex uppermost**. On the funnel it is Hull Navy and 1.2 m tall. In print and email it is the same shape at any size.

- On Hull Navy, draw it in Signal Yellow.
- On Superstructure White, draw it in Hull Navy.
- Never add a vessel name to the mark.
- Never add a second chevron, a circle, a wave, or an anchor.
- Never rotate it. The apex stays up.

Files:

- `assets/logo-icon.png` and `assets/logo-icon.svg` — yellow chevron on Hull Navy
- `assets/logo-mark-light.png` and `assets/logo-mark-light.svg` — navy chevron on Superstructure White
- `assets/chevron-yellow.png` — transparent yellow chevron for emails
- `assets/chevron-navy.png` — transparent navy chevron for light grounds

## Wordmark

Write **HARBORLINE** in capitals, then **FERRIES** in a smaller tracking line underneath.

- Never write Harbourline, Harbor Line, HarborLine, or HL Ferries.
- Letterform: DIN Condensed Bold. If DIN is not available, Arial Narrow Bold.
- On navy: wordmark in white, FERRIES in Signal Yellow.
- On light: both lines in Hull Navy.
- Files: `assets/logo-wordmark.png`, `assets/logo-wordmark-light.png`, `assets/logo-wordmark.svg`.

## Type

| Use | Face | Colour |
|---|---|---|
| Wordmark | DIN Condensed Bold | White on navy, Hull Navy on light |
| Headings in letters and email | Arial Narrow Bold, or Arial Bold | Hull Navy |
| Body of a letter or email | Georgia | Hull Navy |
| Supporting line, caption, address | Arial | Deck Grey |
| Button label | Arial Bold | Hull Navy on Signal Yellow |

Email-safe stack:

- Headings: `Arial, Helvetica, sans-serif`
- Body: `Georgia, 'Times New Roman', serif`

Sizes for a 600 px email:

- Masthead wordmark: the header image, do not reset type over it
- Greeting and headings: 22 px
- Body: 16 px, line-height 1.5
- Supporting text and footer: 13 px
- Button label: 16 px, bold

## Email layout

A Harborline email is a 600 px letter on Superstructure White, not a marketing page.

1. Masthead: Hull Navy bar, 120 px tall. Use `assets/email-header.png`. If the image does not load, the cell is still Hull Navy and still reads HARBORLINE.
2. One greeting. No preheader pun, no hero photograph of a sunset.
3. Short body in Georgia, Hull Navy.
4. One Signal Yellow button. Label names the action, usually `View your booking`. The label is Hull Navy.
5. A short list of facts the passenger needs on the day, if the letter is operational.
6. Sign-off: `See you on the quay` then `Harborline Ferries`.
7. Footer: `assets/email-footer.png`, or a Hull Navy bar naming Kelsall Quay, Nethergill, Tolquin Pier, and Braewick Slip.

Do not add a second button. Do not add social icons. Do not add a stock photograph of a ferry.

The canonical new-customer letter is `emails/welcome.html`. Follow it rather than inventing a layout.

## Imagery

Harborline images are the mark, the wordmark, and the color sheet. There is no mascot and no lifestyle photography in this kit.

When an assistant is asked to use the brand colors or the brand kit, the file to return is `assets/brand-kit.png`. When the letter itself needs a picture, use the header and the chevron. Do not describe the logo in prose and omit the file.

## What this system is not

It is not a website theme and it is not a permission to restyle the vessels. Hull color, boot topping, funnel mark, and deck coating stay on specification LIV-4. Customer paper follows the same five colors so a letter and a hull are visibly the same company.
