def matrix(n=None, m=None, value=None):
    if n is None:
        return [[0]]
    elif m is None and value is None:
        return [[0] * n for _ in range(n)]
    elif value is None:
        return [[0] * m for _ in range(n)]
    return [[int(value)] * m for _ in range(n)]
