# Максимальный в области 2
n = int(input())
data = [[int(i) for i in input().split()] for _ in range(n)]
print(max([data[i][j] for i in range(n) for j in range(n) if i >= n - 1 - j]))
