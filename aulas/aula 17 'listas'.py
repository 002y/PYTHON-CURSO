num = [2,6,4,1,6]
print(f'número inicial: {num}')

num[2] = 3 #adicionar um número na posição escolhida
num.append(7) #adicionar um número
num.sort() #deixar em ordem "(reverse=True)" para deixar em ordem inversa

print(num)

print(f'essa lista tem {len(num)} elementos') #ver quantos elementos tem

print('insert: ', end='')
num.insert(2, 0) # adicionar um número em uma posição especifica (no caso: no elemento 2, adicione 0)
print(num)

print('pop: ', end='')
num.pop() #eliminar o ultimo valor
num.pop(3) #para escolher qual elemento você quer eliminar
print(num)

print('caçando o 5...')
if 5 in num:
    num.remove(5) #remover o 5
else:
    print('não achei o número 5')
print(num)

texto = ' LISTA '
# largura = 60
# enchimento = '='
print(texto.center(60, '='))

valores = [] #eu tambem poderia usar "valores = list()"
for cont in range(0, 5):
    valores.append(int(input('digite um valor: ')))

for c,v in enumerate(valores): # a função enumerate pega tanto a chave quanto o valor
    print(f'na posição {c} encontrei o valor {v}!')
print('cheguei ao final da lista')
