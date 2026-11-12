import json, os
from signalam.pipeline import run_pipeline
from signalam.export import ephem_event, fhir_observation


def test_exports_are_structured_and_labelled_unverified():
    path = os.path.join(os.path.dirname(__file__), "..", "demo", "synthetic_posts.jsonl")
    with open(path, encoding="utf-8") as f:
        items = [json.loads(line) for line in f if line.strip()]
    result = run_pipeline(items)
    assert result["clusters"]
    by_id = {i["id"]: i for i in result["triaged"]}
    event = ephem_event(result["clusters"][0], by_id)
    assert event["event_type"] == "unverified_signal"
    assert event["location"]["region"]
    fhir = fhir_observation(result["clusters"][0])
    assert fhir["resourceType"] == "Observation" and fhir["status"] == "preliminary"
