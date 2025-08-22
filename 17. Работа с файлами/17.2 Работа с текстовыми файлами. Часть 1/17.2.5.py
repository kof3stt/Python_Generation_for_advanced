# Сумма двух-2
file = open("nums.txt", encoding="utf-8")
total = 0
for line in file:
    if line.strip() != "":
        total += int(line)
print(total)
file.close()
