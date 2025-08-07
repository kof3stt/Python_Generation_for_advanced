# Стоимость строки
cost = len(input())
print("{} р. {} коп.".format(cost * 60 // 100, cost * 60 % 100))
