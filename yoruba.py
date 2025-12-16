#English to Yoruba Dictionary

english_to_yoruba = {
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

#Search loop
while True:
    word = input("\nEnter and English word (or 'exit' to quit): "). lower()

    if word == "exit":
        print("Goodbye!")
        break

    if word in english_to_yoruba:
        print(f"Igbo: {english_to_yoruba[word]}")

    else:
        print("Word not found!")