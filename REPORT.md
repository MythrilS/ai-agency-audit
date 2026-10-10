# AI Agency Audit — Report (first pass, 2026-10-07)

**Sample:** 147 raw rows → **130 unique agencies** (deduped across 4 channels: Google/listicles,
marketplaces, YouTube, X/LinkedIn). Each agency's own website audited for verifiable signals.

## Headline numbers (of 130)

| Signal | Result |
|---|---|
| **No published pricing** | **72%** (90/125 known) |
| **No named clients** | 43% (49/113 known) |
| **No case studies** | 36% (42/118 known) |
| **No proof of work at all** (neither clients nor case studies) | **34%** (44/130) |
| **LARP signals** (no team/address, funnel-only, guru/course-led, placeholder clients) | 16% (20/126) |
| Dead site | 1 (Lightpoint AI — domain parked "$55k for sale") |
| Unreachable | 1 (eSparkBiz) |

## The key finding: the space is BIMODAL

The aggregate hides a split. There are two distinct populations:

1. **Real shops** — enterprise/mid-tier firms (LeewayHertz, DataArt, Softeq, Master of Code,
   ThirdEye) with rich client rosters, case studies, years of history. These are legit.
2. **Hype funnels** — the "AI agency" gold-rush tier: template sites, guru/course funnels
   (Morningside AI / Liam Ottley, Goldie, Inflight AI), placeholder "clients" (agencyn8n.com's
   fake "TechCorp"/"StartupX"), no team page, no address, no proof.

The **pricing opacity (72%) is the one universal trait** across BOTH tiers — even the legit
enterprise shops make you "book a call." That's the robust, defensible stat.

## Publish-ready stat + angle

> "I audited 130 'AI automation agencies.' **72% don't list pricing anywhere** — you can't learn
> what they cost without a sales call. **1 in 3 have zero proof of work** (no named clients, no
> case studies). **1 in 6 are just a funnel** — no team, no address, no clients. The gold rush is
> real; a lot of it is a website and a logo."

Angle: "I measured the AI agency gold rush so you don't have to." Feeds the existing
"everyone's lying about AI agencies" narrative — with actual data behind it.

## Honesty caveats (for Michael — NOT for public)

1. **Selection bias.** Sources (listicles, directories, marketplaces) skew toward *legit* shops,
   so the real LARP rate in the wild is likely HIGHER than 16%. A random YouTube/X sample would
   look worse. Say "of the 130 I audited," never "of all AI agencies."
2. **Soft fields need human review.** "No case studies" / "LARP signals" are judgment calls. The
   sub-agents marked `unknown` when unsure, but the 34%/16% figures need a manual pass over the
   LARP list before we'd ever assert them publicly. The **72% pricing** figure is objective and
   safe to publish as-is (verifiable against the raw CSVs).
3. **Founding year is rarely stated** — the "brand new" stat is undercounted; don't publish a %.
4. **Raw data lives here** (the credibility/verifiability layer): `chunk-1..4.csv` in this dir.

## Files
- `chunk-1.csv` (41, Google/listicles) · `chunk-2.csv` (44, marketplaces)
- `chunk-3.csv` (23, YouTube) · `chunk-4.csv` (39, X/LinkedIn)
- LARP-flagged list (20) and dead/unreachable (2) are in the aggregation output.
