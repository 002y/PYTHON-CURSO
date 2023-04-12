lista = []
Cnúmrep = 0

print(' valores únicos em uma lista '.center(60, '='))
resp = 'S'
while resp == 'S':
    n = int(input('digite um número: '))
    if n not in lista:
        lista.append(n)
        print('valor adicionado com sucesso ')
    elif n in lista:
        Cnúmrep += 1
    resp = str(input('quer continuar? ')).upper().strip()

print('=' * 60)
lista.sort()
print(lista)
print(f'você digitou {Cnúmrep} números repetidos')
print('fim')
