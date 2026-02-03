import streamlit as st

# Igbo Dictionary
igbo_dict = {
    "come": "bịa",
    "stand": "guzọ",
    "sit": "ọdụ",
    "god": "Chukwu",
    "morning": "ụtụtụ",
    "night": "abalị",
    "we/us": "anyị",
    "water": "mmiri",
    "drink": "inu",
    "leave": "pụọ",
    "understand": "ghọta",
    "how": "kedu",
    "long time": "ogologo oge",
    "school": "ụlọakwụkwọ",
    "take": "napụ",
    "tomorrow": "echi",
    "write": "dee",
    "car": "ụgbọala",
    "how was your day": "kedu otu ụbọchị ahu",
    "did you sleep well": "ị rahụ nke ọma",
    "yes": "ee",
    "i want": "achọrọ m",
    "everything": "ihe niile",
    "mother": "nne"
}

# Igala Dictionary
igala_dict = {
    "come": "wa",
    "stand": "le",
    "sit": "du",
    "god": "Ojo",
    "morning": "ojokale",
    "night": "ojoko",
    "we/us": "ami",
    "water": "omi",
    "drink": "mu",
    "leave": "ya",
    "understand": "moto",
    "how": "ane",
    "long time": "ojo gogo",
    "school": "ile akwule",
    "take": "gba",
    "tomorrow": "ikawo",
    "write": "ko",
    "car": "moto",
    "how was your day": "ane ojo le",
    "did you sleep well": "du ole",
    "yes": "ee",
    "i want": "mi gba",
    "everything": "ugbo gbogbo",
    "mother": "ine"
}

# Yoruba Dictionary
yoruba_dict = {
    "water": "omi",
    "fire": "ina",
    "house": "lle",
    "food": "ounje",
    "child": "omo",
    "man": "okunrin",
    "woman": "obinrin",
    "book": "iwe",
    "sun": "oorun",
    "moon": "osupa",
    "God": "olorun",
    "road": "ona",
    "friend": "ore",
    "tree": "lgi",
    "rain": "ojo",
    "market": "oja",
    "body": "ara",
    "head": "ori",
    "hand": "owo",
    "love": "ife"
}

# Dictionary mapping
dictionaries = {
    "Igbo": igbo_dict,
    "Igala": igala_dict,
    "Yoruba": yoruba_dict
}

# Page styling
st.set_page_config(page_title="Dictionary Translator", layout="centered")
st.title("🌍 Dictionary Translator")

# Get user's name
user_name = st.text_input("What is your name?", placeholder="Enter your name here")

if user_name:
    st.success(f"Hello, {user_name}! 👋")
    
    # Select dictionary
    selected_dict = st.selectbox(
        "Which language would you like to translate to?",
        list(dictionaries.keys())
    )
    
    # Get the selected dictionary
    current_dict = dictionaries[selected_dict]
    
    # Select word to translate
    english_word = st.selectbox(
        f"Choose an English word to translate to {selected_dict}:",
        sorted(list(current_dict.keys()))
    )
    
    # Show translation
    if english_word:
        translation = current_dict[english_word]
        st.info(f"**'{english_word}'** means **'{translation}'** in {selected_dict}")
else:
    st.info("👈 Please enter your name to get started!")
