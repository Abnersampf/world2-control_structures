name = input('Enter your name: ').capitalize()

if name == 'Abner':
    print('Sigma detected!')
elif name == 'Abimael' or name == 'Davi' or name == 'Jhonata':
    print('Alpha detected!')
elif name in 'Enzo Lorenzo Gabriel Thiago':
    print('\033[35mGay confirmed!!!!\033[m')
else:
    print('Beta detected!!!')
