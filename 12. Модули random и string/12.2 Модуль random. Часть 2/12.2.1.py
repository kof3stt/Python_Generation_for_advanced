from random import randint


def generate_ip():
    return ".".join([str(randint(0, 255)) for _ in range(4)])
