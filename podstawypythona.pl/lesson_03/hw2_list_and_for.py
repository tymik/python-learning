import random

numbers = []

for i in range(10):
    numbers.append(random.randint(1,1000000))

numbers_4_6 = []

for number in numbers:
    if (number % 4 == 0) or (number % 6 == 0):
        numbers_4_6.append(number)

print(numbers)
print(numbers_4_6)