# Слияние словарей 🌶️
def merge(values):  # values - это список словарей
    data = {}
    for d in values:
        for key in d:
            data.setdefault(key, set()).add(d[key])
    return data
