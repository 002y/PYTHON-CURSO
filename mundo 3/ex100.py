from random import randint
numeros = list()
par = list()

def sorteia():
    for c in range(0, 5):
        numeros.append(randint(1, 10))
        if numeros[c] % 2 == 0:
            par.append(numeros[c])
    print(f'os números sortados foram {numeros}')


def somaPar():
    print(f'os numeros pares são {par} e a soma entre eles é de {sum(par)}')


sorteia(), somaPar()
