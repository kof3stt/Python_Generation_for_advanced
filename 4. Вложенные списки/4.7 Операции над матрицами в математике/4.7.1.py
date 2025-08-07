# Сложение матриц
n, m = [int(i) for i in input().split()]
A = [[int(i) for i in input().split()] for _ in range(n)]
input()
B = [[int(i) for i in input().split()] for _ in range(n)]
result = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        result[i][j] = A[i][j] + B[i][j]
for i in range(n):
    for j in range(m):
        print(str(result[i][j]).ljust(3), end="")
    print()
