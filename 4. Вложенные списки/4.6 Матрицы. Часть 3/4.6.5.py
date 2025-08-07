# Заполнение 3
n = int(input())
data = [[1 if i == j or i == n - j - 1 else 0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        print(str(data[i][j]).ljust(3), end="")
    print()
