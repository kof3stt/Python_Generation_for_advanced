# Задача Иосифа Флавия 🌶️🌶️
n, k = int(input()), int(input())
people = list(range(1, n + 1))
current = 0
while len(people) > 1:
    current = (current + k - 1) % len(people)
    del people[current]
print(people[0])
