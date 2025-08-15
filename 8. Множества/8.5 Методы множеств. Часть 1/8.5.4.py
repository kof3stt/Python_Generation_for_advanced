# Встречалось ли число раньше?
numbers = [int(i) for i in input().split()]
data = set()
for num in numbers:
    if num in data:
        print("YES")
    else:
        print("NO")
    data.add(num)
