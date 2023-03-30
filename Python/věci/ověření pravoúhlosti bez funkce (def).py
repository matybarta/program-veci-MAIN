import math as m

#Ověření pravoúhlosti trojúhelníku V1
a = float(input("Vlož stranu a: "))
b = float(input("Vlož stranu b: "))
c = float(input("Vlož stranu c: "))

cisla = [a, b, c]

#seřazení
cisla.sort(reverse=True)

print(cisla)

#haha pythagoras

p1 = m.pow(cisla[1], 2) + m.pow(cisla[2], 2)
p2 = m.pow(cisla[0], 2)

print(p1)
print(p2)

if p1 == p2:
    print(bool())
else:
    print("Trojúhelník není pravoúhlý")
