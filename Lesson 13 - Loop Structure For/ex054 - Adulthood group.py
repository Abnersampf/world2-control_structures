from datetime import date

current_year = date.today().year

underage = 0
adult = 0

for c in range(1, 8):
    year = int(input(f'What year the {c}º person was born? '))
    if current_year - year < 18:
        underage += 1
    else:
        adult += 1

print(f'And also we had {adult} adult people')
print(f'In total we had {underage} underage people')
