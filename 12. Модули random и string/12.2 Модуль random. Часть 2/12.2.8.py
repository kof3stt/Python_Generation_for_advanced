# Генератор паролей 1
from random import choice, sample
from string import ascii_letters, digits


LETTER = "".join((set(ascii_letters) | set(digits)) - set("lI1oO0"))


def generate_password(length):
    return "".join(sample(LETTER, length))


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep="\n")
