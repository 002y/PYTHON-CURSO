'''for  c in range(1, 10):
    print(c)
print('fim')

print('=' * 10) #os dois dão o mesmo resultado

c = 1
while c < 10:
    print(c)
    c += 1
print('fim')'''

r = 'S'
while r == 'S':
    n = int(input('digite um valor: '))
    r = str(input('quer continuar? [S/N] ')).upper()
    if r == 'N':
        break
print('fim')