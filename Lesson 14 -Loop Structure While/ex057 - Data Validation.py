sex = input('Enter your gender: [M/F] ').strip().upper()
while not (sex in 'MF'):
    sex = input('Invalid gender! Please, enter a valid gender: ')
print(f'The sex {sex} was registered with sucess!')
