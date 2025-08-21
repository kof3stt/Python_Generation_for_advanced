# Генератор паролей 2 🌶️
from random import sample
from string import ascii_uppercase, ascii_lowercase, ascii_letters, digits


LETTER = "".join((set(ascii_letters) | set(digits)) - set("lI1oO0"))


def generate_password(length):
    password = "".join(sample(LETTER, length))
    while (
        (sum([password.count(i) for i in ascii_uppercase]) == 0)
        or (sum([password.count(i) for i in digits]) == 0)
        or (sum([password.count(i) for i in ascii_lowercase]) == 0)
    ):
        password = "".join(sample(LETTER, length))
    return password


def generate_passwords(count, length):
    data = set()
    while len(data) != count:
        data.add(generate_password(length))
    return data


n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep="\n")
