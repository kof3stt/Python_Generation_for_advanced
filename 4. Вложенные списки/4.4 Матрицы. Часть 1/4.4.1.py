# Вывести матрицу 1
n, m = int(input()), int(input())
data = [[input() for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        print(data[i][j], end=" ")
    print()
