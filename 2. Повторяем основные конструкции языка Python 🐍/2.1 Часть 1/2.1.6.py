# Переворот числа 🔄
num = input()
print(int(num[:-5] + num[-5:][::-1]))
