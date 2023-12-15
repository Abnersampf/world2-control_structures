from random import randint

print(f'''{'=-' * 20}
{'LET\'S PLAY EVEN OR ODD':^40}
{'=-' * 20}''')

count = 0

while True:
    cpu_num = randint(0, 10)

    usr_num = int(input('Enter a number: '))
    usr_choice = input('Choose Even or Odd [E/O]: ').strip().upper()[0]

    while not (usr_choice in 'EO'):
        usr_choice = input('ERROR: INVALID OPTION! [E/O] ').strip().upper()[0]

    total = cpu_num + usr_num

    print(f'You choose {usr_num} and the computer choose {cpu_num}.')
    print(f'The total is {total}, a', end=' ')
    print('EVEN' if total % 2 == 0 else 'ODD', 'number')

    print('-' * 40)

    if total % 2 == 0 and usr_choice == 'E' or total % 2 != 0 and usr_choice == 'O':
        print('YOU WON!\nLet\'s play agin...')
        print('-' * 40)
        count += 1
    else:
        print('YOU LOSE!')
        break

print('=-' * 20)
print(f'GAME OVER! You won {count} times.')
