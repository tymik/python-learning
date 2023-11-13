def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

while True:
    user_input = input("Enter 1 to convert from Celsius to Fahrenheit, 2 to convert from Fahrenheit to Celsius: ")
    if user_input == '1':
        celsius = float(input("Enter Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f'{celsius} Celsius equals {fahrenheit} Fahrenheit')
        break
    elif user_input == '2':
        fahrenheit = float(input("Enter Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f'{fahrenheit} Fahrenheit equals {celsius} Celsius')
        break
    else:
        print('Invalid input. Please enter 1 or 2.')

print('Thanks, Goodbye!')
