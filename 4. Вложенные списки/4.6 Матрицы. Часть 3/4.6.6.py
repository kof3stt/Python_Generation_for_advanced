# Заполнение 4
n = int(input())
data = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i <= j and j <= n - i - 1 or i >= j and j >= n - i - 1:
            data[i][j] = 1
for i in range(n):
    for j in range(n):
        print(str(data[i][j]).ljust(3), end="")
    print()
