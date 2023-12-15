segment1 = float(input('First segment: '))
segment2 = float(input('Second segment: '))
segment3 = float(input('Third segment: '))

print('The segments above ', end='')

if (segment1 + segment2 > segment3 and segment1 + segment3 > segment2 and
        segment2 + segment3 > segment1):
    print('can form a ', end='')
    if segment1 == segment2 == segment3:
        print('EQUILATERAL triangle')
    elif segment1 == segment2 or segment1 == segment3 or segment2 == segment3:
        print('ISOCELES triangle')
    else:
        print('SCALENE triangle')
else:
    print('cannot form a triangle')
