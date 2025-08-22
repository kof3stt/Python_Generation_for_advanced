# Необычные страны 🗺️
with open("population.txt", encoding="utf-8") as file:
    for line in file:
        country, population = line.split("\t")
        if int(population) > 500_000 and country.startswith("G"):
            print(country)
