# Симметричная матрица
n = int(input())
data = [[int(i) for i in input().split()] for _ in range(n)]
flag = "YES"
for i in range(n):
    for j in range(n):
        if data[i][j] != data[n - j - 1][n - i - 1]:
            flag = "NO"
            break
    if flag == "NO":
        break
print(flag)
