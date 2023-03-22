from time import sleep

soma_idade = homens = mulher = 0
pm_idade = H = F = False
print('\033[1;33;40m ANÁLISE DE DADOS DO GRUPO \033[m ')

pessoas = 0

while True:
    pessoas += 1
    print('-=' * 20)
    idade = int(input('qual é a sua idade? '))
    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input('qual o seu sexo? [M/F] ')).strip().upper()[0]
        if sexo not in 'MF':
            print('\033[1;31;40m opção invalida, tente novamente. \033[m ')

        if idade > 18:  # se a pessoa for maior de 18 anos
            pm_idade = True
            soma_idade += 1

        if sexo == 'M':  # quantos homens
            H = True
            homens += 1

        if sexo == 'F' and idade > 20:  # quantas mulheres
            F = True
            mulher += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('quer continuar? [S/N]')).strip().upper()[0]
        if continuar == 'S':
            continue
        if continuar == 'N':
            break
        else:
            print('\033[1;31;40m opção invalida, tente novamente. \033[m ')

    if continuar == 'N':
        break

print('-=' * 20)
print(f'foram cadastradas {pessoas} pessoas ')

if pm_idade == True:  # se existir pessoa maior de idade
    if soma_idade == 1:  # se for só uma
        print(f'{soma_idade} pessoa é maior de idade ')
    if soma_idade > 1:  # se for várias
        print(f'{soma_idade} pessoas são maiores de idade ')

if H == True:  # se existir homem
    if homens == 1:  # se for só um
        print(f'{homens} homem foi cadastrado ')
    if homens > 1:  # se for vários
        print(f'{homens} homens foram cadastrados ')

if F == True:  # se existir mulher
    if mulher == 1:  # se for só uma
        print(f'tem {mulher} mulher cadastrada com mais de 20 anos ')
    if mulher > 1:  # se for várias
        print(f'tem {mulher} mulheres cadastradas com mais de 20 anos  ')

input('digite qualquer tecla para finalizar: ')
print('FIM')
print('-=' * 20)
sleep(3.5)