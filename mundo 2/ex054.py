from datetime import date
hoje = date.today().year
maior = 0
menor = 0
for c in range(1, 6):
    ano = int(input(f'ano de nascimento da {c}° pessoa: '))
    idade = hoje - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'existem {maior} pessoas mais velhas, e {menor} pessoas mais novas ')
