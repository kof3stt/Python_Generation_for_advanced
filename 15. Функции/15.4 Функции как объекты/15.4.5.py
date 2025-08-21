# Математические функции
from math import sin


n, command = int(input()), input()
commandos = {
    "квадрат": n**2,
    "куб": n**3,
    "корень": n**0.5,
    "модуль": abs(n),
    "синус": sin(n),
}


def calc(command):
    return commandos[command]


print(calc(command))
