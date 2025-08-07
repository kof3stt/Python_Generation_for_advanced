# Побочная диагональ
n = int(input())
data = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        data[i][n - i - 1] = 1
        if i + j > n - 1:
            data[i][j] = 2
[print(*row) for row in data]
