# Словарь синонимов
data = {}
for _ in range(int(input())):
    s1, s2 = input().split()
    data[s1] = s2
    data[s2] = s1
print(data[input()])
