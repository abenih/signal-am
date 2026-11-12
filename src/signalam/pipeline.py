"""End-to-end pipeline on in-memory items (v0.1)."""
from .normalise import normalise_text, detect_language
from .gazetteer import load_gazetteer, match_place
from .lexicon import load_lexicons, score_text
from .cluster import cluster_items

def run_pipeline(raw_items, lexicons=None, gazetteer=None):
    lexicons = lexicons or load_lexicons()
    gazetteer = gazetteer or load_gazetteer()
    triaged, dead_letter = [], []
    for raw in raw_items:
        try:
            text = normalise_text(raw["text"])
            place = match_place(text, gazetteer) or match_place(raw["text"], gazetteer)
            scores = score_text(text, lexicons)
            if not scores:
                continue  # below threshold: kept out of the queue by design
            for syndrome in scores:
                triaged.append({
                    "id": raw["id"], "syndrome": syndrome, "text": text,
                    "source": raw["source"], "url": raw.get("url", ""),
                    "published_at": raw["published_at"],
                    "language": detect_language(text),
                    "region": place["region"] if place else None,
                    "woreda": place["woreda"] if place else None,
                    "score": scores[syndrome],
                })
        except Exception as exc:  # never silently drop
            dead_letter.append({"id": raw.get("id"), "reason": str(exc)})
    return {"triaged": triaged, "clusters": cluster_items(triaged), "dead_letter": dead_letter}
