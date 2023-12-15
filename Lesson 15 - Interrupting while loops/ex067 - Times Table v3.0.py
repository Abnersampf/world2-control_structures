while True:
    number = int(input('Type in number to see it\'s multiplication table? '))
    print('-' * 52)
    if number < 0:
        break
    for c in range(1, 11):
        print(f'{number} x {c:2} = {number * c:2}')
    print('-' * 52)
print('Program finished sucessfully!')
