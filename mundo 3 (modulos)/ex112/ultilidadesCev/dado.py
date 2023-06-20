from .moeda import moeda
def leiaDinheiro(dinheiro):
    valido = False
    while not valido:
        entrada = input(dinheiro).replace(',', '.')
        if not entrada.replace('.', '').isnumeric():
            print(f'\033[0;31mERRO: "{entrada}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
