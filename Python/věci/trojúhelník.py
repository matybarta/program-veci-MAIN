#Jsem hloupej na tohle... Ale snad funguje...
#Sestrojení trojúhelníka V3.1
a = float(input("Vlož stranu a: "))
b = float(input("Vlož stranu b: "))
c = float(input("Vlož stranu c: "))

if (a+b > c) and (a+c > b) and (b+c > a):
    print("Může být sestrojen")
else:
    print("nemůže být sestrojen")