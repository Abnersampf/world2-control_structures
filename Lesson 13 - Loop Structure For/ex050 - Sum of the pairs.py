sum_of_even = 0
for c in range(0, 6):
    number = int(input('Enter a number: '))
    if number % 2 == 0:
        sum_of_even += number
print(f'The sum of all even numbers entered is {sum_of_even}')
