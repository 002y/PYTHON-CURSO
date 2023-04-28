jogador = {}
gol = []
cont = total = 0

jogador['nome'] = str(input('nome do jogador: '))
jogador['partidas'] = int(input('quantas partidas foram jogadas? '))
for v in range(1, jogador['partidas']+1):
    gol.append(int(input(f'quantidade de gols na {v}° partida: ')))
jogador['gols'] = gol

print('='*60)
for k, v in jogador.items():
    print(f'{k}: {v}')

print()
print('='*60)
print(f'o {jogador["nome"]} jogou {jogador["partidas"]} partidas')
while cont != jogador['partidas']:
    for c in range(jogador['partidas']):
        print(f'na partida {c+1}: {jogador["nome"]} fez {jogador["gols"][c]}')
        cont += 1
        total += jogador["gols"][c]

print(f'total de {total} gols')
print()
print('='*60)
