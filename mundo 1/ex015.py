dia = int(input('quantidade de dias rodados:'))
km = float(input('quantidade de km rodados:'))
total = (dia * 60) + (km * 0.15)
print('o valor total é de {:.2f}R$.'.format(total))
