total = over1000 = 0

print(f'''{'-' * 40}
{'SUPER-CHEAP STORE':^40}
{'-' * 40}''')

while True:
    product_name = input('Product\'s name: ').strip().capitalize()
    product_price = float(input('Price: R$'))

    if total == 0 or product_price < cheapest_price:
        cheapest_name = product_name
        cheapest_price = product_price

    total += product_price

    if product_price > 1000:
        over1000 += 1

    continue_loop = input('Do you want to continue? [Y/N] ').strip().upper()[0]
    while continue_loop not in 'YN':
        continue_loop = input('ERROR! Enter Y or N: ').strip().upper()[0]

    if continue_loop == 'N':
        break

print(f'{' END OF PROGRAM ':-^40}')
print(f'The total purchase was R${total}')
print(f'We have {over1000} products costing more than R$1000.00')
print(f'The cheapest product was {cheapest_name} costing R${cheapest_price}')
