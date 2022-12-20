n = int(input('Digite um número:'))
print('Escolha uma base de conversão')
print('='*20)
print('[1]Binário\n[2]Octal\n[3]Hexadecimal')
print('='*20)
escolha = int(input('Escolha: '))
if escolha == 1:
    print(f'{n} Convertido em binário é {bin(n)[2:]}')
elif escolha == 2:
    print(f'{n} Convertido em octal é {oct(n)[2:]}')
elif escolha == 3:
    print(f'{n} Convertido em hexadecimal é {hex(n)[2:]}')
else:
    print('Escolha as opções de 1 ao 3.')
