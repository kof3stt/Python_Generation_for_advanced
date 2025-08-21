def mean(*args):
    total_sum = sum([arg for arg in args if type(arg) in (int, float)])
    total_count = len([arg for arg in args if type(arg) in (int, float)])
    if total_count != 0:
        return total_sum / total_count
    return 0
