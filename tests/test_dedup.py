import json, os
from signalam.pipeline import run_pipeline


def _items():
    path = os.path.join(os.path.dirname(__file__), "..", "demo", "synthetic_posts.jsonl")
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def test_same_event_posts_merge_into_one_cluster():
    result = run_pipeline(_items())
    jinka = [c for c in result["clusters"] if c["woreda"] == "Jinka"]
    assert jinka, "expected a Jinka cluster"
    assert max(len(c["item_ids"]) for c in jinka) >= 2


def test_weather_post_is_not_triaged():
    result = run_pipeline(_items())
    assert all(i["id"] != "S08" for i in result["triaged"])
