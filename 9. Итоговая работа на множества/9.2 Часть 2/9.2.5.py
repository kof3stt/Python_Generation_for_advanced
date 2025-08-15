# Странное увлечение 📄
first = {int(i) for i in input().split()}
second = {int(i) for i in input().split()}
if first.isdisjoint(second):
    print("BAD DAY")
else:
    print(*sorted(first.intersection(second), reverse=True))
