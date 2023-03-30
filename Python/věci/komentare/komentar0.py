#vytiskne nejvyšší číslo v seznamu

#vytvoření funkce nejvetsi
def nejvetsi(pole, n):
    #definuje max jako seznam s názvem pole
    max = pole[0]
    #vytvoření cyklu, který zjistí jaká je největší hodnota v nějakém seznamu
    for i in range(1, n):
        #podmínka která říká, že pokud hodnota v seznamu je vyšší jak max změní se max na i
        if pole[i] > max:
            #max se definuje jako pole[i]
            max = pole[i]
    #vrátí max
    return max

#vytovření seznamu arr
arr = [10, 324, 45, 90, 9808]
#definuje n jako délku seznamu arr
n = len(arr)
#definuje vysledek jako funkci nejvetsi
vysledek = nejvetsi(arr, n)
#vytiskne string "Největší v daném poli" a hned za to vysledek (to co je hned nad timhle)
print("Největší v daném poli ", vysledek)