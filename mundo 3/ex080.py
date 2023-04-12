#bisect.insort(lista, n) já insere n na lista de forma ordenada:
import bisect
numeros = []
for c in range(0,5):
    n = int(input('digite um número: '))
    bisect.insort(numeros, n)
    print(f'o número {n} foi inserido na posição {numeros.index(n)}')
print(f'números digitados: {numeros} ')
