def resumo(p, aum, dec):
    rest = [
    aumentar(p, aum),
    diminuir(p, dec),
    dobro(p),
    metade(p)]
    return rest



def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def aumentar(preco=0, taxa=0, formato=True):
    rest = preco + (preco * taxa/100)
    return rest if formato is False else moeda(rest)


def diminuir(preco=0, taxa=0, formato=True):
    rest = preco - (preco * taxa/100)
    return rest if formato is False else moeda(rest)


def dobro(preco=0, formato=True):
    rest = preco * 2
    return rest if formato is False else moeda(rest)


def metade(preco=0, formato=True):
    rest = preco / 2
    return rest if formato is False else moeda(rest)
