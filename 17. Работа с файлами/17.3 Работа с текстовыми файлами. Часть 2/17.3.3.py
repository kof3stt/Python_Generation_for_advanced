# Длинные строки ↔️
with open("lines.txt", encoding="utf-8") as file:
    max_len = len(max(file.readlines(), key=len))
    file.seek(0)
    print(*map(str.strip, filter(lambda x: len(x) == max_len, file.readlines())), sep = "\n")
