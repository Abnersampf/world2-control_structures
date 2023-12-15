grade1 = float(input('First grade: '))
grade2 = float(input('Second grade: '))

average = (grade1 + grade2) / 2

print(f'With {grade1} and {grade2} the student\'s average is {average:.2f}')

if average < 5:
    print('The student has FAILED!')
elif average >= 7:
    print('The student has PASSED!')
else:
    print('The student is in REMEDIAL CLASSES!')
