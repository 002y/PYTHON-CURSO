objetos = [2, 4, 6, 8]

def dobra(lista):
    c = 0
    while c < len(lista):
        lista[c] *= 2
        c += 1


print(objetos)
dobra(objetos)
print(objetos)
