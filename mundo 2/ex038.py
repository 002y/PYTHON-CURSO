p = int(input('primeiro numero: '))
s = int(input('segundo numero: '))
if p > s:
    print('{} é maior '.format(p))
elif s > p:
    print('{} é maior '.format(s))
else:
    p == s or s == p
    print('os dois numeros são iguais')
