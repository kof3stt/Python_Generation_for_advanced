# Латинский квадрат 🌶️
def is_latin_square(data, n):
    numbers = list(range(1, n + 1))
    for i in range(len(data)):
        tmp_row = sorted(data[i])
        tmp_col = sorted([data[j][i] for j in range(n)])
        if tmp_row != numbers or tmp_col != numbers:
            return "NO"
    return "YES"


n = int(input())
data = [[int(i) for i in input().split()] for _ in range(n)]
print(is_latin_square(data, n))
