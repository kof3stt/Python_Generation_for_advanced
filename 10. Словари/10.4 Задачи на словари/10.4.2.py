# Анаграммы 1
word1 = input()
d1 = {c: word1.count(c) for c in word1}
word2 = input()
d2 = {c: word2.count(c) for c in word2}
print(("YES", "NO")[d1 != d2])
