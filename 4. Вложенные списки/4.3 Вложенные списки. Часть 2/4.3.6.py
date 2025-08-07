# Разбиение на чанки 🌶️
def chuncked(data, n):
    return [data[i : i + n] for i in range(0, len(data), n)]


data, n = input().split(), int(input())
print(chuncked(data, n))
