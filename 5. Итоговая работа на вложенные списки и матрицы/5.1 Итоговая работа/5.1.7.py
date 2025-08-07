# Ходы ферзя
coordinates = input()
letters = "abcdefgh"
x = int(letters.index(coordinates[0]))
y = int(coordinates[1]) - 1
data = [["."] * 8 for _ in range(8)]
for i in range(len(data)):
    for j in range(len(data)):
        if x == j or 7 - y == i or (x - j) ** 2 == (7 - y - i) ** 2:
            data[i][j] = "*"
data[7 - y][x] = "Q"
for row in data:
    print(*row)
