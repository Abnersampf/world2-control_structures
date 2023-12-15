from time import sleep

number1 = int(input('First number: '))
number2 = int(input('Second number: '))

close = False

while not close:
    print('''    [ 1 ] Sum
    [ 2 ] Multiplication
    [ 3 ] Biggest
    [ 4 ] New numbers
    [ 5 ] Close the program''')
    option = input('>>>>> What\'s your option? ')

    if option == '1':
        print(f'\nThe sum of {number1} + {number2} is {number1 + number2}')

    elif option == '2':
        print(f'\nThe result of {number1} x {number2} is {number1 * number2}')

    elif option == '3':
        print(f'\nBetwen {number1} and {number2} the biggest value', end=' ')
        print(f'is {max(number1, number2)}')

    elif option == '4':
        print('\nEnter the numbers agin:')
        number1 = int(input('First number: '))
        number2 = int(input('Second number: '))
        sleep(1)

    elif option == '5':
        close = True
        print('\nClosing...')
        sleep(1)

    else:
        print('\nERROR. Invalid option! Try agin')
    print('=-=' * 10)

print('Program successfully closed!')
