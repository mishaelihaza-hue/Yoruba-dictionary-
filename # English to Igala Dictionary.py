# English to Igala Dictionary

words = {
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

print("Translate Words from English to Igala")
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
