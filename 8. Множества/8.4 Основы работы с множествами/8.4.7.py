# Все 10 цифр
print(("YES", "NO")[len(set(input() + input())) != 10])
