number = int(input('Enter a number: '))
count = 0

for c in range(1, number + 1):
    if number % c == 0:
        count += 1
        print(f'\033[34m{c}\033[m', end=' ')
    else:
        print(f'\033[31m{c}\033[m', end=' ')

print(f'\nThe number {number} has {count} divisors')

print('That\'s why it\'s', end=' ')
if count == 2:
    print('a prime number!')
else:
    print('NOT a prime number!')
