# Поворот матрицы 🔁
n = int(input())
data = [[int(x) for x in input().split()] for _ in range(n)]
for i in range(n):
    for j in range(n - 1, -1, -1):
        print(data[j][i], end=" ")
    print()
