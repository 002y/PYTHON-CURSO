sal = float(input(' salario do funcionario R$:'))
if sal <= 1250.00:
    new = sal + (sal * 15 / 100)
else:
    new = sal + (sal * 10 / 100)
print('quem ganhava R${:.2f} passa a ganhar R${:.2f} agora. '.format(sal, new))
