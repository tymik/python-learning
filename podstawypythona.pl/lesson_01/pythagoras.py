import math
print('This program calculates the hypotenuse using Pythagorean theorem.')

a = float(input("Provide the length of the first adjoining: "))
b = float(input("Provide the length of the second adjoining: "))

c = math.sqrt(a**2 + b**2)

print(f'The hypotenuse for provided adjoinings equals: {c}')
