# Онлайн-школа BEEGEEK 2 🐝
m, n = (int(input()) for _ in range(2))
mat = {input() for _ in range(m)}
inf = {input() for _ in range(n)}
print(len(mat - inf))
