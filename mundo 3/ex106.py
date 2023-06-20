from time import sleep

cores = {'vermelho': '\033[1;31;40m', 'verde': '\033[1;32;40m', 'cinza': '\033[1;37;40m', 'azul': '\033[1;34;40m', 'nulo': '\033[m'}
def ajuda(funcao):
    print(cores['cinza'])
    help(funcao)
    print(cores['nulo'])


def continuar():
    continuar = str(input(f'{cores["azul"]} quer continuar? [S/N] {cores["nulo"]}')).upper()
    while continuar not in 'SN':
        print(f'{cores["vermelho"]} resposta inválida! digita apenas [S ou N] {cores["vermelho"]}')
        continuar = str(input(f'{cores["azul"]} quer continuar? [S/N] {cores["nulo"]}')).strip().upper()[0]
    if continuar == 'S':
        return True
    else:
        return False


contin = True
while contin == True:
    print(f'{cores["verde"]}', f' INTERACTIVE HELP '.center(60, '='), f'{cores["nulo"]}')
    funcao = str(input(f'{cores["azul"]} manual da função: '))
    sleep(0.3)
    ajuda(funcao)
    contin = continuar()

print(cores["azul"], 'FIM')
