# Подсписки списка 🌶️🌶️
data = input().split()
my_list = [[]]
for i in range(len(data)):
    for j in range(i, len(data)):
        my_list.append(data[i : j + 1])
print(my_list)
