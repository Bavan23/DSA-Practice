import math

radius = float(input("Enter The radius of the circle: "))

circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f"\nCircumference of the Circle is {round(circumference,2)}\nArea of the Circle is {round(area,2)}")