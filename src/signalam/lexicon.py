"""Syndrome lexicon loading + transparent scoring."""
import os, glob, yaml

def load_lexicons(directory=None):
    directory = directory or os.path.join(os.path.dirname(__file__), "..", "..", "lexicon")
    lexicons = []
    for path in sorted(glob.glob(os.path.join(directory, "*.yaml"))):
        with open(path, encoding="utf-8") as f:
            lexicons.append(yaml.safe_load(f))
    return lexicons

def score_text(text, lexicons):
    """Return {syndrome: {score, fired:[terms]}} for syndromes above threshold."""
    lower = text.lower()
    results = {}
    for lex in lexicons:
        score, fired = 0, []
        for term in lex.get("terms", []):
            t = term["term"]
            if t.lower() in lower:
                score += int(term.get("weight", 1)); fired.append(t)
        if score >= int(lex.get("threshold", 3)):
            results[lex["syndrome"]] = {"score": score, "fired": fired, "label": lex.get("label_en", lex["syndrome"])}
    return results
