weight = float(input('How much do you weight? (Kg) '))
height = float(input('How tall are you? (m) '))

bmi = weight / pow(height, 2)

print(f'The BMI of this person is {bmi:.2f}')

if bmi < 18.5:
    print('Underweight')
elif bmi < 25:
    print('Ideal weight')
elif bmi < 30:
    print('Overweight')
elif bmi < 40:
    print('Obesity')
else:
    print('You\'re gonna DIE!!!')
