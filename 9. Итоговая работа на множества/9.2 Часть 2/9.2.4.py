# Книги на прочтение 📚
m, n = int(input()), int(input())
home = {input() for _ in range(m)}
for i in range(n):
    print("NO" if input() not in home else "YES")
