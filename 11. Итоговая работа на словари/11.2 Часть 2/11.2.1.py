# Минутка генетики 🧬
chain = input()
DNA_RNA = {"G": "C", "C": "G", "T": "A", "A": "U"}
print(*[DNA_RNA[c] for c in chain], sep="")
