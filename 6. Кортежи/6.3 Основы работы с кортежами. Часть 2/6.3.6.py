# Конкурсный отбор
students = [input().split() for _ in range(int(input()))]
for row in students:
    print(*row)
print()
for surname, mark in students:
    if int(mark) > 3:
        print(surname, mark)
