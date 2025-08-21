def print_products(*args):
    products = [i for i in args if type(i) is str and len(i) > 0]
    if len(products) == 0:
        print("Нет продуктов")
    else:
        num = 1
        for i in products:
            print(f"{num}) {i}", sep="\n")
            num += 1
