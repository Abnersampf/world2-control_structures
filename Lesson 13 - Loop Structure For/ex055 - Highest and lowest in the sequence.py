highest = 0
for person in range(1, 6):
    weight = float(input(f'Weight of the {person}º person: '))
    if person == 1:
        lowest = weight
    if weight > highest:
        highest = weight
    if weight < lowest:
        lowest = weight
print(f'The highest weight read was {highest}Kg')
print(f'The lowest weight read was {lowest}Kg')
