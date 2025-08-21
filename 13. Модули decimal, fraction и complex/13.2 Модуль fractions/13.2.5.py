# Сумма дробей 1
from fractions import Fraction


print(sum([Fraction(1, i**2) for i in range(1, int(input()) + 1)]))
