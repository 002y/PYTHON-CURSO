import random
from time import sleep
print(' JOGOS NA MEGA SENA '.center(60, '¬'))

jogos = []
lista = []
num = []

resp = int(input('quantos jogos você quer gerar? '))
tot = 1
while tot <= resp:
    for c in range(6):
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print(' SORTEANDO JOGOS '.center(60, '¬'))
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l} ')
    sleep(1)

print(' BOA SORTE '.center(60, '¬'))
