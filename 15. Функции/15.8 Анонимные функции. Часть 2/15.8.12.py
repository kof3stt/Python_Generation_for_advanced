# Значение многочлена 🌶️
from functools import reduce


def evaluate(coef, x):
    return reduce(lambda s, a: s * x + a, coef, 0)


coef = list(map(int, input().split()))
x = int(input())

print(evaluate(coef, x))
