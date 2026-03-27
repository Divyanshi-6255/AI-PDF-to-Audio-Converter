from gtts import gTTS   
from io import BytesIO
from .helpers import LANGUAGE_MAP

def text_to_speech(text: str, target_lang: str) -> BytesIO:
    """Convert text to audio"""
    lang_code = LANGUAGE_MAP.get(target_lang, LANGUAGE_MAP["English"])["gtts"]
    
    tts = gTTS(text=text, lang=lang_code, slow=False)
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes