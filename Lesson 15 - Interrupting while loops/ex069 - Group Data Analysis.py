over18_people = total_men = under20_women = 0

while True:
    print('-' * 30)
    print(f'{'REGISTER A PERSON':^30}')
    print('-' * 30)

    age = int(input('Age: '))
    sex = input('Sex: [M/F] ').strip().upper()[0]

    while sex not in 'MF':
        sex = input('ERROR! Enter M or F: ').strip().upper()[0]

    if age > 18:
        over18_people += 1
    if sex == 'M':
        total_men += 1
    if age < 20 and sex == 'F':
        under20_women += 1

    print('-' * 30)

    continue_loop = input('Do you want to continue? [Y/N] ').strip().upper()[0]
    while continue_loop not in 'YN':
        continue_loop = input('ERROR! Enter Y or N: ').strip().upper()[0]

    if continue_loop == 'N':
        break

print(f'Total number of people over 18: {over18_people}')
print(f'In total we have {total_men} men registered')
print(f'And we have {under20_women} women under 20\n')
