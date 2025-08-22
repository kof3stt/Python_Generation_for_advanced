# Обратный порядок 🔄
with open("data.txt", encoding="utf-8") as file:
    print(*[line.rstrip() for line in file.readlines()][::-1], sep="\n")
