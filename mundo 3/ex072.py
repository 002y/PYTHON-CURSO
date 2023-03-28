from time import sleep


print('número por extenso ')
números = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco',\
          'seis', 'sete', 'oito', 'nove', 'dez',\
          'onze', 'doze', 'treze', 'quatorze', 'quinze',\
          'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:
    n = int(input('digite um número de 0 a 20: '))
    if n >= 0 and n <= 20:
        sleep(0.5)
        print(números[n])
    else:
        print('número inválido, tente novamente ')
        continue

    resposta = str(input('deseja continuar? (S/N) ')).strip().upper()
    while resposta != 'S' and resposta != 'N':
        print('Resposta inválida. Por favor, digite: (S ou N)')
        resposta = str(input('Deseja continuar? (S/N) ')).strip().upper()

    if resposta == 'N':
        print('encerrando o programa...')
        sleep(1)
        break
    elif resposta == 'S':
        print('continuando o programa... ')
        sleep(1)


print('FIM')