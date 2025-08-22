# Три слова
a, b, c = input().split()
print("YES" if set(a) == set(b) == set(c) else "NO")
