# Заполнение 2
n, m = [int(x) for x in input().split()]
data = [[i * n + j + 1 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        print(str(data[i][j]).ljust(3), end="")
    print()
