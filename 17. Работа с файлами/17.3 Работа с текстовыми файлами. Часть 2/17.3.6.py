# Статистика по файлу 📊
with open("file.txt", encoding="utf-8") as file:
    context = file.read()
    print("Input file contains:")
    print(f"{len(list(filter(str.isalpha, context)))} letters")
    print(f"{len(context.split())} words")
    print(f"{len(context.split('\n'))} lines")
