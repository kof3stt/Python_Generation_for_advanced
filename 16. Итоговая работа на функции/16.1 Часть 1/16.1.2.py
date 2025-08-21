# Pretty print
def pretty_print(data, side="-", delimiter="|"):
    line = f" {delimiter} ".join(map(str, data))
    print(" " + side * (len(line) + 2))
    print(f"{delimiter} {line} {delimiter}")
    print(" " + side * (len(line) + 2))
