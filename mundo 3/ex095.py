from time import sleep

jogadores = []
cont = total = 0

def calcular_total(gols):
    return sum(gols)


while True:
    jogador = {}
    gol = []
    jogador['nome'] = str(input('nome do jogador: '))
    jogador['partidas'] = int(input('quantas partidas foram jogadas? '))
    for v in range(1, jogador['partidas']+1):
        gol.append(int(input(f'quantidade de gols na {v}° partida: ')))
    jogador['gols'] = gol[:]
    jogadores.append(jogador.copy())

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('quer continuar? [S/N]')).strip().upper()[0]
        if continuar == 'S':
            continue
        elif continuar == 'N':
            break
        else:
            print('erro! digite apenas S ou N')
    print('='*60)
    if continuar == 'N':
        break

print('='*60)
print('N°   NOME            GOLS            TOTAL')
print('-'*50)
for c, jogador in enumerate(jogadores):
    nome = jogador['nome']
    gols = jogador['gols']
    total = calcular_total(gols)
    print(f'{c}°   {nome:<15} {gols}{"":<15}{total}')
print('=' * 60)
print()

while True:
    e = int(input('de qual jogador você quer ver os detalhes? [999: para parar]'))
    if e == 999:
        break
    gols = jogadores[e]["gols"]
    tot = calcular_total(gols)

    print(f'jogador: {jogadores[e]["nome"]}')
    for c, v in enumerate(jogadores[e]["gols"], start=1):
        print(f' {c}° partida -> {v} gols ')
        sleep(1)
    print(f'-> total: {tot} pontos')
    print('='*60)


print('<< VOLTE SEMPRE >>')
sleep(3)
