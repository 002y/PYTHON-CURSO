#exercicio feito depois (não consegui fazer na época)
primeiro = int(input('primeiro termo: '))
razão = int(input('razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print(f'{c}', end=' -> ')
print('fim')
