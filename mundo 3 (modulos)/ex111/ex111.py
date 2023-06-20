from ultilidadesCev.moeda import *
from time import sleep

while True:
    resposta = int(input('''CALCULADORA DE PREÇOS
  [1] aumentar
  [2] diminuir
  [3] dobro
  [4] metade
  [5] resumo
  
  [0] parar

  o que você quer fazer? '''))
    sleep(0.3)

    if resposta == 1:
        num_aumento = float(input('qual preço você quer aumentar? R$'))
        aumento = int(input('qual vai ser a porcentagem? '))
        aum_resultado = aumentar(num_aumento, aumento, True)
        print(f'{moeda(num_aumento)} sendo aumentado por {aumento}% é {aum_resultado}')


    elif resposta == 2:
        num_decrescimo = float(input('qual preço você quer diminuir? R$'))
        decrescimo = int(input('qual vai ser a porcentagem? '))
        dec_resultado = diminuir(num_decrescimo, decrescimo, True)
        print(f'{moeda(num_decrescimo)} sendo diminuído por {decrescimo}% é {dec_resultado}')

    elif resposta == 3:
        num_dobro = float(input('qual preço você quer dobrar? R$'))
        dobro_resultado = dobro(num_dobro)
        print(f'o dobro de {moeda(num_dobro)} é {moeda(dobro_resultado)}')

    elif resposta == 4:
        num_metade = float(input('qual preço você quer saber a metade? R$'))
        metade_resultado = metade(num_metade)
        print(f'a metade de {moeda(num_metade)} é {moeda(metade_resultado)}')

    elif resposta == 5:
        preco = float(input('qual é o preço? R$'))
        preco_aum =int(input('qual será o aumento? '))
        preco_dec = int(input('qual será o decrescimo? '))
        resum = resumo(preco, preco_aum, preco_dec)
        print(f'  aumento: \t{resum[0]} \n  decresc: \t{resum[1]} \n  dobro: \t{resum[2]} \n  metade: \t{resum[3]}')

    sleep(1)
    print('=-' * 30)
    print()
    if resposta == 0:
        break

print('<<< FIM, VOLTE SEMPRE >>>')
sleep(4)
