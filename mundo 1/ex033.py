a = int(input('first value: '))
b = int(input('second value: '))
c = int(input('third value: '))
#menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = b
#maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
#resposta
print('the smallest number was {}'.format(menor))
print('the largest number was {}'.format(maior))
