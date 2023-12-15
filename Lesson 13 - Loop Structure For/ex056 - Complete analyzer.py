average_age = 0
oldest_man_age = 0
under20_women = 0

for person in range(1, 5):
    print(f'----{person}º PERSON----')

    name = input('Name: ').strip().capitalize()
    age = int(input('Age: '))
    sex = input('Sex [M/F]: ').strip().upper()

    average_age += age

    if age > oldest_man_age and sex == 'M':
        oldest_man_age = age
        oldest_man_name = name

    if age < 20 and sex == 'F':
        under20_women += 1

average_age /= 4

print(f'The average age of the group is {average_age:.1f}')
print(f'The oldest man is {oldest_man_age} years old and his name is', end=' ')
print(oldest_man_name)
print(f'There are a total of {under20_women} women under the age of 20')
