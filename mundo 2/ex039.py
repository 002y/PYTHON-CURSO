from time import sleep
from datetime import date
now = date.today().year
print('     \033[7;30;42m ALISTAMENTO MILITAR  \033[m ')
print("=" * 35)
print(' ' * 1)
idade = int(input('em qual ano você nasceu? '))
y =  now - idade
print('aguarde...')
sleep(1)
print('...')
sleep(0.7)
print('...')
sleep(0.7)
print('...')
sleep(0.7)
if y == 18:
    print('quer jogar um free fire mais realista? kkkkkkkkkkkk')
elif y < 18:
    print('você fará o alistamento em {}'.format(idade + 18))
elif y > 18:
    print('a época do seu alistamento foi em {}'.format(idade + 18))
