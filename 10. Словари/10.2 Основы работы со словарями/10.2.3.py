# Набор сообщений 📩
message = input().upper()
data = {
    ".,?!:": "1",
    "ABC": "2",
    "DEF": "3",
    "GHI": "4",
    "JKL": "5",
    "MNO": "6",
    "PQRS": "7",
    "TUV": "8",
    "WXYZ": "9",
    " ": "0",
}
for c in message:
    for key in data:
        if c in key:
            print(data[key] * (key.index(c) + 1), end="")
