from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0

# Language mapping (VERY IMPORTANT)

LANGUAGE_MAP = {
    "English": {"code": "en", "gtts": "en"},
    "Hindi": {"code": "hi", "gtts": "hi"},
    "French": {"code": "fr", "gtts": "fr"},
    "Spanish": {"code": "es", "gtts": "es"},
    "German": {"code": "de", "gtts": "de"},
}

def detect_language(text: str) -> str:
    """Detect language of text"""
    try:
        lang = detect(text[:300])
        mapping = {v["code"]: k for k, v in LANGUAGE_MAP.items()}
        return mapping.get(lang, "English")
    except:
        return "English"