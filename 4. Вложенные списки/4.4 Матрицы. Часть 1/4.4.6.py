# Максимальный в области 2 🌶️
n = int(input())
data = [[int(i) for i in input().split()] for _ in range(n)]
max_elem = data[0][0]
for i in range(n):
    for j in range(n):
        if i <= j and i >= n - 1 - j or i >= j and i <= n - j - 1:
            if data[i][j] > max_elem:
                max_elem = data[i][j]
print(max_elem)
