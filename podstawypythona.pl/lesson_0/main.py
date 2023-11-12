first_name = input('Jak masz na imię? ')
age = int(input('Ile masz lat? '))

print(f'Hello {first_name}!')
print(f'Mam {age} lata.')

if first_name == 'Jan':
    print('Elo ziom!')
else:
    print('Miło mi Cię poznać!')

if age >= 18:
    print('Jesteś pełnoletni')
else:
    print('Jeszcze musisz poczekać')
    print(f'{18 - age} lat.')
