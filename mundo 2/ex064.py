
c = soma = n = 0

while n != 999:
    n = int(input('digite um número [999 para parar]: '))
    c += 1
    soma += n
c -= 1
soma -= 999
print(f'você digitou {c} números e a soma entre eles foi {soma} ')
