# Конкатенация файлов 🗃️🌶️
files = [input() for _ in range(int(input()))]
with open("output.txt", "w", encoding="utf-8") as output_file:
    for filename in files:
        file = open(filename, encoding="utf-8")
        output_file.write(file.read())
        file.close()
