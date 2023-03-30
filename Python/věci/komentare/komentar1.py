#rozdělí string tak, aby se každé slovo se sudým počtem znaků napsalo na každý nový řádek

#definování stringu jako n
n = "Toto je programovací jazyk Python"

#definování slova jako rozdělení stringu n 
slova = n.split(" ")

#vytvoření cyklu, který zjistí kolik je písmen v 1 slově u stringu
for i in slova:
  #podmínka která říká: pokud počet písmen je sudý napiš je
  if len(i)%2==0:
    #vypsání slova který má sudý počet znaků
    print(i)