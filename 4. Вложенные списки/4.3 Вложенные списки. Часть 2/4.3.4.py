# Треугольник Паскаля 2
n = int(input())
data = [[1] * (i + 1) for i in range(n)]
for i in range(n):
    for j in range(1, i):
        data[i][j] = data[i - 1][j - 1] + data[i - 1][j]
for row in data:
    print(*row)
