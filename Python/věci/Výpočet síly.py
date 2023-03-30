g = 9.81
m = float(input("Vložte hmotnost v kg: "))
F = m*g

print(F, "N - Newton")

if F<1:
    print(F*1000, "mN - Milinewton")
elif F>1000:
    print(F/1000, "kN - Kilonewton")
    quit()