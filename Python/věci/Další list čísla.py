import math

#prostě nějaký list čísel, který se postupně zvětšuje
cisla = []
koren = 2
for i in range(5):
    cisla.append(koren)
    koren = koren ** 2

print(cisla)