# Сумма чисел в файле
with open("nums.txt", encoding="utf-8") as file:
    total = 0
    for line in file:
        for c in line:
            if not c.isdigit():
                line = line.replace(c, " ")
        total += sum(map(int, line.split()))
    print(total)
