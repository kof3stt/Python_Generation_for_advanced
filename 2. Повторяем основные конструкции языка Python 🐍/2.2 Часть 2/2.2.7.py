# Камень, ножницы, бумага
timur = input()
ruslan = input()
if timur == ruslan:
    print("ничья")
elif timur == "камень" and ruslan == "бумага":
    print("Руслан")
elif timur == "ножницы" and ruslan == "камень":
    print("Руслан")
elif timur == "бумага" and ruslan == "ножницы":
    print("Руслан")
else:
    print("Тимур")
