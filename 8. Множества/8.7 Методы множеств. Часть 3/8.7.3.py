# Урок информатики 👨‍💻
print(
    *sorted(
        set(input().split()) & set(input().split()) - set(input().split()),
        reverse=True,
        key=int,
    )
)
