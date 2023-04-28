from math import hypot
print('teorema de pitágoras')
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('a hipotenusa irá medir {:.2f}'.format(hi))
