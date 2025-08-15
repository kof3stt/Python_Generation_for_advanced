# Онлайн-школа BEEGEEK 6 🐝🌶️
n = int(input())
result = {input() for _ in range(int(input()))}
for _ in range(n - 1):
    result &= {input() for _ in range(int(input()))}
print(*sorted(result), sep="\n")
