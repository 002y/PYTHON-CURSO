r1 = float(input('enter a value: '))
r2 = float(input('enter a value: '))
r3 = float(input('enter a value: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('these values can form a triangle ', end = '')
    if r1 == r2 == r3:
        print('EQUILATERAL')
    elif r1 != r2 != r3 != r1:
        print('SCALENE')
    else:
        print('ISOSCELES')
else:
    print('these values cannot form a triangle')
