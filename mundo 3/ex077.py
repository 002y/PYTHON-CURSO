palavras = ('ESTUDAR',
           'PROGRAMAR',
           'PENSAR',
           'DEPRESSAO',
           'CHORAR',
           'DINHEIRO',
           'MONEY')

for c in palavras:
    print(f'\n em {c} temos:',end=' ')
    for letra in c:
        if letra in 'AEIOU':
            print(letra, end=' ')