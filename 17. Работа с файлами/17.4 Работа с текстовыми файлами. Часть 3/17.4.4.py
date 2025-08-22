# Подарок на новый год 🎁
with open("class_scores.txt", encoding="utf-8") as old, open(
    "new_scores.txt", "w", encoding="utf-8"
) as new:
    for line in old:
        name, mark = line.split()
        new.write(f"{name} {min(100, int(mark) + 5)}\n")
