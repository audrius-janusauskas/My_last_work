import ipaddress

ivestis = int(input("Įveskite taškų skaičių: "))

sub_mask = "255.255.255"

ip = ipaddress.IPv4Address("192.168.2.1")

# Funkcija susijusi su IPv4 adresais.
def perf_24(x):
    return 1 * x
def perf_25(x):
    return 1 * x
def perf_26(x):
    return 128 + x
def perf_27(x, s):
    return 128 + x + s
def perf_28(x):
    return 128 + 64 + 32 + x
def perf_29(x):
    return 128 + 64 + 32 + 16 + x
def perf_30(x):
    return 128 + 64 + 32 + 16 + 8 + x

if ivestis <= 255 and ivestis > 128:
    print(f"ipv4 ruozas nuo {ip} - 254 / {sub_mask}.{perf_24(0)}")
elif ivestis <= 128 and ivestis > 64:
    print(f"ipv4 ruozas nuo {ip} - 126 / {sub_mask}.{perf_25(128)}")
elif ivestis <= 64 and ivestis > 32:
    print(f"ipv4 ruozas nuo {ip} - 62 / {sub_mask}.{perf_26(64)}")
elif ivestis <= 32 and ivestis > 16:
    print(f"ipv4 ruozas nuo {ip} - 30 / {sub_mask}.{perf_27(64, 32)}")
elif ivestis <= 16 and ivestis > 8:
    print(f"ipv4 ruozas nuo {ip} - 14 / {sub_mask}.{perf_28(16)}")
elif ivestis <= 8 and ivestis > 4:
    print(f"ipv4 ruozas nuo {ip} - 6 / {sub_mask}.{perf_29(8)}")
elif ivestis <= 4 and ivestis > 2:
    print(f"ipv4 ruozas nuo {ip} - 2 / {sub_mask}.{perf_30(4)}")
else:
    print("IPv4 ruozas nenaudojamas!!!")

# Funkcija susijusi su Prefix dalimi.
ivestis2 = int(input("Įveskite prefiksą: "))


def sub_24(x):
    return x * 10 + 14
def sub_25(x):
    return x * 5 + 1
def sub_26(x):
    return x * 2 + 10
def sub_27(x):
    return x - 13
def sub_28(x):
    return x - 22
def sub_29(x):
    return x - 25
def sub_30(x):
    return x - 28

if ivestis2 == 24:
    print(f"IPv4 adresų kiekis - {sub_24(24)}")
elif ivestis2 == 25:
    print(f"IPv4 adresų kiekis - {sub_25(25)}")
elif ivestis2 == 26:
    print(f"IPv4 adresų kiekis - {sub_26(26)}")
elif ivestis2 == 27:
    print(f"IPv4 adresų kiekis - {sub_27(27)}")
elif ivestis2 == 28:
    print(f"IPv4 adresų kiekis - {sub_28(28)}")
elif ivestis2 == 29:
    print(f"IPv4 adresų kiekis - {sub_29(29)}")
elif ivestis2 == 30:
    print(f"IPv4 adresų kiekis - {sub_30(30)}")
else:
    print("Toks IPv4 adresų kiekis neegzistuoja!!!")