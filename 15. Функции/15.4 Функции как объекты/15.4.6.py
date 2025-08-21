# Интересная сортировка-1
data = [int(i) for i in input().split()]


def compare(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


data.sort(key=compare)
print(*data)
