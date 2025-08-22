# Неповторимые цифры
text = input()
print("YES" if len(text) == len(set(text)) else "NO")
