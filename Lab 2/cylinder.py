import math

r = int(input("Enter Radius: "))
h = int(input("Enter Height: "))

area = math.pi * r * r
vol = area * h

print("area:", area)
print("volume:", vol)