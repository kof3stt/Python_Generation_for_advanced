# Гематрия слова
def gem(word):
    return (sum([ord(i.upper()) - ord("A") for i in word]), word)


data = []
for _ in range(int(input())):
    data.append(input())
print(*sorted(data, key=gem), sep="\n")
