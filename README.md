# Signal-Am

**Ethiopian-language epidemic-intelligence triage — public signals in, verified structured events out, into the systems EPHI already runs.**

Signal-Am screens public sources in Amharic and Afaan Oromo (Tigrinya, Somali and English supported), scores them against an auditable syndrome lexicon, de-duplicates them into event clusters located to region/zone/woreda, and puts them in front of a human verifier. Only a verified cluster can be exported — as an ePHEM/EIOS-compatible file, a DHIS2 event, or an HL7 FHIR R4 resource.

It is **not** a surveillance platform and replaces nothing: DHIS2, ePHEM, EIOS and eCHIS remain the systems of record. Signal-Am shortens the two slowest steps before them — noticing a public signal in an Ethiopian language, and turning it into structured data without re-typing.

## Why

- Aligned with the Africa CDC Digital Transformation Strategy 2023–2030 (IDSR flagship, digital public goods, home-grown innovation) and designed for the Africa CDC Data & Innovation Sandbox.
- Built for Ethiopia's reality: offline-capable verifier queue, runs fully on in-country infrastructure, Amharic UI strings.
- Privacy by architecture: **no patient data, ever** — public and aggregate signals only, in line with Ethiopia's Personal Data Protection Proclamation 1321/2024 and the federated model of the African Continental Health Data Governance Framework.

## Status

M0 — repo skeleton, lexicon seed, synthetic demo. The pipeline runs end-to-end on synthetic data (`signalam demo`). Lexicon terms are a **seed** pending validation with EPHI/APHI and native speakers. See `benchmarks/2025-replay.md` for the evaluation plan.

## Quick start

```bash
pip install -e .
signalam demo
pytest
```

## Pipeline

`CAPTURE → NORMALISE → TRIAGE → CLUSTER → VERIFY → EXPORT` — every item carries an audited state; failures go to a dead-letter list with a reason, never silently dropped. See `docs/architecture.md`.

## የአማርኛ ማጠቃለያ

ሲግናል-አም በይፋ የሚወጡ የአማርኛ እና የኦሮምኛ ምንጮችን በመመርመር የወረርሽኝ ምልክቶችን ፈልጎ፣ ድግግሞሽን አስወግዶ፣ በሰው እንዲረጋገጡ ያቀርባል። የተረጋገጠ ምልክት ብቻ ወደ ePHEM፣ DHIS2 ወይም FHIR መልክ ይላካል። የታካሚ መረጃ በጭራሽ አይሰበሰብም።

*(Amharic summary — to be reviewed by a native speaker before any external release.)*

## Licence

Apache-2.0
