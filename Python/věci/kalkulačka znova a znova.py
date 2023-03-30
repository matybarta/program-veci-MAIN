import math as m


i = 1

while i == 1:
    x = float(input("Zadejte x: "))
    y = float(input("Zadejte y: "))
    p1 = input("Jakou operaci chcete provést? (scitat, odecist, nasobit, delit, odmocnit, mocnit): " )
    if p1 == "scitat":
        print(x + y)
    elif p1 == "odecist":
        print(x - y)
    elif p1 == "nasobit":
        print(x * y)
    elif p1 == "delit":
        if y == 0:
            print("Nelze")
        else:
            print(x / y)
    elif p1 == "odmocnit":
        z = float(input("Zadejte odmocninu : "))
        print(m.pow(x, 1/z))
    elif p1 == "mocnit":
        z = int(input("Zadejte mocninu: "))
        print(m.pow(x, z))


    opak = input("Chcete pokračovat? Ano/Ne: ")
    if opak == "Ne":
        i = 0