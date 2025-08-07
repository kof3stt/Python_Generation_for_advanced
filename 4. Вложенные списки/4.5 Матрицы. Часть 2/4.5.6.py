# Зеркальное отображение 🦋
n = int(input())
data = [[int(x) for x in input().split()] for _ in range(n)]
for i in range(n // 2):
    data[i], data[n - i - 1] = data[n - i - 1], data[i]
for row in data:
    print(*row)
