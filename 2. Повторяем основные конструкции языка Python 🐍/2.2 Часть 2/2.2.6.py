# Произведение чисел
f = "НЕТ"
data = []
for i in range(int(input())):
    data.append(int(input()))
num = int(input())
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] * data[j] == num:
            f = "ДА"
            break
    if f == "ДА":
        break
print(f)
