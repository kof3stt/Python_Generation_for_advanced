# Переворот строки 🙃
with open("text.txt", encoding="utf-8") as file:
    print(file.readline().rstrip()[::-1])
