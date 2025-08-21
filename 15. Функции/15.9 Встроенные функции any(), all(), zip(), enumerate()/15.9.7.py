# Отличники
data = []
for _ in range(int(input())):
    data.append(
        any(map(lambda x: x.endswith("5"), [input() for _ in range(int(input()))]))
    )
print(("NO", "YES")[all(data)])
