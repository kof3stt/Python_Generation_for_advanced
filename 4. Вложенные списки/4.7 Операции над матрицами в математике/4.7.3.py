# Возведение матрицы в степень 🌶️
n = int(input())
data = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())
pred = data
for y in range(m - 1):
    tek = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for x in range(n):
                tek[i][j] += pred[i][x] * data[x][j]
    pred = tek
for i in tek:
    print(*i)
