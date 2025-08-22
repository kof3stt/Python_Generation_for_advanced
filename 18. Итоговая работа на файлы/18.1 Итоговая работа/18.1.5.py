# Tail of a File 🔚
with open(input(), encoding="utf-8") as file:
    data = file.readlines()
    print(*data[-10:], sep="")
