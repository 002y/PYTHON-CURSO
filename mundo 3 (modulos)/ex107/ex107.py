from moeda import *
from time import sleep

while True:
    resposta = int(input('''CALCULADORA
  [1] aumentar
  [2] diminuir
  [3] dobro
  [4] metade
  [0] parar
  
  o que você quer fazer? '''))
    sleep(0.3)

    if resposta == 1:
        num_aumento = int(input('qual número você quer aumentar? '))
        aumento = int(input('qual vai ser a porcentagem? '))
        aum_resultado = aumentar(num_aumento, aumento)
        print(f'{num_aumento} sendo aumentado por {aumento}% é {aum_resultado}')

    elif resposta == 2:
        num_decrescimo = int(input('qual número você quer diminuir? '))
        decrescimo = int(input('qual vai ser a porcentagem? '))
        dec_resultado = diminuir(num_decrescimo, decrescimo)
        print(f'{num_decrescimo} sendo diminuido por {decrescimo}% é {dec_resultado}')

    elif resposta == 3:
        num_dobro = int(input('qual número você quer dobrar? '))
        dobro_resultado = dobro(num_dobro)
        print(f'o dobro de {num_dobro} é {dobro_resultado}')

    elif resposta == 4:
        num_metade = int(input('qual número você quer saber a metade? '))
        metade_resultado = metade(num_metade)
        print(f'a metade de {num_metade} é {metade_resultado}')

    if resposta == 0:
        break

    sleep(1)
    print('=-' * 30)
    print()
print('<<< FIM, VOLTE SEMPRE >>>')
sleep(4)
