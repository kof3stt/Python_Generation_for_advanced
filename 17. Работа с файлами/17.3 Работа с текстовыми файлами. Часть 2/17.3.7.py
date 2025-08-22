# Random name and surname 🎲
from random import choice


with open("first_names.txt", encoding="utf-8") as names, open(
    "last_names.txt", encoding="utf-8"
) as surnames:
    names_lst = names.readlines()
    surnames_lst = surnames.readlines()
    for _ in range(3):
        print(choice(names_lst).rstrip(), choice(surnames_lst).rstrip())
