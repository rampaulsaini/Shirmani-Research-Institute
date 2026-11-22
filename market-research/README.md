# SRI Global Market Research Register

**Snapshot:** 22 November 2026  
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
- `tests/test_market_research.py`: schema, source-link, ID, date, opportunity-link and country-count consistency checks; run with `python -m unittest tests/test_market_research.py -v`.

## Snapshot limitations

This is an initial research dataset, not a completed 195-country census. The global directories claim broad coverage (for example, 196 countries/territories or more than 190 countries), but their full underlying institution records have not been individually extracted, checked, deduplicated, or classified here. No persistent historical country register was present in the repository at the time this snapshot was created; this PR establishes the first reviewable seed dataset. Do not infer total institutions or contacts from directory coverage claims.

No emails or enquiries were sent during this research pass. No procurement bid, supplier registration, KYC, payment, or paid subscription was initiated.

## Next steps

1. Continue from these CSVs and deduplicate by official domain + normalized organization name.
2. Expand one region and one institution segment at a time, recording explicit country evidence and gaps.
3. Prefer current, open, clearly scoped procurement opportunities that match an existing SRI deliverable and capability.
4. Improve the product offer only when repeated evidence shows a specific buyer need.
5. Keep direct outreach for high-fit organizations with a lawful, published business channel and no tender communication restriction.
