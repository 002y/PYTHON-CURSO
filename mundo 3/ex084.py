pessoas = []
dados = []
nomeMAI = []
nomeMEN = []
menor = maior = 0

while True:
    dados.append(str(input('nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
        nomeMAI = nomeMEN = dados[0]
    else:
        if dados[1] > maior:
            maior = dados[1]
            nomeMAI = dados[0]
        if dados[1] < menor:
            menor = dados[1]
            nomeMEN = dados[0]
    pessoas.append(dados[0])
    dados.clear()

    cont = str(input('quer continuar? ')).strip().upper()
    if cont == 'S':
        continue
    elif cont == 'N':
        break
    while cont not in 'SN':
        print('resposta inválida, tente novamente')
        cont = str(input('quer continuar? ')).strip().upper()

print(f'no total foram {len(pessoas)} pessoas cadastradas ')
print(f'o nome do maior é {nomeMAI} com {maior}Kg ')
print(f'o nome do menor é {nomeMEN} com {menor}Kg ')
print('fim')
