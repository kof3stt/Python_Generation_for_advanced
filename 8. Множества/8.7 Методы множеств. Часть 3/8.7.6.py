# Урок биологии 🌱
print(
    *sorted(
        set(range(0, 11))
        - set([int(i) for i in input().split()])
        - set([int(i) for i in input().split()])
        - set([int(i) for i in input().split()])
    )
)
