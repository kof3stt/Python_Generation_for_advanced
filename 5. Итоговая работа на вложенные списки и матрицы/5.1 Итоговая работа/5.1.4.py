# Снежинка
n = int(input())
data = [["."] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == n // 2 or j == n // 2 or i == j or j == n - i - 1:
            data[i][j] = "*"
for i in range(len(data)):
    print(*data[i], sep=" ")
