number = 1
odd = 0
even = 0
while number != 0:
    number = int(input('Enter a number: '))
    if number != 0:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
print(f'{odd} odd numbers were entered')
print(f'And {even} even numbers were entered')
print('End!')
