"""TAKŽE... Tohle dalo zabrat víc než jsem čekal... Celkově jsem se pokusil vytvořit kopii Dungeons and Dragons (DnD, Dračí doupě, atd.).
   2 hráči hrajou proti sobě za 2 postavy... U každý postavy si nastaví vlastní jméno, počet životů, dexteritu která jim sníží šanci na trefu, strength neboli sílu která jim zváší poškození a na konec zbraň u které si nastaví pouze poškození.
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DŮLEŽITÉ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   PROSÍM O TO ABY MAXIMÁLNÍ HODNOTA DEXTERITY BYLA 20 JINAK SE HRA ROZBIJE A ÚTOKY NIKDY NEZASÁHNOU"""




import random

#Vytvoření postavy
class Postava:
    def __init__(self, jmeno, health, dexterity, strength, zbran):
        self.jmeno=jmeno
        self.health=health
        self.dexterity=dexterity
        self.strength=strength
        self.zbran=zbran



#Funkce na útok
def attack(Player):

    #hod "kostkou" aby se zjistilo jestli se trefí
    hit = random.randint(1,20)
    #Podmínka na to aby se zjistilo jestli útok zasáhl postavu
    if (hit > (10 + (Player1.dexterity // 4)) and Player == 1):
        print("Útok úspěšný!")
        damage = 0 + Player2.zbran + (Player2.strength // 4)
        if (damage > 0):
            Player1.health = Player1.health - damage
            print(Player1.jmeno, "má", Player1.health, "hp.")
        #Co se stane pokud nezasáhne
        else:
            print(Player1.jmeno, "neutržil žádné poškození.")

    #Podmínka na to aby se zjistilo jestli útok zasáhl postavu
    if (hit > (10 + (Player2.dexterity // 4)) and Player == 2):
        print("Útok úspěšný!")
        damage = 0 + Player1.zbran + (Player1.strength // 4)
        if (damage > 0):
            Player2.health = Player2.health - damage
            print(Player2.jmeno, "má", Player2.health, "hp.")
        else:
            print(Player2.jmeno, "neutržil žádné poškození")
    #Co se stane pokud nezasáhne
    else:
        print("Nezasáhl jsi.")

#vytvoření funkce na léčení
def heal(Player):

    #kolik si vyléčí zdraví (hp)
    healing = random.randint(1,10)

    #postava 1
    if (Player == 1):
        Player1.health = Player1.health + healing
        print(Player1.jmeno, "získal: ", healing, "hp.")
        print(Player1.jmeno, "má: ", Player1.health, "hp.")

    #postava 2
    elif (Player == 2):
        Player2.health = Player2.health + healing
        print(Player2.jmeno, "získal: ", healing, "hp.")
        print(Player2.jmeno, "má: ", Player2.health, "hp.")


#Nastavení postavy 1
print("Zde si nastavte postavu pro hráče 1")

#NASTAVOVÁNÍ
Player1 = Postava(
        input("Zadejte jméno postavy: "),
    int(input("Zadejte počet životů postavy: ")),
    int(input("Zadejte dexterity postavy: ")),    
    int(input("Zadejte strenght postavy: ")),
    int(input("Zadejte poškození zbraně: ")),
    )

#Nastavení postavy 1
print("Zde si nastavte postavu pro hráče 2")

#NASTAVOVÁNÍ
Player2 = Postava(
        input("Zadejte jméno postavy: "),
    int(input("Zadejte počet životů postavy: ")),
    int(input("Zadejte dexterity postavy: ")),    
    int(input("Zadejte strenght postavy: ")),
    int(input("Zadejte poškození zbraně: ")),
    )


#Cyklus aby mezi sebou bojovali
while(Player1.health > 0 and Player2.health > 0):
    #Vždy začíná postava 1
    print("Hraje", Player1.jmeno)
    delani = int(input("Co chce " + Player1.jmeno + " udělat? (1 - zaútočit, 2 - vyléčit se): "))
    if (delani == 1):
        attack(1)
        if (Player2.health <= 0):
            break
    elif (delani == 2):
        heal(1)

    #2. postava hraje
    print("Hraje", Player2.jmeno)
    delani = int(input("Co chce " + Player2.jmeno + " udělat? (1 - zaútočit, 2 - vyléčit se): "))
    if (delani == 1):
        attack(2)
        if (Player1.health <= 0):
            break
    elif (delani == 2):
        heal(2)


#UKONČENÍ HRY - Po smrti postavy
if(Player1.health > 0):
    print("\n", Player1.jmeno, "VYHRÁL!")
elif(Player2.health > 0):
    print("\n", Player2.jmeno, "VYHRÁL!")