mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(' MATRIZ EM PYTHON '.center(60, '~'))
for c in range(0, 3):
    for l in range(0, 3):
        mat[c][l] = int(input(f'digite um número para [{c}][{l}]: '))
for c in range(0, 3):
    for l in range(0, 3):
        print(f'|{mat[c][l]:^5}|', end='')
    print()
    print('-'.center(21, '-'))
