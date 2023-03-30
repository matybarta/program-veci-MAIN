#definování věcí
heslo = input("Zadejte heslo: ")
delka = len(heslo)
skore = 0
x = 0
y = 0
z = 0
j = 0
l = 0

#obsah listu
znaky = ["!", '"', "#", "$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~"]

#body za délku
if delka < 8:
    x = skore + 0
elif delka == 8:
    x = skore + 1
elif delka > 8:
    x = skore + delka - 7

#body za malá písmena
for malap in heslo:
    if malap.islower():
        y = skore + 10

#body za velká písmena
for velkap in heslo:
    if velkap.isupper():
        z = skore + 10
#body za čísla
for cisla in heslo:
    if cisla.isdigit():
        j = skore + 10

#body za spešl znaky
for veci in znaky:
    if veci in heslo:
        l = skore + 10


final_skore = x+y+z+j+l

#konečný výsledek
print(x, y, z, j, l)

if final_skore <= 20:
    print("Slabé heslo")
elif final_skore > 20 and final_skore < 43:
    print("Středně silné heslo")
elif final_skore >= 43:
    print("Silné heslo")
