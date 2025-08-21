# Упорядоченные дроби
from fractions import Fraction
from math import gcd


n = int(input())
data = []
for i in range(1, n):
    for j in range(1, n + 1):
        num = Fraction(i, j)
        if i < j and gcd(i, j) == 1:
            data.append(Fraction(i, j))
print(*sorted(data), sep="\n")
