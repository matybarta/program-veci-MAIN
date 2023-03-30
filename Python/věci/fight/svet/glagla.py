import os
from mapicka import Map
from char import Character

clear = lambda: os.system('cls')
clear()

Lake = Map("Zelené jezero", "Velké nádherné jezero s malým ostrůvkem nacházejícím se uprostřed tohoto jezera.")
City = Map("město Osvon", "Vidíš nápis s jménem města: Osvon. Toto město je hlavním městem malé země uprostřed kontinentu Jernom. Na první pohled si všimneš hradeb, které vypadají, že zde stojí již několik stovek let. U brány stojí desítky obchodníků, někteří se připravují na vstup do města a jiní se chystají na odchod.")
Intersection = Map("křižovatka", "Vidíš křižovatku, můžeš se vydat do čtyř směrů")
Mountain = Map("Diamond mountain", "Vidíš Diamantovou horu (Diamond mountain), celkově vypadá nádherně. +-400 metrů nad zemí se nachází jeskyně, ve které se údajně nachází černý drak Alphonso")
Village = Map("Vesnice Lain", "Vidíš malou vesničku Lain, vesnička je tvořená z 15 domů, z 1 knihovny a 1 radnice.")
Path = Map("Cesta", "Vidíš vyšlapanou cestičku, která tě někam zavede")

Lake.setPorts({"jih": Intersection, "východ": City, "západ": Village})
City.setPorts({"sever": Lake, "jih": Mountain, "západ": Intersection})
Intersection.setPorts({"sever": Lake, "jih": Mountain, "východ": City, "západ": Village})
Mountain.setPorts({"sever": Intersection, "východ": City, "západ": Village})
Village.setPorts({"sever": Lake, "jih": Mountain, "východ": Intersection})

choice = ""
position = Intersection

print("Udělej si postavu!")
hrac = Character(
    input("Jméno: "),
    int(input("Počet životů (číslo): ")),
    int(input("Kolik máš dexterity (číslo): ")),
    int(input("Kolik máš síly (číslo): ")),
    position
)
print("Pokud budeš potřebovat ukončit hru napiš: END")


print("Právě se nacházíš na křižovatce.")

while(choice != "END"):
    clear()
    print(hrac.place)
    position=hrac.place
    choice = input("Kam se chceš vydat? ")
    hrac.place=position.gate[choice]
