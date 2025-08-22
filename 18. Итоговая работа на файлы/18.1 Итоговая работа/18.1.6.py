# Forbidden words 🤬🌶️
with open(input(), encoding="utf-8") as file, open(
    "forbidden_words.txt", encoding="utf-8"
) as words:
    noway = words.read().split()
    data = file.read()
    data_copy = data.lower()
    for i in noway:
        while data_copy.find(i) != -1:
            data = data.replace(
                data[data_copy.find(i) : data_copy.find(i) + len(i)], "*" * len(i)
            )
            data_copy = data_copy.replace(
                data_copy[data_copy.find(i) : data_copy.find(i) + len(i)],
                "*" * len(i),
                1,
            )
    print(data)
