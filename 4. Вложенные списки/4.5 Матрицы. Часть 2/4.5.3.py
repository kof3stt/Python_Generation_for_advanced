# Обмен столбцов ⏸️
n, m = int(input()), int(input())
data = [[int(i) for i in input().split()] for _ in range(n)]
i_old, j_new = [int(x) for x in input().split()]
for i in range(n):
    for j in range(m):
        if j == i_old:
            data[i][j], data[i][j_new] = data[i][j_new], data[i][j]
for row in data:
    print(*row)
