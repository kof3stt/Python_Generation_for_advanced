# Орел и решка
text = input()
total = 0
for i in range(1, len(text) + 1):
    if text.count("Р" * i) > 0:
        total = i
print(total)
