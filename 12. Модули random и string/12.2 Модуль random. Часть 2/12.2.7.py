# Тайный друг 🕵🏻🌶️
from random import shuffle


def check_two_lists(list1, list2):
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            return True
    return False


data = []
for _ in range(int(input())):
    data.append(input())
friends = data.copy()
while check_two_lists(data, friends):
    shuffle(friends)
for i in range(len(data)):
    print(f"{data[i]} - {friends[i]}")
