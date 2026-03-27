from transformers import pipeline

from .helpers import LANGUAGE_MAP

translator_pipe = None


def get_translator(source_lang, target_lang):
    global translator_pipe

    src = LANGUAGE_MAP[source_lang]["code"]
    tgt = LANGUAGE_MAP[target_lang]["code"]

    model_name = f"Helsinki-NLP/opus-mt-{src}-{tgt}"

    print(f"Loading model: {model_name}")

    translator_pipe = pipeline("translation", model=model_name)


def translate_text(text: str, source_lang: str, target_lang: str) -> str:
    if source_lang == target_lang or not text.strip():
        return text

    try:
        get_translator(source_lang, target_lang)

        chunks = [text[i:i+500] for i in range(0, len(text), 500)]
        translated_chunks = []

        for chunk in chunks:
            result = translator_pipe(chunk, max_length=512)
            translated_chunks.append(result[0]['translation_text'])

        return " ".join(translated_chunks)

    except Exception as e:
        print(f"Translation error: {e}")
        return text