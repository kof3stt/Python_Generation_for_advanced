# Шахматная доска
n, m = [int(i) for i in input().split()]
data = [["."] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if (i + j) % 2:
            data[i][j] = "*"
for row in data:
    print(*row)
