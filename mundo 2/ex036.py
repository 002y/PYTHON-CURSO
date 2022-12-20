'''casa = float(input('qual é o valor da casa? R$'))
sal = float(input('qual é o seu salário? R$'))
fin = int(input('quantos anos de financiamento?'))
pres = casa / (fin * 12)
min = sal * 30 / 100
print('para pagar uma casa de {} em {} anos \na prestação será de {} ao mês'.format(casa, fin, pres))
if sal <= min:
    print('o seu pedido de emprestimo não foi aceito')
else:
    print('o seu pedido não foi aceito')'''

cores = {'verde':'\033[1;32;40m',
         'vermelho':'\033[1;31;40m',
         'limpa':'\033[m'}
casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe seu salário: '))
anospagamento= int(input('Informe em quantos anos irá pagar: '))
meses = anospagamento * 12
mensalidade = casa / meses
print('DURANTE {} ANOS\nSUA MENSALIDADE SERÁ: {:.2f}'.format(anospagamento,mensalidade))
if mensalidade > salario*0.30:
    print('O VALOR É MAIOR QUE 30% DO SEU SALÁRIO\n{}EMPRESTIMO NEGADO{}'.format(cores['vermelho'], cores['limpa']))
else:
    print('{}EMPRESTIMO APROVADO{}'.format(cores['verde'], cores['limpa']))