import random

f = 1
x = random.randint(0,500)

while f == 1:

    y = int(input("Vlož číslo:"))

    if x > y:
        print("x je větší")
    elif x < y:
        print("x je menší")
    else:
        print("Gratuluji, uhádl jsi to")
        quit()