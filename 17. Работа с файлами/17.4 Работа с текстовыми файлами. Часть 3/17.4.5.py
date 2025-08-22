# Загадка от Жака Фреско 🐐🌶️
with open("goats.txt", encoding="utf-8") as goats, open(
    "answer.txt", "w", encoding="utf-8"
) as output:
    goats.readline()
    line = goats.readline()
    colours = dict()
    while line != "GOATS\n":
        colour, goat = line.split()
        colours[colour] = 0
        line = goats.readline()
    line = goats.readline()
    while line != "":
        colour, goat = line.split()
        colours[colour] += 1
        line = goats.readline()
    total = sum(colours.values())
    for key, value in colours.items():
        if value > total * 0.07:
            print(f"{key} goat", file=output)
