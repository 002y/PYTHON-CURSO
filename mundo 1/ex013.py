sal = float(input('salario do funcionario: R$'))
aum = sal + (sal*15/100)
print('um funcionario que recebia {:.2f} com 15% de aumento.\n vai passar a receber {:.2f} '.format(sal,aum))