words = {
    "i": "من",
    "love": "دوست دارم",
    "python": "پایتون",
    "hello": "سلام",
    "book": "کتاب",
    "water": "آب",
    "computer": "رایانه",
    "school": "مدرسه",
}

sentence = "I love python and AI"
translated_words = []

for word in sentence.lower().split():
    if word in words:
        translated_words.append(words[word])
    else:
        translated_words.append(f"[{word}]")

print(" ".join(translated_words))
