pesel = input('Enter your PESEL number: ')

if len(pesel) != 11:
    print('PESEL number must have 11 digits.')
elif not pesel.isdigit():
    print('PESEL number must contain only digits.')
print('Your PESEL number is correct.')

year = int(pesel[0:2])
month = int(pesel[2:4])
day = int(pesel[4:6])

if month >= 20 and month <= 32:
    year += 2000
    month -= 20
elif month >= 80 and month <= 92:
    year += 1800
    month -= 80
else:
    year += 1900

print(f'Your birth date is: {year}-{month:02d}-{day:02d}')