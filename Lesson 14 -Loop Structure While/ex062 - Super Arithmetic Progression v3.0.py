print('Arithmetic Progression Generator')
print('-=' * 16)

first_term = int(input('First term: '))
difference = int(input('Common difference: '))
n = 10
last_term = first_term + (n - 1) * difference

while first_term <= last_term:
    print(f'{first_term} ->', end=' ')
    first_term += difference

    if first_term > last_term:
        print('PAUSE')
        n = int(input('How many terms do you want to show more? '))
        last_term = first_term + (n - 1) * difference

        if n == 0:
            first_term = last_term + 1

print(f'Arithmetic Progression completed with', end=' ')
print(f'{(last_term // difference) + 1} terms shown')
