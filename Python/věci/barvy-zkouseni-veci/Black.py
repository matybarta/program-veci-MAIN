seznam = [1,15,3,20]
def zdvojnasob(cisla):
    x = len(cisla)
    for i in range(0,x):
        cisla[i] = int(cisla[i])*2
    return cisla
        #print(cisla[i])

print(seznam)
zdvojnasob(seznam)

print(seznam)