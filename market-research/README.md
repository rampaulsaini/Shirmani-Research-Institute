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

- **17 country rows** have dated country-level evidence: Bangladesh, Yemen, Switzerland, India, South Africa, Philippines, Rwanda, Bahrain, Kuwait, Lebanon, Nepal, Oman, Qatar, Saudi Arabia, Sri Lanka and United Arab Emirates. Eight countries have at least one organization record; nine country-only rows are supported only by one expired ILO multi-destination notice and have no local organization or contact record. This is a small, non-exhaustive sample of the 195-country ambition.
- **Canada (North America) market signal:** official CanadaBuys award notices published 18 Nov 2026 show ISED's English↔French translation/editing/proofreading standing-offer contracts. The Stream A and Stream B award notices each state CAD 2,057,142.86; awards were made 1 Sep 2026 for a 24-month period through 31 Aug 2028. These are already-awarded incumbent contracts, not open demand, and SRI is not qualified because French capability and federal procurement eligibility are not evidenced.
- **12 organization records** and **14 procurement opportunities** are recorded. The opportunity register includes two separately tracked DeepRoot tenders, WMO's expired Jobsys 2.0 TMS RFP as a historical benchmark, and a Rwanda EOI reported by a third-party listing but not verified against a primary GIZ tender document. The register contains **35 dated sources** and **9 internal reminders**.
- **0 organizations qualified** for the current SRI-SVC-001 offer; the new procurement signals are outside the documented 500-word Hindi/English pilot or have a missed eligibility gate.
- **3 first-contact emails** are recorded against source-verified organizations in India (Ayaan Humanity Foundation, Broadview Publications and Sankalp Learning Hub); **0 confirmed delivered, 3 delivery-status-unknown and 0 replies**. All three are unqualified hypotheses/hiring signals, not buyer enquiries. The wider Gmail audit found **16 service-offer emails to 16 unique recipient addresses** sent 21–23 Nov; 3 are matched to source-verified organization records and 13 remain unmatched, so they are not counted in country-level organization totals. Across those 16 messages, there was 1 permanent 550 bounce, 2 temporary 4.4.1 delays and 13 with no provider delivery confirmation; no replies were received to those 16. A separate job application was excluded. Earlier email history is not fully reconciled. **0 buyer enquiries, 0 written scopes, 0 quotes, 0 accepted orders, 0 payment requests, 0 payment claims, 0 verified payment transactions, ₹0 verified payments, 0 work-in-progress items, 0 QA-passed jobs, 0 deliveries, 0 customer acceptances and 0 repeat purchases** are recorded in this market register.
- Published procurement contacts are counted as verified channels only; they are not counted as contact attempts and do not imply permission for cold sales outreach.
- Country-level segment and funnel counts are maintained in `country-coverage.csv`. First-contact and follow-up delivery status is recorded as delivered, unknown or bounced; each set reconciles to messages sent. Claimed and verified payments, work, QA, delivery and acceptance are separate counters.
- Internal reminder dates are maintained in `reminders.csv`. They are research-status checks only; no external follow-up is currently permitted.
- The AUDA-NEPAD RFB 007/AUDA/DOO/PRO/RFB/2027 in South Africa is added as OPP-010. The Philippines is added as a new country row through Philippine Ports Authority notice ASD-017-2026 (OPP-011), an expired 10 Nov annual-report publishing tender. Two third-party listings report a 36-month editing/design/layout/proofreading framework with a 18 Dec 2026 deadline; the linked official NEPAD PDF returned HTTP 403 on 24 Nov, so eligibility and detailed requirements remain unverified. No contact or bid was made. The Philippine Ports Authority official ITB confirms a PHP 2,288,000 budget, 180-day integrated publishing scope, 10-year similar-contract requirement and Filipino/reciprocal-country eligibility; it is historical only and not qualified for SRI-SVC-001. New country and opportunity sources in this update were checked on 24 November 2026; older source records retain their original access dates. See the source URLs and dates in `sources.csv` and `opportunities.csv`.

## Income-first consistency blocker

As checked on 24 November 2026, the authorized repository's `main`-branch `README.md` and `index.html` state the introductory SRI-SVC-001 pilot at ₹499 through 30 November. The live [Take App product page](https://take.app/httpsgithubcomrampaulsainishirmaniresearchinstituteshirmaniresearchinstitute/p/cmwu5mym0005408jp00vu7djn) lists ₹999, and the separate read-only showroom repository's [first-paid-pilot-offer.html](https://github.com/rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-/blob/main/first-paid-pilot-offer.html), [services-writing-research.html](https://github.com/rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-/blob/main/services-writing-research.html), [writing-research-enquiry.html](https://github.com/rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-/blob/main/writing-research-enquiry.html), [supreme-clean-showroom.html](https://github.com/rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-/blob/main/supreme-clean-showroom.html) and [income-action-center.html](https://github.com/rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-/blob/main/income-action-center.html) show ₹999 as the proposed editing/pilot price. ₹999 may be the standard rate, but the ₹499 introductory offer is not clearly reconciled across the customer-facing channels. No external listing, price, payment setting or public page was changed in this PR. Align or explicitly label the standard-versus-introductory price before sending further outreach.

## Authorized repository readiness (checked 24 Nov 2026)

The `main` branch contains four tracked files: `LICENSE`, `README.md`, `index.html` and `brief.html`. It is a static sales entry, not a complete digital-products backend. `brief.html` is a browser-only brief builder that prepares a WhatsApp/email draft; it does not store or submit an enquiry. No package manifest, product catalogue, server, CRM, payment integration, reconciliation workflow, automated delivery or acceptance ledger is present on `main`. The repository uses an MIT license. The current PR changes only the market-research register and its validation evidence; it does not add runtime product functionality.

## Snapshot limitations

This is a staged research dataset, not a completed 195-country census. The global directories claim broad coverage (for example, 196 countries/territories or more than 190 countries), but their full underlying institution records have not been individually extracted, checked, deduplicated, or classified here. The current reviewable register contains 17 country rows and 12 organization records only. Do not infer total institutions or contacts from directory coverage claims.

No new emails or enquiries were sent during this research pass. The 16 emails above were sent before this run; the originating automation/run for each is not available in the mailbox metadata, so per-run contact-cap compliance cannot be attributed. The permanent CIIT Classes 550 bounce is suppressed; Broadview and JKSSB remain temporary delivery delays and must not be resent while unresolved. TravelView explicitly declined the earlier pilot on 9 Nov; no further contact is permitted unless they reinitiate. Replies from Translayte, Lionbridge and Multisolution Agency were vendor-side or closed/mismatched opportunities, not SRI buyer enquiries. No procurement bid, supplier registration, KYC, payment, or paid subscription was initiated.

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
