# Кремниевая долина 🤖🌶️
data = []
for i in range(int(input())):
    text = input()
    a = text.find("a")
    n = text.find("n", a)
    t = text.find("t", n)
    o = text.find("o", t)
    n = text.find("n", o)
    if n != -1 and o != -1:
        data.append(i + 1)
print(*data)
