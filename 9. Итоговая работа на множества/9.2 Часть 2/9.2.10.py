# Онлайн-школа BEEGEEK 5 🐝🌶️
m, n = int(input()), int(input())
surnames = [input() for _ in range(n + m)]
students = set(surnames)
both_sub = len(surnames) - len(students)
one_sub = len(students) - both_sub
print(one_sub or "NO")
