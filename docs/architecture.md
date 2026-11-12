# Architecture

## States (audited ETL, no silent drops)

`captured → normalised → triaged → clustered → verified | rejected → exported`
Any stage can instead send an item to `dead_letter` **with a reason**.

## Modules

- `collectors/` — public-source collectors (RSS first; public Telegram/web next). Each item: raw text, source name, URL, published/captured timestamps, collector id.
- `normalise/` — language ID, Fidel-script normalisation (variant characters unified), gazetteer matching to region/zone/woreda.
- `triage/` — syndrome lexicon scoring. Transparent: every score lists the terms that fired. No black-box ML in v1.
- `cluster/` — same syndrome + same woreda + 72h window + text similarity → one queue row.
- `verify/` — human queue states and the append-only audit log. A human decision is the only exit from the tool.
- `export/` — ePHEM/EIOS-compatible JSON, DHIS2 event payload, FHIR R4 resource.
- `store.py` — SQLite store (v1). Postgres is a documented later step, not built until a pilot demands it.

## Design rules

Public sources only · no patient data · offline-first verifier queue · runs fully in-country · replaces no existing system.
