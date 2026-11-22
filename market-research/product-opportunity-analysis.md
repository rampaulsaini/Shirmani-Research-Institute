# Product opportunity analysis: language-data quality operations

**Research snapshot:** 22 November 2026  
**Evidence base:** Three open LEHS/Wadhwani AI procurement notices reviewed in detail. These are buyer requirements, not SRI orders or evidence that SRI is qualified.

## What buyers demonstrably require

1. **Word-level timestamped transcription:** Hindi student reading audio; every heard word/letter timestamped and transcribed verbatim, including disfluencies or pronunciation as heard. Blind annotation without reference text. Mandatory onboarding and protocol alignment.
2. **Human-reviewed multilingual health language data:** ASR annotation, transcription, Indian-language-to-English query translation, English-to-Indian-language output translation; initial Hindi, Marathi and Odia. Native-speaker linguists, healthcare terminology knowledge, independent second-person review, senior adjudication, multi-pass QA and rework.
3. **Purpose-built workflow, not spreadsheets:** The multilingual RFP explicitly rejects spreadsheet-based work and requires a purpose-built tool operating in a secure environment provided or approved by the buyer.
4. **Data collection quality:** Clinical speech datasets must represent Hindi/English, varied accents/dialects, gender, age, region, qualification, fluency and urban/rural/tribal settings.

## Product hypothesis to test — not yet a built or market-ready product

A lightweight **Language Data QA Workbench** could help small qualified teams manage:
- audio/job intake with explicit consent, data classification, retention and deletion controls;
- protocol versioning and task instructions;
- word/segment timestamps and verbatim transcription;
- separate annotator and reviewer roles;
- disagreement queues, adjudication and traceable corrections;
- batch-level quality metrics, sampling and rejection/rework reports;
- export to buyer-defined JSON/CSV schemas;
- role-based access, audit events and buyer-approved deployment boundaries.

## Critical gaps before offering it

- No validated SRI annotation team or native-speaker reviewer roster.
- No demonstrated health-domain linguistic competence.
- No buyer-approved secure environment or audited data-protection controls.
- No purpose-built annotation tool, protocol conformance demo or benchmark results yet.
- No legal/vendor eligibility package or relevant institutional completion references evidenced.
- No independent accuracy benchmark on a lawful, non-sensitive sample.

## Safe validation sequence

1. Build a synthetic/public-domain demo only; never use real child recordings, patient audio or confidential data without lawful authorization and buyer-approved controls.
2. Test timestamp precision, verbatim fidelity, diarization where required, Hindi/English code-switching, reviewer disagreement and JSON schema conformance.
3. Run blinded quality evaluation with qualified human reviewers; publish measured error rates and limitations, not unsupported accuracy claims.
4. Interview prospective buyers through published, permitted channels only after the demo and capability evidence exist.
5. Offer a small paid pilot with explicit scope, data-processing terms, acceptance criteria and deletion schedule before scaling.

## Commercial conclusion

The notices show a repeated institutional purchasing category around Indian-language speech data and quality assurance. They do **not** show that SRI can currently deliver these contracts. Do not bid on the reviewed LEHS notices or contact the procurement team as a cold sales lead. First-payment work remains the existing small Hindi/English writing and research pilot; product exploration must not distract from that immediate path.

## Existing products and competitive baseline

A first-pass comparison shows that the basic annotation interface is already a mature category. SRI should not claim novelty or superiority merely by building an audio player with timestamps.

| Product | Evidence-backed strengths | Important limitation or validation point |
|---|---|---|
| Label Studio Community / Enterprise | Community supports audio, text and multimodal tasks, data management and exports; Enterprise adds mature role workflows, review queues, quality controls, activity logs and advanced security/on-prem options. | Several buyer-critical controls are edition-dependent. Confirm license, actual role/QA features and deployment model before adopting. |
| Audino v2 | Open-source audio annotation; project describes transcription, labeling, VAD, diarization, speaker identification, multi-language support and exports. | Maintainers describe v2 as actively under development; check release activity, issue backlog, security posture and exact workflow maturity. |
| ELAN | Established linguistic audio/video annotation with time-aligned multi-tier annotations and structured EAF/XML plus multiple exports. | Strong research annotation tool, but not automatically an institutional multi-vendor procurement workflow with independent review, secure tenant controls or healthcare QA. |
| Praat | Mature phonetic analysis and TextGrid interval/point annotation; its manual describes optional Whisper.cpp transcription and word-level alignment. | Model-assisted transcription/alignment is not proof of verbatim accuracy; human protocol-driven verification remains essential. |

## Where a differentiated SRI product might earn its place

Only pursue a product after comparing an actual prototype against the tools above. Potential differentiators to test—not claims of current capability—are:
- Hindi/Indic-specific verbatim protocols, dialect and code-switching guidance, and per-buyer configurable schemas.
- Blind annotation mode where reference text is hidden from annotators.
- Two independent human passes, disagreement visualization, senior adjudication and immutable correction history.
- Buyer-defined JSON export validation and batch acceptance/rework reports.
- A small, auditable workflow that can run inside a buyer-approved environment, with explicit data retention/deletion controls.
- Low training burden and transparent per-hour/per-minute/per-task cost reporting.

**Build-vs-adopt rule:** first test whether ELAN/Praat/Audino/Label Studio can satisfy the workflow through configuration or integration. Build only the missing layer. Before adoption, inspect the exact license, maintainers, dependency tree, security advisories, data flows, authentication, export fidelity, accessibility, offline/on-prem feasibility and total operating cost. No new dependency, paid plan or production data use is authorized by this research.

## Minimum comparative benchmark before any “better than” claim

Use only synthetic or public-domain sample audio until legal authorization and buyer-approved safeguards exist. Measure:
- word timestamp error (milliseconds) and proportion within the buyer's tolerance;
- verbatim word error rate, including fillers, repetitions, partial words and mispronunciations;
- Hindi/English code-switch and dialect handling;
- inter-annotator agreement and adjudication rate;
- reviewer time per audio minute and rework percentage;
- export schema validity and reproducibility;
- task completion time on a low-end Android device and desktop;
- security and privacy controls demonstrated, not merely described.

A future product may be considered better only if it beats a named alternative on buyer-relevant measured outcomes while meeting the same data-security and protocol requirements.
