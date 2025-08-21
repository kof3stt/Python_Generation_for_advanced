# Сумма дробей 2
from math import factorial
from fractions import Fraction


print(sum((Fraction(1, factorial(i)) for i in range(1, int(input()) + 1))))
