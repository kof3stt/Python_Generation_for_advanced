# Уникальные символы 1
print(*[len(set(input().lower())) for _ in range(int(input()))], sep="\n")
