# Заполнение 5 🌶️
n, m = [int(x) for x in input().split()]
data = [[1] * m for _ in range(n)]
for j in range(m):
    data[0][j] = j + 1
for i in range(1, n):
    for j in range(m):
        if j != m - 1:
            data[i][j] = data[i - 1][j + 1]
        else:
            data[i][j] = data[i - 1][0]
for i in range(n):
    for j in range(m):
        print(str(data[i][j]).ljust(3), end="")
    print()
