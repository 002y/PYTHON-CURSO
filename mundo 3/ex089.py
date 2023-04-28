from time import sleep
from tqdm import tqdm

def long_running_function():
    for i in tqdm(range(100)):
        sleep(0.005)

print(' BOLETIM '.center(60, '='))

ficha = list()
verde = '\033[1;32;40m'
amarelo = '\033[1;33;40m'
azul = '\033[1;36;40m'
nulo = '\033[m'

while True:
    nome = str(input('nome: '))
    nota1 = float(input('primeira nota: '))
    nota2 = float(input('segunda nota: '))
    media = (nota1 + nota2) /2
    ficha.append([nome, [nota1, nota2], media])
    print('='*60)
    cont = ' '
    while cont not in 'SN':
        cont = str(input('quer continuar? ')).strip().upper()
        if cont == 'S':
            continue
        if cont == 'N':
            break
        else:
            print('opção invalida, tente novamente. ')
    if cont == 'N':
        break

print('='*30)
print(f'{azul} {"N°":<4} {amarelo} {"NOME":<11} {verde} {"MÉDIA":>7} {nulo}')
for c, a in enumerate(ficha):
    print(f'{ c:^4}   {a[0]:<7}  {a[2]:>11.1f}')

print('='*30)
while True:
    n = int(input('de qual aluno você quer ver a nota? [999: interrompe] '))
    if n == 999:
        print('finalizando...')
        sleep(2)
        break
    if n <= len(ficha) -1:
        long_running_function()
        print(f'as notas de {ficha[n][0]} são {ficha[n][1]}')
        print()

print('FIM')
