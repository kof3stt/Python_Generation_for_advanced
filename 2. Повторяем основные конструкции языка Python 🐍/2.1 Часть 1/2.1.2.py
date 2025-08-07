# Индекс массы тела
weight, height = float(input()), float(input())
imb = weight / height**2
if 18.5 <= imb <= 25:
    print("Оптимальная масса")
elif imb < 18.5:
    print("Недостаточная масса")
else:
    print("Избыточная масса")
