from random import randint
com = randint(1, 3)
print(''' 
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
''')
p1 = int(input('escolha um numero: '))
print('computador jogou: {}'.format(com))
print('você jogou: {}'.format(itens[p1]))
if com == p1:
    print('EMPATE!!')
if p1 == 1: # pedra
    if com == 2:
        print("COMPUTADOR GANHOU")
    if com == 3:
        print("PLAYER GANHOU")
elif p1 == 2: # papel
    if com == 3:
        print("COMPUTADOR GANHOU")
    if com == 1:
        print("PLAYER GANHOU")
else: #tesoura
    if com == 1:
        print("COMPUTADOR GANHOU")
    if com == 2:
        print("PLAYER GANHOU")
