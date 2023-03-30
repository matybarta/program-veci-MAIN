class Mobil:
    def __init__(self, znacka, pamet, os, vec):
        self.znacka = znacka
        self.pamet = pamet
        self.os = os
        self.vec = vec
    def je5Gcko(self, je5G, test):
        self.je5G = je5G
        self.test = test

mobil1 = Mobil("Motorola", "12GB", "Android", True)
mobil1.je5Gcko(True, False)
print(mobil1.je5G)
print(mobil1.znacka, mobil1.pamet)