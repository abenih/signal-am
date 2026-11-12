# Interoperability

| Target | What Signal-Am produces | Status |
|---|---|---|
| ePHEM / EIOS | Structured event JSON (syndrome, location, dates, source links, verification state) | v0.1 file export |
| DHIS2 | Event payload for the Web API (aggregate + Tracker) | M3 — test instance |
| HL7 FHIR R4 | `Observation`-style event resource | v0.1 basic resource + validation test |

Alignment references: Africa CDC Health Information Exchange Guidelines and Standards; OpenHIE architecture patterns.
Interoperability is **tested**, not asserted: see `tests/test_export_*.py`.
