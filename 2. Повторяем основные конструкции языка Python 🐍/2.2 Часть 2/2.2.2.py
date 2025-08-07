# Больше предыдущего
numbers = [int(i) for i in input().split()]
total = 0
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        total += 1
print(total)
