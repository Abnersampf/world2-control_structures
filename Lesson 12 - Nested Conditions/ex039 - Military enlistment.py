from datetime import date

year_of_birth = int(input('Year of birth: '))
current_year = date.today().year
age = current_year - year_of_birth

print(f'Those born in {year_of_birth} will be {age} in {current_year}')

if age < 18:
    print(f'There are still {18 - age} years to go untill enlistment')
elif age > 18:
    print(f'You should have enlisted {age - 18} years ago')
else:
    print('You have to enlist IMMEDIATELY!!!')
