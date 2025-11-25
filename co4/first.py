def area(length, breadth):
    return length * breadth

def perimeter(length, breadth):
    return 2 * (length + breadth)


import math

def area(radius):
    return math.pi * radius ** 2

def perimeter(radius):
    return 2 * math.pi * radius



def area(length, breadth, height):
    return 2 * (length * breadth + breadth * height + height * length)

def perimeter(length, breadth, height):
    return 4 * (length + breadth + height)


import math

def area(radius):
    return 4 * math.pi * radius ** 2

def perimeter(radius):
    return 2 * math.pi * radius  # Circumference


from graphics.rectangle import area as rect_area, perimeter as rect_perimeter
print("Rectangle Area:", rect_area(10, 5))
print("Rectangle Perimeter:", rect_perimeter(10, 5))

from graphics.circle import *
print("Circle Area:", area(7))
print("Circle Perimeter:", perimeter(7))



from graphics.graphics3d.sphere import area as sphere_area
print("Sphere Surface Area:", sphere_area(4))

