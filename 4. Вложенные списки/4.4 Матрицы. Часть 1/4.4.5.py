# Максимальный в области 1
n = int(input())
data = [[int(i) for i in input().split()] for _ in range(n)]
max_elem = data[0][0]
for i in range(n):
    for j in range(i + 1):
        if data[i][j] > max_elem:
            max_elem = data[i][j]
print(max_elem)
