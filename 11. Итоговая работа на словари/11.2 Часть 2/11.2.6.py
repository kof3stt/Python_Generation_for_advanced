# Опасный вирус 😈
data = {}
do = {"write": "W", "read": "R", "execute": "X"}
for _ in range(int(input())):
    file, *oper = input().split()
    data[file] = oper
for _ in range(int(input())):
    operation, file = input().split()
    command = do[operation]
    if command in data[file]:
        print("OK")
    else:
        print("Access denied")
