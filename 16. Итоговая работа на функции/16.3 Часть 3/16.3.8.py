from operator import add, sub, truediv, mul


def arithmetic_operation(operation):
    def f(x, y):
        ops = {"+": add, "-": sub, "/": truediv, "*": mul}
        return ops[operation](x, y)

    return f
