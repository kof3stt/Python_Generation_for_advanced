# Заполнение спиралью 🌀🌶️🌶️
n, m = [int(i) for i in input().split()]
data = [[0] * m for _ in range(n)]
x = y = 0
dx, dy = 1, 0
for i in range(n * m):
    data[y][x] = i + 1
    next_x = x + dx
    next_y = y + dy
    if (
        next_x < 0
        or next_x >= m
        or next_y < 0
        or next_y >= n
        or data[next_y][next_x] != 0
    ):
        dx, dy = -dy, dx
        next_x = x + dx
        next_y = y + dy
    if i < n * m - 1:
        x = next_x
        y = next_y

for i in range(n):
    for j in range(m):
        print(str(data[i][j]).ljust(3), end="")
    print()
