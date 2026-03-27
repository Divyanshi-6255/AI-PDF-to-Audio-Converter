import streamlit as st
from utils.extractor import extract_text_from_pdf
from utils.preprocessor import clean_text
from utils.translator import translate_text
from utils.tts import text_to_speech
from utils.helpers import detect_language, LANGUAGE_MAP

# Page config
st.set_page_config(page_title="PDF to Audio", layout="centered")

# Title
st.title("📄 AI PDF to Audio Converter")
st.markdown("### Extract → Translate → Speak 🎧")

# Sidebar
st.sidebar.header("⚙️ Options")
target_lang = st.sidebar.selectbox(
    "Select Target Language",
    options=list(LANGUAGE_MAP.keys()),
    index=0
)

# File uploader
uploaded_file = st.file_uploader("📤 Upload your PDF file", type="pdf")

if uploaded_file:
    # Step 1: Extract text
    with st.spinner("📄 Extracting text from PDF..."):
        raw_text = extract_text_from_pdf(uploaded_file)
        cleaned_text = clean_text(raw_text)

    if not cleaned_text.strip():
        st.error("❌ No text found in PDF. Try another file.")
        st.stop()

    # Step 2: Detect language
    source_lang = detect_language(cleaned_text)

    st.success(f"✅ Text extracted! Detected Language: **{source_lang}**")

    # Layout
    col1, col2 = st.columns(2)

    # Original text
    with col1:
        st.subheader("📘 Original Text")
        st.text_area(
            "Original Text Area",
            cleaned_text,
            height=300,
            key="original_text"
        )

    # Translated text
    with col2:
        st.subheader(f"🌍 Translated Text ({target_lang})")

        with st.spinner("🔄 Translating... Please wait"):
            translated_text = translate_text(
                cleaned_text, source_lang, target_lang
            )

        st.text_area(
            "Translated Text Area",
            translated_text,
            height=300,
            key="translated_text"
        )

    st.divider()

    # Audio generation
    if st.button("🎤 Generate Audio", type="primary"):

        if translated_text.strip():

            with st.spinner("🔊 Converting to speech..."):
                audio_bytes = text_to_speech(translated_text, target_lang)

            st.audio(audio_bytes, format="audio/mp3")

            st.download_button(
                label="⬇️ Download Audio",
                data=audio_bytes,
                file_name=f"audio_{target_lang}.mp3",
                mime="audio/mp3"
            )

            st.success("✅ Audio generated successfully!")

        else:
            st.error("❌ No translated text available.")