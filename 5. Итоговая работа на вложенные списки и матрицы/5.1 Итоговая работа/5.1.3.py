# Транспонирование матрицы
n = int(input())
data = [[int(i) for i in input().split()] for _ in range(n)]
for i in range(n):
    for j in range(n):
        print(data[j][i], end=" ")
    print()
