# Сортировка IP-адресов
def dip(ip):
    return sum([list(map(int, ip.split(".")))[i] * 256 ** (3 - i) for i in range(4)])


ips = [input() for _ in range(int(input()))]
print(*sorted(ips, key=dip), sep="\n")
