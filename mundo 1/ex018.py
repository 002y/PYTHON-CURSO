from math import radians, sin, cos, tan
ângulo = float(input('digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
print('o ângulo de {} tem o seno de {:.2f} '.format(ângulo, seno))
c = cos(radians(ângulo))
print('o ângulo de {} tem o conseno de {:.2f} '.format(ângulo, c))
t = tan(radians(ângulo))
print('o ângulo de {} tem a tangente de {:.2f}'.format(ângulo, t))
