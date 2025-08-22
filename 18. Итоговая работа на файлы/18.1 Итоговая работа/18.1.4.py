# Самое длинное слово в файле
with open("words.txt", encoding="utf-8") as file:
    data = file.read().split()
    print(*list(filter(lambda x: len(x) == len(max(data, key=len)), data)), sep="\n")
