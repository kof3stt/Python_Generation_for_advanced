# Сумма чисел в строках
with open("numbers.txt", encoding="utf-8") as file:
    for line in file:
        print(sum(map(int, line.split())))
