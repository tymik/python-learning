import math

PI = 3.14

def distance(c1,c2):
    if c1 >= c2:
        return c1 - c2
    else:
        return c2 - c1

def radius(s1,s2):
    return math.sqrt(s1**2 + s2**2)/2

def area(r):
    return PI * r**2

print("Welcome to the Circle Area and Radius Calculator!")
print("This program calculates the area and radius of a circle.")
print("Please enter x1, x2, y1 and y2 co-ordinates of the segment ends.")

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

s1 = distance(x1,x2)
s2 = distance(y1,y2)

r = radius(s1,s2)
print(f'The radius of the circle is {r}')
print(f'The area of the circle is {area(r)}')