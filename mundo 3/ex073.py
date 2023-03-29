from time import sleep

cont = 0
print('=' * 60)

texto = ' BRASILEIRÃO 2023 '
largura = 60
preenchimento = '='
print(texto.center(largura, preenchimento))

print('=' * 60)
print('')

times = 'Flamengo',\
        'Palmeiras',\
        'Athletico Paranaense',\
        'Atlético Mineiro',\
        'São Paulo',\
        'Fluminense',\
        'Fortaleza',\
        'Corinthians',\
        'Santos',\
        'Internacional',\
        'Grêmio',\
        'América Mineiro',\
        'Atlético Goianiense',\
        'Ceará',\
        'Bahia',\
        'Botafogo',\
        'Red Bull Bragantino',\
        'Cruzeiro',\
        'Goiás',\
        'Cuiabá'
for c in times:
    cont += 1
    print(f'{cont}° {c}')
cont = 0

print('')
print('=' * 60)
print('')

print('cinco primeiros: ')
for c in range(0,5):
    cont += 1
    print(f'{cont}° {times[c]}')
    
print('')
print('=' * 60)
print('')

cont = 17

print('os quatro últimos colocados: ')
for c in range(-4, 0):
    print(f'{cont}° {times[c]} ')
    cont += 1

print('')
print('=' * 60)
print('')

print('times em ordem alfabética: ')
times = sorted(times)
for ordem in range(0, len(times)):
    print(f'{times[ordem]}', end='\n')

print('')
print('=' * 60)
print('')

pesquisa = str(input('Qual time deseja saber a posição? ')).capitalize()
if pesquisa not in times:
    print('O TIME PESQUISADO NÃO ESTA NA CLASSIFICAÇÃO ATUAL.')
else:
    pos = times.index(pesquisa) + 1
    print(f'0 time pesquisado está na {pos}ª posição')


print('')
print('=' * 60)
print('')


sleep(1)
print('\033[1;31mFINALIZANDO O PROGRAMA...\033[m')
sleep(0.5)
