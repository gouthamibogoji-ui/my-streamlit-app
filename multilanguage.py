import streamlit as st
from gtts import gTTS
from deep_translator import GoogleTranslator

# Page Title
st.title("🌍 Multilanguage Translator + Text to Speech Converter")


# Supported language codes
languages = {
    "en": "en",
    "hi": "hi",
    "kn": "kn",
    "te": "te",
    "ta": "ta",
    "fr": "fr",
    "pa":"pa"
}
    
    
# -----------------------------
# ⭐ SIDEBAR SECTION
# -----------------------------
st.sidebar.header("🌐 Language Section")

src_lang = st.sidebar.selectbox("📝 Select Source Language:", list(languages.keys()))
dest_lang = st.sidebar.selectbox("🎯 Select Destination Language:", list(languages.keys()))

translator = GoogleTranslator(source='auto', target=dest_lang)


translate_btn = st.sidebar.button("🔄 Translate & Convert")

# -----------------------------
# ⭐ MAIN AREA
# -----------------------------
text = st.text_area("✍️ Enter text to translate and convert:")

if translate_btn:
    if text.strip() == "":
        st.error("Please enter some text!")
    else:
        # Translate text
        translated = translator.translate(
            text, 
            src=languages[src_lang], 
            dest=languages[dest_lang]
        )

        st.success("✔ Translation Successful!")

        # Display translated text
        st.subheader("🔤 Translated Text:")
        st.write(translated)

        # Convert to speech
        tts = gTTS(text=translated, lang=languages[dest_lang])
        tts.save("translated_audio.wav")

        # Play audio
        st.subheader("🔊 Listen to Audio:")
        st.audio("translated_audio.wav")

        # Download button
        st.download_button(
            label="⬇ Download Audio",
            data=open("translated_audio.wav", "rb"),
            file_name="translated_audio.wav",
            mime="audio/mpeg"
        )
