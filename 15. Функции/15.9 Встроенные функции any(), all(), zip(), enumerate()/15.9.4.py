# Корректный IP-адрес
ip = input().split(".")
print(all(map(lambda s: s.isdigit() and 0 <= int(s) <= 255, ip)))
