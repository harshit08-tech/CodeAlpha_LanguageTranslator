import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Translator",page_icon="icon.png")


st.markdown("""
<style>
/* Full app background */
[data-testid="stAppViewContainer"] {
    background-color: #F0F8FF;
}

/* Main content area */
[data-testid="stMain"] {
    background-color:#F0F8FF;
}

/* Title */
.title {
    text-align: center;
    color: #1E3A8A;
    font-size: 40px;
    font-weight: bold;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #6B7280;
    margin-bottom: 20px;
}

/* Button */
.stButton>button {
    background-color: #4169E1;
    color: white;
    font-size: 16px;
    border-radius: 10px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🌐 Language Translation Tool</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Translate text instantly between languages</div>', unsafe_allow_html=True)

st.image("icon.png", width=120)

#input text
text= st.text_area("enter text to translate")


#Language options
languages = {
    "English": "en",
    "Hindi": "hi",
    "Gujarati": "gu",
    "French": "fr",
    "Spanish": "es"

}

#Dropdowns
source_lang = st.selectbox("Select Source Language", list(languages.keys()))
target_lang = st.selectbox("Select Target Language", list(languages.keys()))

def is_valid_text(text):
    return any(char.isalpha() for char in text)

#Translate button

if st.button("Translate"):
    if not text:
        st.warning("please enter some text")
    elif not is_valid_text(text):
        st.warning("please enter valid text and not only nubers")
    elif source_lang == target_lang:
        st.warning("Source and Target languages should be different")
    else:
        translated= GoogleTranslator(
            source= languages[source_lang],
            target= languages[target_lang]
        ).translate(text)

        st.success("translated Text:")
        st.write(translated)
