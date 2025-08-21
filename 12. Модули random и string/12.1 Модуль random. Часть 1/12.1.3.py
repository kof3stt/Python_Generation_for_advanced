import random


length = int(input())
for i in range(length):
    a = random.randint(0, 1)
    if a == 0:
        print(chr(random.randint(65, 90)), end="")
    else:
        print(chr(random.randint(97, 122)), end="")
