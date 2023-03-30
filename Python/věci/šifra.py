sifra = input("Zadej šifru: ")
ascii_values = []
y = 0
for character in sifra:
    ascii_values.append(ord(character))
print(ascii_values)

for i in range(25):
    y = y + 1
    new_list = [x + y for x in ascii_values]
    for x in new_list:
        if x > 122:
            new_list[x] == 97
    #print(new_list)

    bagr = ''.join(chr(i) for i in new_list)
    print(bagr)
