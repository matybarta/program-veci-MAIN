class Mapa:
    def __init__(self, jmeno, popis):
        self.jmeno=jmeno
        self.popis=popis
        self.brana={}

    def __str__(self):
        vypis = f"Místo: {self.jmeno}\n Popis: {self.popis}\n"" Vidíš: "
        
        for smer in self.brana:
            vypis += f"\n\t{smer}: {self.brana[smer].jmeno},"
            
        return vypis + "\n"
    
    def setbrana(self, brana):
        self.brana=brana
