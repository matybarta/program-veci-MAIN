#vypíše číslo ze seznamu, který mají zbytek po dělení 0

#definování seznamu
seznam = [10, 21, 4, 45, 66, 93]

#vytovření cyklu na prohledání seznamu
for cislo in seznam:
 
 #Vytvoření podmínky, když číslo po dělení 2 má nulový zbytek tak ho nechá v seznamu
    if cislo % 2 == 0:
        #vypíše čísla která mají zbytek 0
        print(cislo, end=" ")