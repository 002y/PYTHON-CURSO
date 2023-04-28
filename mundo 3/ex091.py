from random import randint
from operator import itemgetter
from time import sleep

jogadores = {}
nomes = ['joão', 'marcos', 'felipe', 'gabriel']
for n in nomes:
    jogadores[n] = randint(1,6)
print(jogadores)

ranking = []
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
c = 1
print('==  RANKING DO JOGADORES  =='.center(41, ' '))
for k, v in ranking:
    print(f'{c:>9}°   {k:<15} -> {v}')
    c += 1
