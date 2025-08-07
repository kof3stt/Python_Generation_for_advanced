# Заполнение диагоналями ↙️🌶️
n, m = [int(i) for i in input().split()]
data = [[0] * m for _ in range(n)]
index_list = [[i, j] for i in range(n) for j in range(m)]
index_list.sort(key=lambda x: x[0] + x[1])
for i in range(n * m):
    data[index_list[i][0]][index_list[i][1]] = i + 1
for i in range(n):
    for j in range(m):
        print(str(data[i][j]).ljust(3), end="")
    print()
