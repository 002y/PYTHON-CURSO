from time import sleep

def maior(* val):
    print('analizando os valores...')
    sleep(2)
    print(f'foram digitados {len(val[0])} números ')
    print(f'o maior valor é: {max(val[0])}')


n = int(input('digite números: ')), int(input('digite números: ')), int(input('digite números: ')), int(input('digite números: ')), int(input('digite números: '))
maior(n)
