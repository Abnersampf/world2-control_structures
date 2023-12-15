print(f'''{'-' * 37}
Fibonacci Sequence
{'-' * 37}''')

number_of_terms = int(input('How many terms do you want to see? '))
print('~' * 37)

previous_term = 0
next_term = 1

while number_of_terms != 0:
    print(f'{previous_term} ->', end=' ')

    next_term += previous_term
    previous_term = next_term - previous_term

    number_of_terms -= 1

print('End')