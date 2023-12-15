total = 0
for c in range(0, 3):
    number = int(input('Enter a number: '))
    total += number
print(f'{'=' * 10} outside for loop {'=' * 10}')
print(f'Total: {total}')
print('End!')
