# Содержимое файла 📑
file_name = input()
file = open(file_name, encoding="utf-8")
print(*[i.strip() for i in file.readlines()])
file.close()
