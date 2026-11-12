"""signalam CLI — `signalam demo` runs the pipeline on synthetic posts."""
import json, os, sys
from .pipeline import run_pipeline
from .export import ephem_event, fhir_observation

def _demo_items():
    path = os.path.join(os.path.dirname(__file__), "..", "..", "demo", "synthetic_posts.jsonl")
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]

def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    if argv and argv[0] == "demo":
        items = _demo_items()
        result = run_pipeline(items)
        by_id = {i["id"]: i for i in result["triaged"]}
        print(f"Signal-Am demo: {len(items)} synthetic public posts in")
        print(f"  triaged items: {len(result['triaged'])} · dead-letter: {len(result['dead_letter'])}")
        for c in result["clusters"]:
            print(f"  cluster {c['id']}: {c['syndrome']} @ {c['woreda'] or 'unknown'} — {len(c['item_ids'])} posts merged")
        if result["clusters"]:
            c = dict(result["clusters"][0]); c["status"] = "verified"
            print("  sample ePHEM export:", json.dumps(ephem_event(c, by_id), ensure_ascii=False)[:220], "...")
            print("  sample FHIR resourceType:", fhir_observation(c)["resourceType"])
        return 0
    print("Usage: signalam demo")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
