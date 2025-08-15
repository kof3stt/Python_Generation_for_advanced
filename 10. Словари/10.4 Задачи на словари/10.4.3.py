# Анаграммы 2
word1 = input().lower()
d1 = {c: word1.count(c) for c in word1 if c.isalpha()}
word2 = input().lower()
d2 = {c: word2.count(c) for c in word2 if c.isalpha()}
print(("YES", "NO")[d1 != d2])
