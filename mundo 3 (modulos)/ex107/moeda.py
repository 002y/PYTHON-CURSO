def aumentar(preco, taxa):
    rest = preco + (preco * taxa/100)
    return rest


def diminuir(preco, taxa):
    rest = preco - (preco * taxa/100)
    return rest


def dobro(preco):
    rest = preco * 2
    return rest


def metade(preco):
    rest = preco/2
    return rest
