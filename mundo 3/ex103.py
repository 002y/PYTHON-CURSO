def ficha(nome, gol):
    if nome == '':
        nome = '<desconhecido>'
    if gol.isnumeric():
        gol = int(gol)
    else:
        gol = 0
    print(f'o jogador {nome} marcou {gol} gol(s)')


jogador = {'nome': str(input('nome do jogador: ')), 'gols': str(input('numero de gols: '))}
ficha(jogador['nome'], jogador['gols'])
