# Камень, ножницы, бумага, ящерица, Спок 🌶️
s = ["ножницы", "бумага", "камень", "ящерица", "Спок"]
timur, ruslan = input(), input()
t, r = s.index(timur) + 1, s.index(ruslan) + 1
if t - r == 1:
    print("Руслан")
elif t - r == 2:
    print("Тимур")
elif t - r == -3:
    print("Тимур")
elif t - r == 4:
    print("Тимур")
elif r - t == 1:
    print("Тимур")
elif r - t == 2:
    print("Руслан")
elif r - t == -3:
    print("Руслан")
elif r - t == 4:
    print("Руслан")
elif r - t == 0:
    print("ничья")
