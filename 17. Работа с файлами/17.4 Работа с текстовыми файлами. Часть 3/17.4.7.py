# Лог файл 📝🌶️
with open("logfile.txt", encoding="utf-8") as log_file, open(
    "output.txt", "w", encoding="utf-8"
) as output_file:
    for line in log_file:
        name, surname, start, finish = map(str.rstrip, line.split(), "," * 4)
        start_time = int(start[:2]) * 60 + int(start[4:])
        finish_time = int(finish[:2]) * 60 + int(finish[4:])
        if abs(finish_time - start_time) >= 60:
            output_file.write(name + " " + surname + "\n")
