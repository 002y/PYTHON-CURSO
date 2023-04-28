import random
print('me apresente o numero dos alunos para a ordem da apresentação')
a1 = str(input('primeiro aluno: '))
a2 = str(input('segundo aluno: '))
a3 = str(input('terceiro aluno: '))
a4 = str(input('quarto aluno: '))
lis = [a1, a2, a3, a4]
alunos = random.shuffle(lis)
print('a ondem da apresentação será:')
print(lis)
