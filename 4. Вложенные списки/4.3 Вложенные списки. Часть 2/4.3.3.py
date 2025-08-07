# Треугольник Паскаля 1 🌶️
n = int(input())
data = [[1] * (i + 1) for i in range(n + 1)]
for i in range(n + 1):
    for j in range(1, i):
        data[i][j] = data[i - 1][j - 1] + data[i - 1][j]
print(data[n])
