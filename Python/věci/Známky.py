import random
#Vytvořeno s menší pomocí internetu (vyhledávání co dělají některé věci)

#vytvoření seznamu a definování x
znamky = []
x = random.randint(1,15)

#vvoření rozmezího, kolik čísel bude v listu a vložení čísel do listu
for i in range(0,x):
    y = random.randint(1, 5)
    znamky.append(y)

#definování celkového součtu čísel v listu a kolik čísel je v listu
celkem = sum(znamky)
pocet = len(znamky)

#vypsání listu, celkového počtu čísel, kolik čísel je v listu a průměr známkek
print("v listu je:", znamky)
print("celkový součet čísel v listu:", celkem)
print("kolik čísel je v listu:", pocet)
print("průměr je:", celkem/pocet)


