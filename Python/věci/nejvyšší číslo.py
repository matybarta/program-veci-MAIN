import random

x = random.randint(0,100)
y = random.randint(0,100)
z = random.randint(0,100)

print("x:", x, "y:", y, "z:", z)

if (x > y) and (x > z):
    print("x je nejvyšší číslo:", x)
elif (y > x) and (y > z):
    print("y je nejvyšší číslo:", y)
elif (z > x) and (z > y):
    print("z je nejvyšší číslo:", z)
elif (x == y) and (x > z):
    print("x a y jsou nejvyšší:", x)
elif (x == z) and (x > y):
    print("x a z jsou nejvyšší:", x)
elif (y == z) and (y > x):
    print("y a z jsou nejvyšší:", y)
else:
    print("všechna čísla jsou stejně veliká:", x)
