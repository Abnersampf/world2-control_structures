number = int(input('Enter a number [999 to stop]: '))
quantity = total = 0
while number != 999:
    quantity += 1
    total += number
    number = int(input('Enter a number [999 to stop]: '))
print(f'You entered {quantity} numbers, and the sum of them was {total}')
