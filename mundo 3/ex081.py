num = []
n = 0
cinco = 0

resp = 'S'
while resp == 'S':
    num.append(int(input('digite um número: ')))
    n += 1
    resp = str(input('quer continuar? [S/N] ')).strip().upper()

print('=' * 60)
print(f'ao total foram digitados {n} números ')
num.sort(reverse=True)
print(f'números em ondem decrescente: num')
if 5 in num:
    print('o 5 está na lista ')
else:
    print('o 5 não está na lista ')
print(' FIM ')
