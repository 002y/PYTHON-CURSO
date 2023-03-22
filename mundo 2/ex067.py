x = 0

print('-=' * 10)
print('\033[1;32;40m TABUADA \033[m ')
print('-=' * 10)

while True:
    n = int(input('digite um número: '))
    if n <= 0:
        break
    print('-=' * 10)
    while x != 10:   #enquanto o contador for diferente de 0
        x += 1   # no final o contador vai ser 10
        print(f'{n} X {x} = {n*x}')

    x = 0 # então ele volta a ser 0
    print('-=' * 10)
print('FIM')
