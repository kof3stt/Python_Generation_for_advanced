# Интересная сортировка-2
data = [int(i) for i in input().split()]


def compare(n):
    return sum([int(i) for i in str(n)])


data.sort()
data.sort(key=compare)
print(*data)
