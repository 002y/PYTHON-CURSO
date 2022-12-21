from time import sleep
n1 = float(input('primeiro bimestre: '))
n2 = float(input('segundo bimestre: '))
n3 = float(input('terceiro bimestre: '))
n4 = float(input('quarto bimestre: '))
m = (n1 + n2 + n3 + n4)
sleep(0.4)
print('a sua media foi de : {}'.format(m))
if m >= 60:
    print('parabens!! você foi \033[1;32;40m APROVADO \033[m')
elif m < 60:
    print('você foi \033[1;30;41m REPROVADO \033[m :( seja mais inteligente' )
