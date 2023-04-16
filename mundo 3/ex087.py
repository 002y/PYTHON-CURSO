print(' MATRIZ EM PYTHON '.center(60,'~'))
val = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = colu = linha = 0
for l in range(0, 3):
    for c in range(0, 3):
        val[l][c] = int(input(f'digite um valor para [{l}][{c}]:  '))

print('~' * 60)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'|{val[l][c]:^5}|', end='')
    print()
    print('-'.center(21, '-'))

print('~' * 60)
for l in range(0, 3):
    for c in range(0, 3):
        if val[l][c] %2 == 0:
            par += val[l][c]
        if c == 2:
            colu += val[l][2]

linha = val[1][0]
if val[1][1] >= linha:
    linha = val[1][1]
if val[1][2] >= linha:
    linha = val[1][2]

print(f'a soma dos valores pares na matriz é de: {par}')
print(f'a soma dos valores da terceira coluna foi de {colu}')
print(f'o maior valor da segunda linha é: {linha}')
