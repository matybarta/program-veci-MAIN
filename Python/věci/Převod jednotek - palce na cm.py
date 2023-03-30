cm = float(input("Vlož délku: "))
inch = 2.54

prevod = input("Chcete převést z cm na palce? Ano/Ne: ")

if prevod == "Ano":
    print(cm/inch)
    quit()
elif prevod == "Ne":
    prevod2 = input("Chcete převést z palců na cm? Ano/Ne: ")
    if prevod2 == "Ano":
        print(cm*inch)
        quit()
    else:
        print("Nic se nestalo.")
        quit()
