quantity = average = 0

continue_loop = 'Y'

while continue_loop == 'Y':
    number = int(input('Enter a number: '))

    quantity += 1
    average += number

    if quantity == 1:
        highest_number = lowest_number = number

    if number > highest_number:
        highest_number = number

    if number < lowest_number:
        lowest_number = number

    continue_loop = input('Do you want to continue? [Y/N] ').strip().upper()[0]

average /= quantity

print(f'You entered {quantity} numbers, and the average was', end=' ')
print(f'{average:.2f}')
print(f'The highest value was {highest_number} and the lowest was', end=' ')
print(lowest_number)
