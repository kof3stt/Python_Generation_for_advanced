# Случайная строка 🎲
from random import randint


file = open("lines.txt", "r", encoding="utf-8")
my_list = file.readlines()
print(my_list[randint(0, len(my_list))].rstrip("\n"))
file.close()
