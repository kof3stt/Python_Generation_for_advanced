# Больше среднего
n = int(input())
data = [[int(i) for i in input().split()] for _ in range(n)]
for row in data:
    total = 0
    arithmetic_mean = sum(row) / n
    for elem in row:
        if elem > arithmetic_mean:
            total += 1
    print(total)
