# Интересные числа
def f(x):
    numbers = [int(i) for i in str(x)]
    return all(map(lambda i: i != 0 and x % i == 0, numbers))


print(*list(filter(f, range(int(input()), int(input()) + 1))))
