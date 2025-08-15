# Количество слов в тексте
text = [word.lower().strip(".,;:-?!") for word in input().split()]
print(len(set(text)))
