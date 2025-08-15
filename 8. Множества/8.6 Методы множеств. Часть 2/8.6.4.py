# Общие цифры
data = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
for _ in range(int(input())):
    data.intersection_update(set([int(i) for i in input()]))
print(*sorted(data))
