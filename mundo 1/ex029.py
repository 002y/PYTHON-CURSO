x = int(input('Qual é a velocidade em kilometros por hora atual do automovel?'))
if x <= 80:
    print('''Você está dentro da velocidade permitida,
pode seguir viagem.''')
else:
    print(f'''Você está acima da velocidade permitida,
você receberá uma multa de {(x-80)*7},00 reais.''')

