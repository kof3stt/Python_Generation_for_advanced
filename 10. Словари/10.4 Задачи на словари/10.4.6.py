# Телефонная книга 📒
data = dict()
for _ in range(int(input())):
    phone, name = input().lower().split()
    data.setdefault(name, []).append(phone)
for _ in range(int(input())):
    print(*data.get(input().lower(), ["абонент не найден"]))
