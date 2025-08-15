# Исправление дубликатов 🌶️
ids = input().split()
data = {}
for id in ids:
    if id in data:
        print(f"{id}_{data[id]}", end=" ")
    else:
        print(id, end=" ")
    data[id] = data.get(id, 0) + 1
