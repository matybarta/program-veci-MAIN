
import os
from mapa import Mapa
from postava import Postava

les = Mapa("Temný les","Jsi v temné lese. Máš pocit že na tebe ze tmy koukají blyštivě bílé oči.")
pevnost = Mapa("Opuštěná pevnost", "Vidíš již před věky zbudovanou vojenskou pevnost.")
jezero = Mapa("Jezero", "Vidíš kříšťálově modré jezero jehož vody čeří vítr.")
cesta = Mapa("Cesta", "Vídíš vyšlapanou a vyježděnou prašnou cestu")
farma = Mapa("Farma", "Kousek před sebou vidíš nejspíše obydlenou farmu.")
zed = Mapa("Velká neviditelná zeď", "Kde nic tu nic - neprostupno.")

les.setbrana({"sever": pevnost, "jih":jezero, "zapad":cesta, "vychod": farma})
pevnost.setbrana({"sever":zed, "jih":les, "zapad":cesta, "vychod":zed})
jezero.setbrana({"sever": farma, "jih":zed, "zapad":cesta, "vychod": zed})
cesta.setbrana({"sever": pevnost, "jih":jezero, "zapad":zed, "vychod": les})
farma.setbrana({"sever": zed, "jih":jezero, "zapad":les, "vychod": zed})

volba  = ""
pozice = les

print("Právě jsi se probudil uprostřed temného lesa a nevíš co se stalo.\nTeď si můžeš nastavit svoje staty.")
hrac = Postava(
    input("Jméno:"),
    input("Počet životů:"),
    input("Počet síly:"),
    pozice
)
print("Pokud budeš chtít hru ukončit napiš: konec")


while(volba!="konec"):
    print(hrac.misto)
    pozice=hrac.misto
    volba=input("Kam chceš jít?\n")
    hrac.misto=pozice.brana[volba]
