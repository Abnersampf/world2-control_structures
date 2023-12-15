total = count = 0
while True:
    number = int(input('Enter a number (999 to stop): '))
    if number == 999:
        break
    total += number
    count += 1
print(f'The sum of all {count} numbers was {total}!')
