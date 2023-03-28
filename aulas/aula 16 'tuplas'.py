a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(sorted(c)) #organizando os números
print(len(c)) #qual é o tamanho dessa tupla
print(c.count(5)) #quantas vezes está aparecendo 5 em c
print(c.index(5, 1))  #em que posição está o 5, começando da casa 1
#deslocamento ^
# del(pessoa) #deletar o valor da tupla




lanche = 'hamburguer', 'suco', 'pizza', 'pudim', 'batata frita', 'alface'
# tuplas são imutáveis
# lanche[1] = 'refrigerante'


'''1 print(f'filme com {lanche[-3:]}')'''

'''2 print(sorted(lanche))
print(lanche)'''

'''3 for cont in range(0, len(lanche)):
    print(f'{lanche[cont]} na posição {cont}')

print('=-' * 30)

for pos, comida in enumerate(lanche):
    print(f'{lanche[cont]} na posição {pos}')
'''



'''4 for cont in range(0, len(lanche)):
    print(f'filme com {lanche[cont]}')

for c in lanche: #mesma coisa ^
    print(f'filme com {c}') #usando diretamente uma variável composta
'''


'''5 for c in lanche:
    print(f'filme com {c[0]}')'''


print('muito bom')
