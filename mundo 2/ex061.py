print('\033[1;32;40m PROGRESSÃO ARITIMÉTICA \033[m')
print('=' * 40 )
p1 = int(input('primeiro termo: '))
r= int(input('razão: '))
termo = p1
c = 1
while c <= 10:
    print(f'{termo} > ', end='')
    termo += r
    c += 1
print('FIM')