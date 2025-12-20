words = {
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

print("Translate Words from English to Igbo")
print("Choose a word from the list below:\n")

for word in words:
    print("-", word)

while True:
    word = input("\nEnter word to be translated: ").lower()

    if word in words:
        print(f"'{word}' means '{words[word]}'")
        break
    else:
        print(f"Sorry, '{word}' is not in the dictionary. Try again.")