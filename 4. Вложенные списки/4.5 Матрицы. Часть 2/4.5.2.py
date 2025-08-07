# Максимум в таблице 🔝
n, m = int(input()), int(input())
data = [[int(i) for i in input().split()] for _ in range(n)]
max_elem = data[0][0]
max_i = max_j = 0
for i in range(n):
    for j in range(m):
        if data[i][j] > max_elem:
            max_elem = data[i][j]
            max_i, max_j = i, j
print(max_i, max_j)
