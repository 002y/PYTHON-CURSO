def fatorial(a=0, show=True):
    """
    -> calcula o fatorial de um número
    param a -> número a ser calculado
    param show -> se você quiser ou não a conta
    """
    f = 1
    print(f'{a}! -> ')
    for c in range(a, 0, -1):
        f *= c
        if c == a:
            continue
        if show:
            print(f'{a}x{c} = {f}')
        else:
            if c == 1:
                print(f, end=' -> ')
    print('FIM')

num = int(input('digite um número: '))
show = str(input('quer mostras os calculos? [S/N] ')).strip().upper()[0]
if show == 'S':
    show = True
else:
    show = False
fatorial(num, show)
