words = [
    "Plum",
    "Grapefruit",
    "apple",
    "orange",
    "pomegranate",
    "Cranberry",
    "lime",
    "Lemon",
    "grapes",
    "persimmon",
    "tangerine",
    "Watermelon",
    "currant",
    "Almond",
]
print(*sorted({i.lower()[0] for i in words}))
