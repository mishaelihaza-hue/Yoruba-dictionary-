words = {
    "come": "zo",
    "stand": "tsaya",
    "sit": "zauna",
    "god": "allah",
    "morning": "safiya",
    "night": "dare",
    "we/us": "mu",
    "water": "ruwa",
    "drink": "sha",
    "leave": "tafi",
    "understand": "fahimta",
    "how": "yaya",
    "long time": "dogon lokaci",
    "school": "makaranta",
    "take": "ɗauka",
    "tomorrow": "gobe",
    "write": "rubuta",
    "car": "mota",
    "how was your day": "yaya ranarka",
    "did you sleep well": "ka kwana lafiya?",
    "yes": "eh",
    "i want": "ina so",
    "everything": "komai",
    "mother": "uwa"
}

print("Translate Words from English to Hausa")
print("Choose a word from the list below:\n")

for word in words:
    print("-", word)

while True:
    word = input("\nEnter word to be translated: ").lower()

    if word in words:
        print(f"'{word}' means '{words[word]}'")
        break
    else:
        print(f"Sorry, '{word}' is not in the dictionary.")
        break