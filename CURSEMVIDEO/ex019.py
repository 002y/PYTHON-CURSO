import random
n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno:'))
n3 = str(input('terceiro aluno:'))
n4 = str(input('quarto aluno:'))
lis = [n1, n2, n3, n4]
aluno = random.choice(lis)
print('o aluno sorteado foi: {}'.format(aluno))
