from moeda import *
from time import sleep

while True:
    resposta = int(input('''CALCULADORA DE PREÇOS
  [1] aumentar
  [2] diminuir
  [3] dobro
  [4] metade
  [0] parar

  o que você quer fazer? '''))
    sleep(0.3)

    if resposta == 1:
        num_aumento = float(input('qual preço você quer aumentar? R$'))
        aumento = int(input('qual vai ser a porcentagem? '))
        aum_resultado = aumentar(num_aumento, aumento)
        print(f'{moeda(num_aumento)} sendo aumentado por {aumento}% é {moeda(aum_resultado)}')

    elif resposta == 2:
        num_decrescimo = float(input('qual preço você quer diminuir? R$'))
        decrescimo = int(input('qual vai ser a porcentagem? '))
        dec_resultado = diminuir(num_decrescimo, decrescimo)
        print(f'{moeda(num_decrescimo)} sendo diminuido por {decrescimo}% é {moeda(dec_resultado)}')

    elif resposta == 3:
        num_dobro = float(input('qual preço você quer dobrar? R$'))
        dobro_resultado = dobro(num_dobro)
        print(f'o dobro de {moeda(num_dobro)} é {moeda(dobro_resultado)}')

    elif resposta == 4:
        num_metade = float(input('qual preço você quer saber a metade? R$'))
        metade_resultado = metade(num_metade)
        print(f'a metade de {moeda(num_metade)} é {moeda(metade_resultado)}')

    sleep(1)
    print('=-' * 30)
    print()
    if resposta == 0:
        break

print('<<< FIM, VOLTE SEMPRE >>>')
sleep(4)
