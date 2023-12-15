print('=' * 40)
print(f'{'10 TERMS OF A A.P':^40}')
print('=' * 40)

first_term = int(input('First term: '))
pattern = int(input('Pattern: '))
last_term = first_term + (10 - 1) * pattern

for c in range(first_term, last_term + 1, pattern):
    print(f'{c} ->', end=' ')
print('Finished!')
