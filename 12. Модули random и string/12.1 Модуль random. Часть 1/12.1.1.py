import random


print(
    *[
        "Орел" if x == 1 else "Решка"
        for x in [random.randint(0, 2) for _ in range(int(input()))]
    ],
    sep="\n"
)
