# Общая стоимость 💰
from operator import add
from functools import reduce


file = open("prices.txt", encoding="utf-8")
print(
    reduce(
        add,
        map(
            lambda lst: lst[0] * lst[1],
            map(lambda line: list(map(int, line.rstrip().split("\t")[1:])), list(file)),
        ),
        0,
    )
)
file.close()
