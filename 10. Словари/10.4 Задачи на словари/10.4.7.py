# Секретное слово
msg = input()
msg_dict = dict([(c, msg.count(c)) for c in set(msg)])
data = {}
for _ in range(int(input())):
    letter, total = input().split(": ")
    data[letter] = int(total)
for c in msg:
    for letter in data:
        if data[letter] == msg_dict[c]:
            print(letter, end="")
