# CSV-файл 📂
def read_csv():
    with open("data.csv", encoding="utf-8") as file:
        headers = file.readline().rstrip().split(",")
        lines = [line.rstrip().split(",") for line in file.readlines()]
        return [dict(zip(headers, line)) for line in lines]
