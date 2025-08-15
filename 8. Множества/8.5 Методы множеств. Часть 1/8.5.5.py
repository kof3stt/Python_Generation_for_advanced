# Счетчик верных решений ✅🌶️🌶️
n = int(input())
data = set()
correct = 0
for _ in range(n):
    user, result = input().split(": ")
    if result == "Correct":
        correct += 1
        data.add(user)
if data:
    print("Верно решили {} учащихся".format(len(data)))
    print("Из всех попыток {}% верных".format(int(0.5 + correct / n * 100)))
else:
    print("Вы можете стать первым, кто решит эту задачу")
