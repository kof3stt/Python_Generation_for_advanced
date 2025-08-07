# Ходы коня 🐎
coordinates = input()
letters = "abcdefgh"
x = int(letters.index(coordinates[0]))
y = int(coordinates[1]) - 1
data = [["."] * 8 for _ in range(8)]
data[7 - y][x] = "N"
for i in range(8):
    for j in range(8):
        if abs(7 - y - i) * abs(x - j) == 2:
            data[i][j] = "*"
for row in data:
    print(*row)
