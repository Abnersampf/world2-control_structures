print(f'''{'=' * 40}
{'SIGMA BANK':^40}
{'=' * 40}''')
# 50 20 10 1
banknotes = [50, 20, 10, 1]
count = 0
money = int(input('How much you want to withdraw? R$'))
rest = money
'''
1765 // 50 = 35
1765 % 50 = 15

15 // 20 = 0
15 % 20 = 15

15 // 10 = 1
15 % 10 = 5

5 // 1 = 5
5 % 1 = 0
'''
while True:
    num_of_banknotes = rest // banknotes[count]
    rest %= banknotes[count]
    if num_of_banknotes > 0:
        print(f'Total of {num_of_banknotes} banknotes of R${banknotes[count]}')
    count += 1
    if rest == 0:
        break
print('=' * 40)
print('Always come back to SIGMA BANK! Have a nice day!\n')
