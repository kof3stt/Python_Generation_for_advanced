# Суммы четвертей
n = int(input())
data = [[int(i) for i in input().split()] for _ in range(n)]
result = [0] * 4
for i in range(n):
    for j in range(n):
        if i < j and i < n - j - 1:
            result[0] += data[i][j]
        elif i < j and i > n - j - 1:
            result[1] += data[i][j]
        elif i > j and i > n - j - 1:
            result[2] += data[i][j]
        elif i > j and i < n - j - 1:
            result[3] += data[i][j]
print("Верхняя четверть:", result[0])
print("Правая четверть:", result[1])
print("Нижняя четверть:", result[2])
print("Левая четверть:", result[3])
