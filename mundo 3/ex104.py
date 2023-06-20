def leiaInt(num):
    while True:
        n = str(input(num))
        if n.isnumeric():
            return int(n)
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')


numero = leiaInt('digite um número: ')
print(f'você digitou o número: {numero}')
