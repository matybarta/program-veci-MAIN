cisla = open("cisla.txt", "w")
cisla.write("1, ")
cisla.write("2, ")
cisla.write("3, ")
cisla.write("4, ")
cisla.write("5")
cisla.close()


cisla = open("cisla.txt", "r")
print(cisla.read())
cisla.close()