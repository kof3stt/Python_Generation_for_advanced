# Диагонали, параллельные главной
n = int(input())
data = [[abs(i - j) for i in range(n)] for j in range(n)]
for row in data:
    print(*row)
