# Операции над дробями
from fractions import Fraction


a = input()
fa = Fraction(a)
b = input()
fb = Fraction(b)
print(
    f"{a} + {b} = {fa+fb}",
    f"{a} - {b} = {fa-fb}",
    f"{a} * {b} = {fa*fb}",
    f"{a} / {b} = {fa/fb}",
    sep="\n",
)
