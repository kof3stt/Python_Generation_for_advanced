# Симметричная матрица 💠
n = int(input())
data = [[int(i) for i in input().split()] for _ in range(n)]
flag = "YES"
for i in range(n):
    for j in range(n):
        if data[i][j] != data[j][i]:
            flag = "NO"
            break
print(flag)
