from random import choice
from time import sleep

options = ['Rock', 'Paper', 'Scissors']
print(f'OPTIONS: {options}')

computer_choice = choice(options)
print('The computer has already choosen an object...\n')

user_choice = input('Which object will you choose: ').strip().capitalize()

sleep(0.5)
print('\nJO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!\n')
sleep(0.5)

print(f'''The COMPUTER chose {computer_choice}
YOU chose {user_choice}
''')

if (user_choice == 'Rock' and computer_choice == 'Scissors' or
    user_choice == 'Paper' and computer_choice == 'Rock' or
        user_choice == 'Scissors' and computer_choice == 'Paper'):
    print('YOU WON!!!')
elif user_choice == computer_choice:
    print('DRAW')
else:
    print('YOU LOSE!')
