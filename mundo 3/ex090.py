aluno = {}
aluno['nome'] = str(input('nome: '))
aluno['média'] = float(input('média do aluno: '))

if aluno['média'] < 5:
    aluno['situação'] = 'reprovado'
elif aluno['média'] >= 5 and aluno["média"] <= 9:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'aprovado'

print('='*60)
if aluno['situação'] == 'recuperação':
    print(f'o aluno {aluno["nome"]} está de {aluno["situação"]} com a média de {aluno["média"]} pontos')
else:
    print(f'o aluno {aluno["nome"]} está {aluno["situação"]} com a média de {aluno["média"]} pontos')
