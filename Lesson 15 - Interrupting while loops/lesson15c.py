total = 0
while True:
    number = int(input('Enter a number: '))
    if number == 999:
        break
    total += number
print(f'Total: {total}')
