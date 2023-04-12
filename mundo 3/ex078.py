valores = []
for c in range(6):
    valores.append(int(input(f'digite o valor {c}: ')))

min = min(valores)
min_p = valores.index(min)

max = max(valores)
max_p = valores.index(max)

print(valores)
print(f'o menor valor digitado foi: {min} na posição {min_p}')
print(f'o maior valor digitado foi: {max} na posição {max_p}')
