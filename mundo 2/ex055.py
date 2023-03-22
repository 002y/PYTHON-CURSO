print('MEDIDOR DE PESO') #trabalhando com analise de dados hehe
for c in range(1, 5):
    peso = float(input(f'peso da {c}° pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'a pessoa mais pesada tem {maior}KG e a mais leve tem {menor}KG')
