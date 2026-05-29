from cmath import pi
r = float(input("Provide a radius: "))
v = round(4 * pi * r**3 / 3, 1)

print("The volume is: " + str(v))