linha = ('-=') * 10
preço = totmil = mais_barato = 0
continuar = 'S'
barato_nome = ''

produtos = {
    1: {'nome': 'RTX 4090', 'preco': 14000},
    2: {'nome': 'PS5', 'preco': 5000},
    3: {'nome': 'teclado RAZER', 'preco': 650},
    4: {'nome': 'cadeira gamer', 'preco': 1300}
}

print(f'{linha}LOJA BARATÃO{linha}')
print('produtos disponíveis: ')

for key, value in produtos.items():
    print(f"{value['nome']}: {value['preco']} R$ [{key}]")

while True:
    carrinho = int(input('quais produtos você quer levar? '))
    if carrinho in produtos:
        preço += produtos[carrinho]['preco']
        if produtos[carrinho]['preco'] < mais_barato or mais_barato == 0:
            mais_barato = produtos[carrinho]['preco']
            barato_nome = produtos[carrinho]['nome']
        if produtos[carrinho]['preco'] > 1000:
            totmil += 1
    else:
        print('produto não encontrado, tente novamente. ')

    continuar = str(input('quer continuar? [S/N}')).upper().strip()
    while continuar not in ['N', 'S']:
        print('opção inválida, tente novamente')
        continuar = str(input('quer continuar? [S/N}')).upper().strip()

    if continuar == 'N':
            break

print(f'preço total: {preço} R$')
print(f'temos {totmil} produtos acima de 1000 R$')
print(f'o produto mais barato é {barato_nome} por {mais_barato}R$')
print('Fim')
