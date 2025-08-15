# Числа первой строки
print(*sorted(set(input().split()) - set(input().split()), key=int))
