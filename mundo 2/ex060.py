print('calculadora fatorial em python')
n = int(input('digite um número: '))
c = n
f = 1
print(f'{c}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
