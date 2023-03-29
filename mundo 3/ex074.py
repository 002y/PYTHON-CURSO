from random import randint
maior = 0
menor = 0
cpu = randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10)

print('números sorteados: ',end='')
for n in cpu:
    print(f' {n}', end='')

print(f'\n o maior valor doi {max(cpu)}')
print(f' o menor valor foi {min(cpu)}')
