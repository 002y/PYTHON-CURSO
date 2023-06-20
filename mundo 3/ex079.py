lista = []
num_repetido = 0

print(' valores únicos em uma lista '.center(60, '='))
resp = 'S'
while resp == 'S':
    n = int(input('digite um número: '))
    if n not in lista:
        lista.append(n)
        print('valor adicionado com sucesso ')
    elif n in lista:
        num_repetido += 1
    resp = str(input('quer continuar? ')).upper().strip()

print('=' * 60)
lista.sort()
print(lista)
print(f'você digitou {num_repetido} números repetidos')
print('fim')
