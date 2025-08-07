# Список по образцу 1
n = int(input())
print(*([[int(i) for i in range(1, n + 1)] for j in range(n)]), sep="\n")
