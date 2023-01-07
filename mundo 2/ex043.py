peso = float(input('quanto você pesa? KG'))
alt = float(input('qual é a sua altura? METROS: '))
imc = peso / alt ** 2
print ('{:.1f}'.format(imc))
if imc < 18.5:
    print('abaixo do peso')
elif imc > 18.5 and imc < 25:
    print('peso ideal')
elif imc > 25 and imc < 30:
    print('sobrepeso')
elif imc > 30 and imc < 40:
    print('obesidade')
else:
    print('obesidade mórbida')
