# Юный математик 🤓🌶️
from fractions import Fraction


n = int(input())
num = Fraction(1, n)
maxi = num
for i in range(1, n):
    for j in range(1, n):
        if i + j == n and i < j:
            num = Fraction(i, j)
            if num.numerator == i:
                maxi = max(maxi, num)
print(maxi)
