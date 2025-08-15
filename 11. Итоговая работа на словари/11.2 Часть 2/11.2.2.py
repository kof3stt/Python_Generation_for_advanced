# Порядковый номер
text = input().split()
data = {}
for c in text:
    data[c] = data.get(c, 0) + 1
    print(data[c], end=" ")
