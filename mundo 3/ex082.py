num = []
par = []
impar = []
print(' SEPARANDO VALORES DE UMA LISTA '.center(60, '='))
while True:
    n = int(input('digite um número: '))
    num.append(n)
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        impar.append(n)
    cont = str(input('quer continuar? [S/N]')).upper().strip()
    if cont != 'S':
        break
print('=' * 60)
print(f'números: {num}')
print(f'impar: {impar}')
print(f'par: {par}')
