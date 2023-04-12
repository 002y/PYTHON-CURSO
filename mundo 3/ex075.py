n =(int(input('digite um número: ')) ,
    int(input('digite um número: ')) ,
    int(input('digite um número: ')) ,
    int(input('digite um número: ')))

print(n)

print(f'o maior número é {max(n)}')

if 9 in n:
    if n.count(9) > 1:
        print(f'existem {n.count(9)} noves ')
    else:
        print('existe apenas 1 nove')

if 3 in n:
    print(f'o primeiro valor de 3 foi digitado na {n.index(3) +1}º casa')

print(f'os números pares foram: ',end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')


