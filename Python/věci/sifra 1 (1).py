sifra= input("Zadej šifru: ")
ascii_values = []
y=0
x=0
new_list= []

for character in sifra:
    ascii_values.append(ord(character))
    

ascii_values2=ascii_values
for i in range(20):
    
    y=y+1
    new_list= [x+y for x in ascii_values]
    
    for i in range(100):
        maximum= int(max(new_list))
        ulozna=0
        maximumascii= int(max(ascii_values2))
        f= new_list.index(maximum)
        if maximum>122:
            ulozna= maximum-122+96
            
            new_list.insert(f, ulozna)
            new_list.remove(maximum)
    vysledek = (''.join(chr(i) for i in new_list))
    print(vysledek.replace(",", " "))
odpoved= input("Zadejte správnou odpověď:")
print(odpoved)
    
    
