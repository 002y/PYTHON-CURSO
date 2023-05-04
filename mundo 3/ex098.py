from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('_--'*20)
    print(f'contagem de {i} até {f} de {p} em {p}')
    sleep(2)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ',end='')
            sleep(0.2)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ',end='')
            sleep(0.2)
            cont -= p
        print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)
print('_--'*20)
print('agora é a sua vez! ')
ini = int(input('inicio: '))
fim = int(input('fim: '))
passo = int(input('passo: '))
contador(ini, fim, passo)
