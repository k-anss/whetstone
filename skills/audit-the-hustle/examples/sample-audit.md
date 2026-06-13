# Sample audit — fully fictional

> Every name, product, number, and URL pattern below is invented for demonstration. Any resemblance to a real person or product is coincidental.

## Request

"There's this indie hacker, **'Rilo Vance'**, building a screenshot-to-invoice tool called **SnapLedger** in public. He says he hit $6k MRR in four months. Is he really making money or selling a dream?"

## Step 1 — signal scan (reference/signals.md)

| Class | Mark | Found |
|---|---|---|
| 1. Verifiable revenue | unverifiable | MRR claimed in posts and a pinned screenshot; no processor-connected dashboard, no API-verified listing |
| 2. Third-party mentions | present (weak) | Two forum threads by unaffiliated accounts asking how SnapLedger handles VAT; one blog comparison by an author with an affiliate link (discounted) |
| 3. Real negative feedback | present | A user with a 6-year account history complaining about a double-charge and the 3-day support delay; Rilo replied with a refund confirmation |
| 4. Operational signals | present | A contractor post for OCR tuning last month; a public changelog updated 11 times in 90 days |
| 5. Timeline continuity | present | Three years of posts about freelance bookkeeping automation predating SnapLedger; texture consistent |

## Step 2 — conclusion draft (reference/confidence.md)

## Step 3 — anti-bias gate (reference/anti-bias.md)

1. Famous-name default? No — subject is unknown; same evidence bar applied.
2. Product or content-as-product? Product. No course, no paid community; posts are changelogs, not method-selling. (This check mattered: a "How I hit $6k" thread initially read as funnel; on inspection it links to the product, not to a course.)
3. Beautifying? The $6k figure itself moved my draft number upward once — moved it back; the figure is class-1-unverifiable and may not move anything.
4. Labels applied below.

## Output

**75% looks like a real operation, 25% looks like performance.**

Basis:
- Mundane, specific negative feedback from an aged account, publicly resolved — *checklist-triggered* (class 3, hardest-to-fake)
- Operational motion: contractor hire + 11 changelog entries in 90 days — *checklist-triggered* (class 4)
- Three years of consistent pre-claim history — *checklist-triggered* (class 5)
- The $6k MRR figure specifically did not move this number: it is unverifiable — *checklist-triggered* (class 1 rule)
- The VAT questions suggest real users in real jurisdictions, which is costly to stage — *own reasoning*, weight accordingly

Below the waterline (not assessed): actual revenue volume; whether any testimonials are arranged. If your real question is "is the $6k true," that's below the waterline — outside verification can establish that a real product with real users exists, not the size of the number.
