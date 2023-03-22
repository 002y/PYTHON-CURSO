from random import randint
from time import sleep
cpu = randint(0, 11)
vitory = 0

while True:
    print('-=' * 15)
    player = int(input('digite um número: '))
    chosen = str(input('impar ou par? [I/P] ')).upper().strip()[0]
    num = cpu + player

    print(f'o número escolhido pelo cpu foi {cpu}')

    print ('processando, aguarde ', end='')
    sleep(1)
    print('.', end='')
    sleep(1)
    print('.', end='')
    sleep(1)
    print('.')
    sleep(0.5)

    if (num%2) == 0: # se for par
        if chosen == 'P':
            print('\033[1;32;40m VOCÊ GANHOU! \033[m')
        elif chosen == 'I':
            print('\033[1;31;40m VOCÊ PERDEU! \033[m')
            break

    else: # se não for par
        if chosen == 'P':
            print('\033[1;31;40m VOCÊ PERDEU! \033[m')
            break
        elif chosen == 'I':
            print('\033[1;32;40m VOCÊ GANHOU! \033[m')

    vitory += 1
print(f'a quantidade de vitorias foram {vitory}')
print('FIM')
