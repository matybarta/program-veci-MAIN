class Map:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.gate={}
    
    def setPorts(self, gate):
        self.gate = gate

    def __str__(self):
        vypis = f"Místo: {self.name}\n Popis: {self.description}\n"" Vidíš: "
        
        for direction in self.gate:
            vypis += f"\n\t{direction}: {self.gate[direction].name},"
            
        return vypis + "\n"
