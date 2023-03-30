import math as m

def prav_uhel():
    a = float(input("Vlož stranu a: "))
    b = float(input("Vlož stranu b: "))
    c = float(input("Vlož stranu c: "))

    cisla = [a, b, c]


    cisla.sort(reverse=True)

    print(cisla)

    if (m.pow(cisla[1], 2)+m.pow(cisla[2], 2)==m.pow(cisla[0],2)):
        return "Trojúhelník je pravoúhlý"
    else:
        return "Trojúhelník není pravoúhlý"

print(prav_uhel())