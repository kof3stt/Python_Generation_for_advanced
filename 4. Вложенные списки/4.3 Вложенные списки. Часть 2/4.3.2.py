# Список по образцу 2
n = int(input())
print(*[[i for i in range(1, j + 1)] for j in range(1, n + 1)], sep="\n")
