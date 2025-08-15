# Покупки в интернет-магазине 🛒🌶️
sales = {}
for _ in range(int(input())):
    name, item, count = input().split()
    sales[name][item] = sales.setdefault(name, {}).setdefault(item, 0) + int(count)
for key in sorted(sales):
    print(f"{key}:")
    for i in sorted(sales[key].items()):
        print(*i)
