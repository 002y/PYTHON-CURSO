soma = cont = média =  0 #todos recebem 0
maior = menor = None
r = 'S'

while r == 'S':
    n = int(input('digite um número: '))

    soma += n #somando todos os números
    cont += 1 #contando a quantidade de números

    # agora verificamos se as variáveis maior e menor são None ou já possuem um valor
    if maior is None or n > maior:
        maior = n
    if menor is None or n < menor:
        menor = n

    r = str(input('quer continuar? [S/N] : ')).upper().strip()[0]


média = soma / cont
print(f'você digitou {cont} números e a média entre eles foi: {média}, o maior número foi {maior} e o menor foi {menor} ')

