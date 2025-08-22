# Суммарная стоимость
with open("ledger.txt", encoding="utf-8") as file:
    print(f"${sum([int(price.lstrip("$")) for price in file.readlines()])}")
