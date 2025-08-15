# Страны и города
data = {}
for _ in range(int(input())):
    country, *cities = input().split()
    data[country] = cities
for _ in range(int(input())):
    city = input()
    for country, cities in data.items():
        if city in cities:
            print(country)
