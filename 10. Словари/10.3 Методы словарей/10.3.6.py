# Самое редкое слово 🌶️
words = [word.strip(".,!?:;-") for word in input().lower().split()]
data = dict.fromkeys(words, 0)
for word in words:
    data[word] += 1
print(min(data, key=lambda word: (data[word], word)))
