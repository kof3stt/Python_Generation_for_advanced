# Внутри шара
abscissas = [float(i) for i in input().split()]
ordinates = [float(i) for i in input().split()]
applicates = [float(i) for i in input().split()]
print(
    all(
        (
            map(
                lambda x: x[0] ** 2 + x[1] ** 2 + x[2] ** 2 <= 4,
                list(zip(abscissas, ordinates, applicates)),
            )
        )
    )
)
