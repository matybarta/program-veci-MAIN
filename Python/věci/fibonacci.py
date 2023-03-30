#Definuju si, kolik čísel chci
x = int(input("Vlož kolik fibonacciho čísel chceš: "))

#Fibonacciho posloupnost done
cisla = [0,1]
for i in range(x):
    dalsi = cisla[i] + cisla[i+1]
    cisla.append(dalsi)

print(cisla)