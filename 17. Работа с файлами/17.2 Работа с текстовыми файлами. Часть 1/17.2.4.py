# Сумма двух-1
file = open("numbers.txt", encoding="utf-8")
print(sum([int(line.strip("\n")) for line in file.readlines()]))
file.close()
