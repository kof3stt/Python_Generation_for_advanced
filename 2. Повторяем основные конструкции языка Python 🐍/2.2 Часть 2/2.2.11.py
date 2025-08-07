# Роскомнадзор запретил букву а 🚫🌶️🌶️
text = (input() + " запретил букву").split()
forbidden = list()
for i in range(ord("а"), ord("я") + 1):
    if chr(i) not in "".join(text):
        continue
    text.append(chr(i))
    for j in range(len(text)):
        for c in text[j]:
            if c in forbidden:
                text[j] = text[j].replace(c, "")
    while "" in text:
        text.remove("")
    forbidden.append(chr(i))
    if len(text) == 1 and text[0] == forbidden[-1]:
        break
    print(" ".join(text))
