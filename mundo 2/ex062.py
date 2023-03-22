print('\033[1;32;40m RAZÃO ARITIMÉTICA \033[m')
p1 = int(input('primeiro termo: '))
r = int(input('razão: '))

termo = p1
c = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while c <= total:
        print(f'{termo} > ', end='')
        termo += r
        c += 1

    print('pausa')
    mais = int(input('quantos termos você quer mostrar a mais? '))

print('fim')
print(f' foram {total} termos no total')
print('+-' * 20)