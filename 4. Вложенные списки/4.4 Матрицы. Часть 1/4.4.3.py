# След матрицы ↘️
n = int(input())
data = [[int(i) for i in input().split()] for _ in range(n)]
total = 0
for i in range(n):
    total += data[i][i]
print(total)
