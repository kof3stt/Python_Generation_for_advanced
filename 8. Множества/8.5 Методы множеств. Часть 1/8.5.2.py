# Уникальные символы 2
my_set = set()
for _ in range(int(input())):
    for c in input().lower():
        my_set.add(c)
print(len(my_set))
