azul = '\033[1;34;40m'
vermelho = '\033[1;31;40m'
nulo = '\033[m'

print(f'{vermelho} loja de canecas {nulo}')
contador = 0
produtos = ('copo dev', 16.00,
           'copo geek', 20.00,
           'caneca dev', 40.00,
           'caneca geek', 50.00)


for c in produtos:
    print(f'{azul} {c}',end='')

    contador += 1
    if contador == 2:
        print('R$')
        print(end='')
        contador = 0

