# Словарь программиста 📘
data = {}
for _ in range(int(input())):
    word, definition = input().split(": ")
    data[word.lower()] = definition
for _ in range(int(input())):
    print(data.get(input().lower(), "Не найдено"))
