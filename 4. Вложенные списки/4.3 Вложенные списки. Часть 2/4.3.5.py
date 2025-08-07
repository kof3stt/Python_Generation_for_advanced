# Упаковка дубликатов 🌶️
data = [[]]
for el in input().split():
    if el not in data[-1]:
        data.append([el])
    else:
        data[-1].extend(el)
del data[0]
print(data)
