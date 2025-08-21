from decimal import Decimal


num = Decimal(input())
digits = num.as_tuple().digits
print(max(digits) if abs(num) < 1 else min(digits) + max(digits))
