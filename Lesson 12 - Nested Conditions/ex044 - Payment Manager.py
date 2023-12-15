print(f'{'=' * 10} SIGMA STORE {'=' * 10}')

price = float(input('Price of purchases: R$'))

print('''PAYMENT METHODS
[ 1 ] Sight in cash/check
[ 2 ] Cash on card
[ 3 ] 2x on card
[ 4 ] 3x or more on card''')

option = int(input('Choose an option: '))

print(f'Your purchase of R${price} will cost', end=' ')
if option == 1:
    print(f'R${price - (price * 0.10)} with this payment method')  # 10% off
elif option == 2:
    print(f'R${price - (price * 0.05)} with this payment method')  # 5% off
elif option == 3:
    print('the same price with this payment method')  # no discount
    print(f'The price of each installment will be {price / 2:.2f}')
elif option == 4:
    total = price * 1.20
    print(f'R${total} with this payment method')  # 20% interest
    installments = int(input('How many installments will be? '))
    print(f'The price of each installment will be {total / installments:.2f}')
else:
    print('INVALID OPTION!!!')
