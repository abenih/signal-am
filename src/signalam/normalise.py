"""Fidel-script normalisation + gazetteer matching."""
import re, unicodedata

# Variant Fidel characters unified to one canonical form (seed map).
FIDEL_VARIANTS = {
    "ሐ": "ሀ", "ኀ": "ሀ", "ኃ": "ሀ", "ሓ": "ሀ", "ኻ": "ሀ",
    "ሠ": "ሰ", "ሠ": "ሰ",
    "ኣ": "አ", "ዐ": "አ", "ዓ": "አ", "ኢ": "ኢ",
    "ጸ": "ፀ", "ፀ": "ፀ",
    "ቐ": "ቀ",
}
_TRANS = str.maketrans(FIDEL_VARIANTS)

def normalise_text(text: str) -> str:
    text = unicodedata.normalize("NFC", text or "")
    text = text.translate(_TRANS)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def detect_language(text: str) -> str:
    """Very small heuristic v1: script + marker words."""
    if re.search(r"[\u1200-\u137F]", text):
        return "am"  # Ethiopic script (am/ti share script; refined in v2)
    lower = text.lower()
    if any(m in lower for m in (" dhukkuba ", " fayyaa ", " godina ", " aanaa ")):
        return "om"
    return "en"
