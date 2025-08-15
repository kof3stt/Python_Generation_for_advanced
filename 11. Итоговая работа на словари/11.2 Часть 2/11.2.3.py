# Scrabble game
data = {1: "AEILNORSTU", 2: "DG", 3: "BCMP", 4: "FHVWY", 5: "K", 8: "JX", 10: "QZ"}
total = 0
for i in input():
    for key, value in data.items():
        if i in value:
            total += key
print(total)
