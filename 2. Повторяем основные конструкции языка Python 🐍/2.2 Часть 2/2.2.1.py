# Координатные четверти
total = [0] * 4
for _ in range(int(input())):
    x, y = [int(i) for i in input().split()]
    if x > 0 and y > 0:
        total[0] += 1
    elif x < 0 and y > 0:
        total[1] += 1
    elif x < 0 and y < 0:
        total[2] += 1
    elif x > 0 and y < 0:
        total[3] += 1
print(
    f"Первая четверть: {total[0]}",
    f"Вторая четверть: {total[1]}",
    f"Третья четверть: {total[2]}",
    f"Четвертая четверть: {total[3]}",
    sep="\n",
)
