soma = cont =0
while True:
    núm = int(input('digite um número [999 para parar] :  '))
    if núm == 999:
        break
    soma += núm
    cont += 1

print(f' foram digitados {cont} números , e a soma dos números foi de {soma}')
