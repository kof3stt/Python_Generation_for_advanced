import random


data = set()
while len(data) < 7:
    data.add(random.randint(1, 49))
print(*sorted(data))
