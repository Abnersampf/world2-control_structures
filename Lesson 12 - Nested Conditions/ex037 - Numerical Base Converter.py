number = int(input('Enter any integer number: '))

print('''Choose one of the bases for the conversion:
[ 1 ] convert to binary
[ 2 ] convert to octal
[ 3 ] convert to hexadecimal''')

option = int(input('Your option: '))

print(f'{number} converted to', end=' ')

if option == 1:
    print(f'binary is {bin(number)}')
elif option == 2:
    print(f'octal is {oct(number)}')
elif option == 3:
    print(f'hexadecimal is {hex(number)}')
else:
    print(f'INVALID OPTION!!!')
