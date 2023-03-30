import time

odpovedi = ["Hola", "Já jsem Jerry.", "Komunikuju.", "Nevim", "Jsem starší jak Země.", "Doufám, že se uvidíme příště.", "Na tuto věc nedokážu odpovědět."]
otazky = ["Ahoj", "Jak se jmenuješ?", "Co děláš?", "Odkud jsi?", "Kolik ti je let?", "Čau"]
x = 0


def vypis(odpovedi):
    for i in range(len(odpovedi)):
        print(odpovedi[i], end='')
        time.sleep(0.2)
    print()


l = 1

print("Otázky: ", otazky)

while l == 1:
    otazka = input("Komunikuj: ")
    if otazka == "Ahoj":
        vypis(odpovedi[x])
    elif otazka == "Jak se jmenuješ?":
        x = 1
        vypis(odpovedi[x])
    elif otazka == "Co děláš?":
        x = 2
        vypis(odpovedi[x])
    elif otazka == "Odkud jsi?":
        x = 3
        vypis(odpovedi[x])
    elif otazka == "Kolik ti je let?":
        x = 4
        vypis(odpovedi[x])
    elif otazka not in otazky:
        x = 6
        vypis(odpovedi[6])
    elif otazka == "Čau":
        x = 5
        vypis(odpovedi[x])
        l = 0
      