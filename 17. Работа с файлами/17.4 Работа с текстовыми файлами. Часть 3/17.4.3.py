# Нумерация строк 🔢
with open("input.txt", encoding="utf-8") as input_file, open(
    "output.txt", "w", encoding="utf-8"
) as output_file:
    for index, line in enumerate(input_file.readlines(), 1):
        output_file.write(f"{index}) {line}")
