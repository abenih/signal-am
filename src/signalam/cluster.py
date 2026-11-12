"""Cluster triaged items: same syndrome + same woreda + 72h window."""
from datetime import datetime, timedelta

WINDOW = timedelta(hours=72)

def cluster_items(items):
    """items: dicts with keys id, syndrome, woreda, published_at (ISO str), text."""
    clusters, index = [], {}
    for item in sorted(items, key=lambda x: x["published_at"]):
        ts = datetime.fromisoformat(item["published_at"])
        key = (item["syndrome"], item.get("woreda") or "unknown")
        placed = False
        for c in index.get(key, []):
            if ts - c["last_seen"] <= WINDOW:
                c["item_ids"].append(item["id"]); c["last_seen"] = ts; placed = True; break
        if not placed:
            c = {"id": f"CL-{len(clusters)+1:03d}", "syndrome": item["syndrome"],
                 "woreda": item.get("woreda"), "region": item.get("region"),
                 "first_seen": ts, "last_seen": ts, "item_ids": [item["id"]], "status": "new"}
            clusters.append(c); index.setdefault(key, []).append(c)
    return clusters
