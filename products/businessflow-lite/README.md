# SRI BusinessFlow Lite

An offline-first enquiry and invoice follow-up register for a very small business.

**Current status: not yet released for sale.** This folder documents Product 001 while the existing application is being tested and packaged. The current app source is `businessflow-lab.html` on the parent branch.

## Intended customer

A solo service provider, tutor, small publisher or microbusiness that wants a simple single-device list of enquiries, invoice amounts, due dates and manually confirmed payments without adopting a cloud CRM.

## Buyer-facing description (draft; publish only after release gates pass)

Keep track of customer enquiries and invoice follow-ups in one simple browser tool. Add a business/customer label, work description, amount and due date. Review outstanding and overdue items, search records, and export a CSV or JSON copy.

The tool runs in your browser on one device. It does not connect to your bank, send invoices or reminders, collect payments, calculate GST or replace accounting software. Payment status is a manual note you should set only after checking actual credit in your own account.

## Quick-start flow to validate

1. Download the single HTML file from the approved SRI delivery location.
2. Open it in a supported modern browser.
3. Add one fictional test enquiry.
4. Add one fictional invoice-register record.
5. Check the summary and overdue status.
6. Export CSV and JSON; store backups securely.
7. Close and reopen the file in the same browser profile to confirm local records remain.
8. Remove fictional demo records before entering any real business information.

## Support boundary

The proposed first release is self-service. No remote access, account setup, bookkeeping, tax advice, data migration or unlimited customization is included. A buyer should never send passwords, OTPs, bank credentials, government identity numbers or confidential customer records to SRI.

## Release checklist

- [ ] Android Chrome smoke test
- [ ] Desktop Chromium smoke test
- [ ] Desktop Firefox smoke test
- [ ] Storage disabled/quota failure behavior
- [ ] Malformed JSON and duplicate-ID behavior
- [ ] Export injection tests
- [ ] Backup restore/import implemented and tested, or backup described only as export
- [ ] Keyboard and screen-reader pass
- [ ] Three target-user usability sessions
- [ ] Final licence, price, refund and support terms approved
- [ ] Approved delivery and payment process verified

## Product versioning

Version 0.1 — prototype packaging record. No production release, listing, order or revenue is claimed.
