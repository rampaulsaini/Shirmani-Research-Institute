# SRI Global Market Research Register

**Snapshot:** 24 November 2026  
**Purpose:** Build a lawful, source-linked understanding of institutional needs across countries and institution segments, while prioritizing the first genuine paid SRI order.

## Evidence rules

- A directory listing is an organization-discovery source, not evidence of buyer intent.
- A procurement notice is evidence of a stated requirement, not evidence that SRI is qualified, has applied, or has been selected.
- A public contact channel is not a contact attempt. Contact status changes only after an actual message or documented two-way exchange.
- Job vacancies, calls for individual consultants, expired tenders, and generic institutional pages are market signals, not customer enquiries.
- Record only official public organization-level channels where the organization explicitly publishes them for business/procurement use. Do not harvest personal contact details.
- Never send bulk outreach. The standing limit remains at most three individually researched, high-fit first-contact emails per automation run. Follow tender communication rules, local laws, opt-outs, bounce suppression, and refusal suppression.
- Keep buyer enquiry, written scope, accepted order, verified payment, delivery, acceptance, and repeat purchase as separate stages. Revenue remains ₹0 until verified account/provider evidence confirms receipt.

## Files

- `sources.csv`: directories and primary-source discovery routes, with provider-stated coverage clearly labeled as claims of the source.
- `organizations.csv`: organization-level evidence and opportunity fit. A record may be a benchmark or not-contactable opportunity; it is not automatically a lead.
- `country-coverage.csv`: country-level evidence observed in this snapshot. A country is counted only when a dated source explicitly identifies it.
- `opportunities.csv`: individual procurement opportunities linked to an organization and source; multiple notices from one organization remain separate from the organization count.
- `product-opportunity-analysis.md`: buyer requirements translated into a product hypothesis, capability gaps and safe validation gates.
- `tests/test_market_research.py`: schema, source-link, ID, date, opportunity-link and country-count consistency checks; run with `python tests/test_market_research.py -v`.
- `reminders.csv`: internal, date-based research reminders. Current reminders do not authorize external contact or follow-up.

## Current coverage checkpoint (24 November 2026)

- **14 countries** have dated country-level evidence rows: Bangladesh, Yemen, Switzerland, India, South Africa, Bahrain, Kuwait, Lebanon, Nepal, Oman, Qatar, Saudi Arabia, Sri Lanka and United Arab Emirates. Nine of these additional rows are supported only by one expired ILO multi-destination notice; they have no local organization or contact record. This is a small, non-exhaustive sample of the 195-country ambition.
- **7 organization records** and **11 procurement opportunities** are recorded. The opportunity register also includes two separately tracked DeepRoot tenders and WMO's expired Jobsys 2.0 TMS RFP as a historical benchmark. The register contains **26 dated sources** and **8 internal reminders**.
- **0 organizations qualified** for the current SRI-SVC-001 offer; the new procurement signals are outside the documented 500-word Hindi/English pilot or have a missed eligibility gate.
- **0 first contacts, 0 follow-up messages, 0 delivered messages, 0 replies, 0 opt-outs/refusals, 0 buyer enquiries, 0 written scopes, 0 quotes, 0 accepted orders, 0 payment requests, 0 payment claims, 0 verified payment transactions, ₹0 verified payments, 0 work-in-progress items, 0 QA-passed jobs, 0 deliveries, 0 customer acceptances and 0 repeat purchases** in this market register.
- Published procurement contacts are counted as verified channels only; they are not counted as contact attempts and do not imply permission for cold sales outreach.
- Country-level segment and funnel counts are maintained in `country-coverage.csv`. First-contact and follow-up delivery status is recorded as delivered, unknown or bounced; each set reconciles to messages sent. Claimed and verified payments, work, QA, delivery and acceptance are separate counters.
- Internal reminder dates are maintained in `reminders.csv`. They are research-status checks only; no external follow-up is currently permitted.
- The AUDA-NEPAD RFB 007/AUDA/DOO/PRO/RFB/2027 in South Africa is added as OPP-010. The Philippines is added as a new country row through Philippine Ports Authority notice ASD-017-2026 (OPP-011), an expired 10 Nov annual-report publishing tender. Two third-party listings report a 36-month editing/design/layout/proofreading framework with a 18 Dec 2026 deadline; the linked official NEPAD PDF returned HTTP 403 on 24 Nov, so eligibility and detailed requirements remain unverified. No contact or bid was made. The Philippine Ports Authority official ITB confirms a PHP 2,288,000 budget, 180-day integrated publishing scope, 10-year similar-contract requirement and Filipino/reciprocal-country eligibility; it is historical only and not qualified for SRI-SVC-001. New country and opportunity sources in this update were checked on 24 November 2026; older source records retain their original access dates. See the source URLs and dates in `sources.csv` and `opportunities.csv`.

## Snapshot limitations

This is a staged research dataset, not a completed 195-country census. The global directories claim broad coverage (for example, 196 countries/territories or more than 190 countries), but their full underlying institution records have not been individually extracted, checked, deduplicated, or classified here. The current reviewable register contains 15 country rows and seven organization records only. Do not infer total institutions or contacts from directory coverage claims.

No emails or enquiries were sent during this research pass. No procurement bid, supplier registration, KYC, payment, or paid subscription was initiated.

## Next steps

1. Continue from these CSVs and deduplicate by official domain + normalized organization name; preserve the existing ORG/SRC/OPP identifiers.
2. Expand one region and one institution segment at a time, recording explicit country evidence and gaps.
3. Prefer current, open, clearly scoped procurement opportunities that match an existing SRI deliverable and capability.
4. Improve the product offer only when repeated evidence shows a specific buyer need.
5. Keep direct outreach for high-fit organizations with a lawful, published business channel and no tender communication restriction.


## Funnel metric definitions

- `official_contacts_verified` counts organizations with a source-verified official procurement/business route, not messages sent; a route may be tender-specific or expired and does not imply cold-contact permission.
- `first_contacts_sent` and `follow_up_messages_sent` count actual messages only. For each category, exactly one of delivered, delivery-status-unknown or bounced is recorded; replies and opt-outs/refusals are separate event counts.
- `qualified_for_current_sri_offer` counts organizations whose stated need and eligibility fit an existing, evidenced SRI offer. A procurement notice outside the pilot scope is not qualified.
- `payment_claims`/`payment_claimed_inr` are unverified claims. `verified_payment_transactions`/`verified_payments_inr` and `gross_revenue_inr` count only owner-reconciled actual credits. Net revenue is gross receipts minus recorded fees and refunds. No payment is counted from a screenshot, invoice, test order or message alone.
- Country-segment counts count organization records assigned to that country, not every destination named by a multi-country tender.
