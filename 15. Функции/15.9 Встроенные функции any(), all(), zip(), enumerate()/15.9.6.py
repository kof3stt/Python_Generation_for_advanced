# Хороший пароль
pas = input()
print(
    "YES"
    if all(
        (
            any(map(str.islower, pas)),
            any(map(str.isupper, pas)),
            any(map(str.isdigit, pas)),
            any(map(str.isalpha, pas)),
            len(pas) >= 7,
        )
    )
    else "NO"
)
