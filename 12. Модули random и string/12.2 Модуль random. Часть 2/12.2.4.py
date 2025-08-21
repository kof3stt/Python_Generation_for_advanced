from random import randrange


data = set()
while len(data) != 100:
    ticket = str(randrange(1, 10)) + "".join([str(randrange(10)) for _ in range(6)])
    if ticket not in data:
        data.add(ticket)
print(*data, sep="\n")
