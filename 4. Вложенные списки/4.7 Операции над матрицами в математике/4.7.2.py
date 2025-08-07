# Умножение матриц 🌶️
n, m = [int(i) for i in input().split()]
A = [[int(i) for i in input().split()] for _ in range(n)]
input()
m, k = [int(i) for i in input().split()]
B = [[int(i) for i in input().split()] for _ in range(m)]
data = [[0] * k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for x in range(m):
            data[i][j] += A[i][x] * B[x][j]
for i in range(n):
    for j in range(k):
        print(data[i][j], end=" ")
    print()
