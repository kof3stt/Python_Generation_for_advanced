from string import ascii_uppercase as l
from random import randrange as r, choice as c


def generate_index():
    return f"{c(l)}{c(l)}{r(100)}_{r(100)}{c(l)}{c(l)}"
