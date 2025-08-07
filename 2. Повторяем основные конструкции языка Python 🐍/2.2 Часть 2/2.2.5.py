# Различные элементы
numbers = [int(num) for num in input().split()]
total = 0
for i in range(len(numbers) - 1):
    if numbers[i] == numbers[i + 1]:
        total += 1
print(len(numbers) - total)
