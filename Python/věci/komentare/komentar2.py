#vytiskne string kterýmu se odstraní 7 písmeno

#definování stringu test_str
test_str = "Na blbosti mě užije"

#vytvoření prázdného stringu
new_str = ""

#vytvoření cyklu, který zjistí jak dlouhý je string a následně odstraní 7 písmeno
for i in range(len(test_str)):
    #podmínka která říká, že pokud se odstraní 7 písmeno tak "new_str" bude spojením "new_str" a "test_str[i]"
    if i != 7:
        #vytvoření new_str, který bude vzniknutý spojením "new_str" a "test_str[i]"
        new_str = new_str + test_str[i]

#vytištění nového stringu
print ("Řetězec po odstranění konkrétního znaku : " + new_str)