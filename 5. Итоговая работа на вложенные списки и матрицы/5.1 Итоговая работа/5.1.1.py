# Каждый n-ый элемент
data = input().split()
n = int(input())
result = []
for i in range(n):
    result.append(data[i : len(data) : n])
print(result)
