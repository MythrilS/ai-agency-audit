# The AI Agency Audit

I audited **130 "AI automation agencies"** and measured what each one actually publishes on its own website.

**Headline: 72% don't list pricing anywhere.** You can't learn what most of them charge without a sales call.

## What I measured

For each agency, from its own public site:

| Signal | Result |
|---|---|
| No published pricing | **72%** (90 of 125 sites that loaded) |
| No named clients | 43% (49 of 113) |
| No case studies | 36% (42 of 118) |
| No proof of work (neither clients nor case studies) | **34%** (44 of 130) |
| "Funnel" signals (no team, no address, course/guru-led, placeholder clients) | 16% (20 of 126) |

## Method

- **130 unique agencies**, deduplicated from 147 raw rows across four sources: Google/listicles, marketplaces (Clutch/Upwork/G2), YouTube, and X/LinkedIn.
- Each agency's **own website** was read for verifiable signals: does it list pricing, name clients, show case studies, name a team or address?
- Structured audit in `chunk-1..4.csv`; per-agency classification signals in `signals.json`; supporting page snapshots in `pages/` and `raw/`.

## Honest caveats

1. **This is not a random sample.** Listicles and marketplaces skew toward established shops, so the "funnel" rate in the wild is likely *higher* than 16%, not lower. Read every percentage as "of the 130 I audited," not "of the AI agency industry."
2. **Pricing is objective; the rest is judgment.** "Does it list pricing?" is a yes/no verifiable against the URL in each row. "Funnel" and "proof of work" are classifications from the site content — `signals.json` holds the raw signals behind each call, so you can re-derive and disagree.
3. **"Funnel" ≠ "scam."** A solo founder with no team page isn't dishonest — it just means there's less public proof to evaluate. Draw your own conclusion from the data.

## Files

- `chunk-1.csv` (41, Google/listicles) · `chunk-2.csv` (44, marketplaces) · `chunk-3.csv` (23, YouTube) · `chunk-4.csv` (39, X/LinkedIn)
- `signals.json` — raw classification signals per agency
- `REPORT.md` — full writeup
- `audit-chart.png` + `make_chart.py` — the visualization and how it's generated

*Collected 2026-10-07. Every row carries the source URL — verify any of it yourself.*
