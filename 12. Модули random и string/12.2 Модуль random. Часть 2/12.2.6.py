from random import randint


data = [[0] * 5 for _ in range(5)]
my_set = set()
for i in range(5):
    for j in range(5):
        elem = randint(1, 75)
        while elem in my_set:
            elem = randint(1, 75)
        my_set.add(elem)
        data[i][j] = elem
data[2][2] = 0
for i in range(5):
    for j in range(5):
        print(str(data[i][j]).ljust(3), end="")
    print()
