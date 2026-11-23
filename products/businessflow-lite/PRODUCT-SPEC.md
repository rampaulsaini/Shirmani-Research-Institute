# SRI BusinessFlow Lite — Product 001

**Release status:** Prototype / packaging and validation in progress  
**Product type:** Downloadable, offline-first HTML utility  
**Initial market:** Indian micro and small businesses, solo service providers, tutors, small publishers  
**Proposed one-time pilot price:** ₹99–₹199 (hypothesis only; not a published offer or validated willingness to pay)  
**Sales status:** Not listed; no sales or customer validation claimed

## Buyer problem

A very small business may need one simple place on one device to note enquiries, quoted amounts, invoice due dates, overdue items and payments it has independently confirmed. A full cloud CRM/accounting subscription can be excessive for this narrow job.

## What this release actually does

- Runs locally in a modern browser; records remain in that browser's local storage.
- Creates enquiry and invoice-register records with customer/business label, non-sensitive contact reference, description, amount and due date.
- Shows open invoice count, outstanding total, overdue count and owner-confirmed paid total.
- Allows filtering, CSV export and JSON backup.
- Allows a record to be marked paid only after the owner confirms they independently checked actual credit in their external bank/payment account.
- Includes fictional demo records.

## Explicit limitations — disclose before purchase

- Not cloud-synced, encrypted, multi-user or multi-device.
- Not a payment gateway, bank feed, accounting ledger, GST-compliant invoice generator, tax calculator, inventory manager or statutory book of account.
- Does not send invoices, reminders, emails or WhatsApp messages.
- Payment confirmation is manual and owner-entered; it is not independently verified by the app.
- Browser data can be lost if the browser profile/device is cleared or damaged. The buyer must make and protect backups.
- Do not enter bank details, passwords, OTPs, government identity numbers, health information or confidential customer data.
- INR-only in this first release. No global currency/tax support is claimed.

## Release gate — do not sell until every item passes

1. Independent browser tests on current Android Chrome and desktop Chromium/Firefox.
2. Test create, edit/delete flows (edit is not currently implemented; either implement safely or clearly document the limitation).
3. Verify local-storage failure, malformed backup, duplicate IDs, empty backup and export handling.
4. Add a tested restore/import workflow before advertising JSON backup as recoverable backup.
5. Verify keyboard accessibility, screen-reader labels, responsive layout and reduced-motion behavior.
6. Check CSV spreadsheet-formula injection using adversarial customer and description strings.
7. Ensure demo data is clearly fictional and excluded from real totals unless deliberately added.
8. Prepare a plain-language user guide, version, changelog, licence, refund/support boundary and compatibility list.
9. Have at least three independent target users attempt the defined tasks; record failures and completion time. No testimonials without explicit permission.
10. Obtain owner approval for final price, licence, refund terms and any external seller/payment account.

## Buyer acceptance test

A first-time user should be able to:
- open the file without installing an app or creating an account;
- create an enquiry and an invoice-register entry;
- distinguish an enquiry from an issued invoice and from a manually owner-confirmed payment;
- identify overdue records;
- export a CSV and understand that it is not an accounting report;
- understand where data is stored and how to protect it.

## Distribution decision

- **Amazon India:** Do not list this as a downloadable software product. Amazon's India software policy prohibits digitally downloadable software and related access credentials; only eligible full retail physical software is permitted. See https://sellercentral.amazon.in/help/hub/reference/external/G200386270?locale=en_IN
- **Flipkart:** Do not assume digital-download eligibility. Its seller terms require legally saleable, correctly categorized items, required licences and stock for fulfilment. Obtain written platform clarification before listing.
- **Meesho:** No verified official permission for downloadable software found in this review. Do not list until seller support confirms the product format is allowed.
- **Direct digital storefront:** Instamojo's official help describes downloadable digital goods and post-payment delivery. Fees shown on its official pricing/help pages are not fully consistent; confirm the live fee schedule and KYC eligibility before any account connection or listing. No account is created by this project.
- **SRI website:** A direct enquiry/quote route may be used only after the product passes release gates and payment/delivery handling is approved.

## Evidence and claims policy

Do not claim market demand, customer savings, security certification, accounting compliance, sales, customer acceptance or superiority without measured evidence. Product readiness is not revenue. A successful test is not a customer purchase.
