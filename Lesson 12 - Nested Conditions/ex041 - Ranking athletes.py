from datetime import date

year_of_birth = int(input('Year of birth: '))
age = date.today().year - year_of_birth

print(f'The athlete is {age} years old.')
print('Rank:', end=' ')

if age <= 9:
    print('Young')
elif age <= 14:
    print('Infant')
elif age <= 19:
    print('Junior')
elif age <= 25:
    print('Senior')
else:
    print('Master')
