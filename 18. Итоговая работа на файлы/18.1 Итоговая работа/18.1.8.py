# Пропущенные комменты 🌶️
with open(input(), encoding="utf-8") as file:
    data = []
    com, i, fun = None, 0, None
    flag = True
    for line in file:
        if line.count("# ") > 0:
            com = i
        elif line.count("def ") > 0:
            fun = i
            if com is None or fun - com > 1:
                data.append(line[4 : line.find("(")])
        i += 1
    if len(data) == 0:
        print("Best Programming Team")
    else:
        print(*data, sep="\n")
