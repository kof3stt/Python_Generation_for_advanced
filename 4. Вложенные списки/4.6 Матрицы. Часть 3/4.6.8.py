# Заполнение змейкой 🐍
n, m = [int(x) for x in input().split()]
data = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        data[i][j] = m * i + ((i + 1) % 2) * (j + 1) + (i % 2) * (m - j)
for i in range(n):
    for j in range(m):
        print(str(data[i][j]).ljust(3), end="")
    print()
