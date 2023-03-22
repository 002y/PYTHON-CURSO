from random import randint
cpu = randint(0, 10)
tentativas = 0
certo = False
while not certo:
    p1 = int(input('digite um número [0 > 10] : '))
    tentativas += 1
    if cpu == p1:
        certo = True
    else:
        if p1 < cpu:
            print('mais... tente novamente ')
        elif p1 > cpu:
            print('menos... tente novamente ')
print('=' * 40 )
if tentativas < 5:
    print(f'''              \033[1;33;40m PARABÉNS!! \033[m
    você acertou com {tentativas} tentativas!''')
else:
    print(f'você acertou com {tentativas} tentativas, boa sorte na proxima')
