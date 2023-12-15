number = int(input('Enter a number to see it\'s factorial: '))

factorial = 1

while number != 0:
    factorial *= number

    print(number, end=' ')
    print('x' if number > 1 else '=', end=' ')

    number -= 1

print(factorial)
