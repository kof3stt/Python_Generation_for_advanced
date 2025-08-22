# Goooood students 😇
with open("grades.txt", encoding="utf-8") as file:
    print(
        sum(
            map(
                lambda x: min(x) >= 65,
                [
                    [int(i) for i in line.rstrip().split()[1:]]
                    for line in file.readlines()
                ],
            )
        )
    )
