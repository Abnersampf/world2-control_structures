total = 0
quantity = 0
for number in range(3, 496, 6):
    total += number
    quantity += 1
print(f'The sum of all {quantity} values requested is {total}')
