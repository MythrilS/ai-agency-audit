# Home-Services Call Audit — Dayton, OH

A silent-call audit of how home-services businesses in the Dayton, OH area handle
inbound phone calls during business hours.

## Method
- Called 35 home-services businesses (HVAC, plumbing, roofing, electrical, garage
  doors, landscaping, painting, pest control) during business hours (weekdays,
  roughly 1–4 PM).
- Stayed silent on each call and logged the outcome. No selling, no script.
- Outcomes: `answered` (a human picked up), `voicemail`, `auto-attendant`
  (menu / "press 1 for…"), `disconnected` (dead line).

## Results
| Outcome | Count | Share |
|---|---|---|
| Answered (live human) | 23 | 66% |
| Voicemail | 7 | 20% |
| Auto-attendant | 4 | 11% |
| Disconnected (dead line) | 1 | 3% |
| **Total** | **35** | 100% |

**Key finding:** 11 of 35 calls (31%) went to voicemail or an auto-attendant
instead of a live human — roughly 1 in 3. Add the 1 dead line and 12 of 35 (34%)
never reached a person at all.

See `outcomes-by-trade.csv` for the breakdown by trade.

## Anonymization
Business names, phone numbers, owner names, and emails are removed. Only trade and
outcome are published.

## Caveats
- Single-city sample (Dayton metro). Not a claim about all home-services businesses.
- One business had a live website but a dead number listed on Yelp/BBB (counted as
  `disconnected`).
