# Сдвиг в развитии ↩️
numbers = [int(num) for num in input().split()]
print(*numbers[-1:] + numbers[:-1])
