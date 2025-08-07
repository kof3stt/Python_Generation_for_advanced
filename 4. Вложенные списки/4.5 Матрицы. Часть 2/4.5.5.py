# Обмен диагоналей 🔃
n = int(input())
data = [[int(i) for i in input().split()] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            data[i][j], data[n - j - 1][j] = data[n - j - 1][j], data[i][j]
for row in data:
    print(*row)
