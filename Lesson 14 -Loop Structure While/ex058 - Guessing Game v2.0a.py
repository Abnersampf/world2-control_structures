from random import randint
computer_choice = randint(1, 10)
print('''I'm your computer...
I just thought of a number bewtwen 1 to 10.
Can you guess which one it was?\n''')

user_choice = int(input('What\'s your guess: '))
attempts = 1

while user_choice != computer_choice:
    if user_choice < computer_choice:
        print('\nMore...Try one more time.')
    else:
        print('\nLess...Try one more time.')

    user_choice = int(input('What\'s your guess? '))
    attempts += 1

print(f'\nYou guess with {attempts} attempts. Congratulations!')
