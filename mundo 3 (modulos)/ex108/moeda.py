def aumentar(preco=0, taxa=0):
    rest = preco + (preco * taxa/100)
    return rest


def diminuir(preco=0, taxa=0):
    rest = preco - (preco * taxa/100)
    return rest


def dobro(preco=0):
    rest = preco * 2
    return rest


def metade(preco=0):
    rest = preco/2
    return rest


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
