import math

a=float(input("Enter side A: "))
b=float(input("Enter side B: "))

hypot = math.sqrt((a**2)+(b**2))
print("Hypotenuse is: ", round(hypot,2))