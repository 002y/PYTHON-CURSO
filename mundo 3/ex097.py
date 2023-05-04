def escreva(msg):
    tamanho = len(msg) + 4
    print('~'*tamanho)
    print(msg.center(tamanho, ' '))
    print('~'*tamanho)


for c in range(2):
    escreva(input('digite algo: '))
