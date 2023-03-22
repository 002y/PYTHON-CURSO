from time import sleep
n1 = int(input('escreva o primeiro número: '))
n2 = int(input('escreva o segundo número: '))
opção = 0
while opção != 5:
    print('=' * 45)
    r = int(input('''o que você deseja fazer com esses números?
    [1] somar 
    [2] multiplicar
    [3] maior 
    [4] novos números 
    [5] sair do programa 
    
    R: '''))
    if r == 1:
        s = n1 + n2
        print(f'{n1} + {n2} = {s}')
    elif r == 2:
        s = n1 * n2
        print(f'{n1} x {n2} = {s}')
    elif r == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}')
    elif r == 4:
        n1 = int(input('imforme novamente o primeiro número: '))
        n2 = int(input('informe novamente o segundo número: '))
    elif r == 5:
        print(' ')
        print('\033[32;40;2m FIM DO PROGRAMA \033[m')
        break
    else:
        print('opção inválida. tente novamente')
    print('=' * 45)
    sleep(2)