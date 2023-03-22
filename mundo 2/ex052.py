n = int(input('digite um número: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[m o número {n} foi divisivel {total} vezes ')
if total == 2:
    print('ele é um número primo')
else:
    print('ele não é um número primo ')
