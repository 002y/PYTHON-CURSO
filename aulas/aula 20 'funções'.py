def contador(* núm): #use "*" para quando você não souber o comprimento da variavel
    lan = len(núm)
    print(f'-> {núm} tem o comprimento de {lan}')


contador(1, 2, 3)
contador(9, 5, 3, 2, 6, 1)


print('='*60)


def soma(a, b):
    s = a + b
    print(s)


soma(7, 7)
soma(9, 4, 1) #TypeError: soma() takes 2 positional arguments but 3 were given
# ^ nós definimos apenas 2 valores, e não 3
