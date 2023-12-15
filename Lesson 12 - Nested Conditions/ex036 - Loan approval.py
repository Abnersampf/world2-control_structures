price = float(input('House price: R$'))
salary = float(input('Buyer\'s salary: R$'))
years_of_funding = int(input('How many years of funding? '))

installment = price / (years_of_funding * 12)

print(f'To pay for an R${price:.2f} house in {years_of_funding}', end=' ')
print(f'years, the installment will be R${installment:.2f}')

if installment > salary * 0.3:
    print('Loan DENIED!')
else:
    print('Loan CAN BE GIVEN!')
