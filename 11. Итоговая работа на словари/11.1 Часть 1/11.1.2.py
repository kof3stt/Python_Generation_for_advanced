emails = {
    "nosu.edu": ["timyr", "joseph", "svetlana.gaeva", "larisa.mamuk"],
    "gmail.com": ["ruslan.chaika", "rustam.mini", "stepik-best"],
    "msu.edu": ["apple.fruit", "beegeek", "beegeek.school"],
    "yandex.ru": ["surface", "google"],
    "hse.edu": ["tomas-henders", "cream.soda", "zivert"],
    "mail.ru": ["angel.down", "joanne", "the.fame.moster"],
}
data = []
for i, j in emails.items():
    for name in j:
        data.append(str(name) + "@" + str(i))
print(*sorted(data), sep="\n")
