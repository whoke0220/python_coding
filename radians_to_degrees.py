from math import pi

def radiansToDegrees(radians):
    degrees = radians * (180/pi)
    return degrees

rads = float(input("Enter the radians of the angle: "))

if not type(rads) is float:
    raise TypeError("Only float types are allowed.")

print(str(radiansToDegrees(rads)))

