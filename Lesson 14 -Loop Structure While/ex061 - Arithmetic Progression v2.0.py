print('Arithmetic Progression Generator')
print('-=' * 16)

first_term = int(input('First term: '))
difference = int(input('Common difference: '))
term = first_term
last_term = first_term + (10 - 1) * difference

while term <= last_term:
    print(f'{term} ->', end=' ')
    term += difference

print('End')
