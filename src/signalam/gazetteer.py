"""Load the seed gazetteer and match place names to admin units."""
import os, yaml

def _default_path():
    return os.path.join(os.path.dirname(__file__), "..", "..", "gazetteer", "ethiopia-admin.yaml")

def load_gazetteer(path=None):
    with open(path or _default_path(), encoding="utf-8") as f:
        return yaml.safe_load(f)

def match_place(text, gazetteer):
    """Return the first matching place dict or None."""
    for place in gazetteer.get("places", []):
        for key in ("name", "am"):
            name = place.get(key)
            if name and name.lower() in text.lower():
                return place
    return None
