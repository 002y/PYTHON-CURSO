def leiaDinheiro(dinheiro):
    valido = False
    while not valido:
        entrada = str(input(dinheiro)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
