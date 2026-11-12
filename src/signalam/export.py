"""Exports for verified clusters: ePHEM/EIOS-style JSON + FHIR R4 resource."""
import json, hashlib

def ephem_event(cluster, items_by_id=None):
    sources = []
    for iid in cluster["item_ids"]:
        it = (items_by_id or {}).get(iid)
        if it is None:
            continue
        sources.append({"source": it["source"], "url": it.get("url", ""), "published_at": it["published_at"]})
    return {
        "event_type": "unverified_signal",  # EPHI verifies in their own system
        "syndrome": cluster["syndrome"],
        "location": {"region": cluster.get("region"), "woreda": cluster.get("woreda")},
        "first_seen": cluster["first_seen"].isoformat(), "last_seen": cluster["last_seen"].isoformat(),
        "item_count": len(cluster["item_ids"]), "sources": sources,
        "verification": {"status": cluster.get("status", "new")},
    }

def fhir_observation(cluster):
    payload = ephem_event(cluster)
    digest = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()[:16]
    return {
        "resourceType": "Observation", "id": f"signalam-{digest}",
        "status": "preliminary",
        "code": {"text": f"Epidemic signal: {cluster['syndrome']}"},
        "effectiveDateTime": cluster["first_seen"].isoformat(),
        "note": [{"text": "Unverified public-source signal from Signal-Am. Verify in ePHEM before action."}],
        "extension": [{"url": "https://signalam.example/fhir/woreda", "valueString": str(cluster.get("woreda"))}],
    }
