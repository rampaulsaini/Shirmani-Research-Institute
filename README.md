# Shirmani Research Institute

A minimal, self-contained public sales entry for Shirmani Research Institute, published with GitHub Pages from the `main` branch.

## Primary objective

Convert a real prospective customer into a clearly scoped, paid Hindi/English writing and research pilot. The public page separates enquiry, written scope, payment verification, and delivery. It does not claim sales or customer outcomes without evidence.

## Public page

- GitHub Pages: https://rampaulsaini.github.io/Shirmani-Research-Institute/
- Service: Hindi / English Writing & Research
- One-time pilot: ₹999, available through 30 November 2026
- Scope: one deliverable up to 500 words, one consolidated revision
- Proposed delivery: 2 working days after written scope, required material, and payment confirmation

## How enquiries work

The page uses direct WhatsApp and email links. It is a static GitHub Pages site: it does not store enquiries in a database, run a backend, or claim that a message was received until the owner sees it.

Payment instructions are shared only after the buyer and SRI agree on the exact scope, price, and deadline in writing. The existing Razorpay payment route is https://rzp.io/rzp/UhC1i8c and is shared only after written agreement; it is not an unconditional order or payment confirmation. A payment is verified only after actual account credit is checked; a screenshot alone is not proof of credit.

## Operating boundaries

- This repository is the only authorized source and target for this work.
- Keep the site small, fast, accessible, mobile-friendly, and dependency-free.
- Do not add analytics, trackers, external frameworks, or a backend unless a demonstrated first-payment blocker requires it and the owner approves the required service.
- Never invent testimonials, customer intent, orders, payments, delivery evidence, credentials, or payment details.
- No subscriptions, hidden renewals, pressure tactics, or unlimited free work.
- Do not claim income until a genuine payment is verified.

## Validation and deployment

A dependency-free Python smoke test checks the public offer, enquiry brief, scope, price consistency, and safe external links. GitHub Actions runs this check on pull requests and pushes to `main`.

GitHub Pages must be configured by the repository owner to publish the root of `main`. A successful Actions run is deployment evidence, not sales or payment evidence.

## Self-service enquiry brief

- The public offer links to `brief.html`, a small browser-only enquiry brief builder.
- It validates required fields and prepares a WhatsApp message or email draft; it does not submit automatically, store form data, or create an order.
- Visitors should not enter confidential or sensitive information. The visitor reviews and chooses whether to open an external messaging service.
- This feature is not a checkout, CRM, enquiry database, payment confirmation, or delivery automation.
