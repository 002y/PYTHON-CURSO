# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
# del pessoas['sexo']
# print(pessoas.values())
#
#
# filme = {'nome': 'Star Wars', 'ano': 1977, 'diretor': 'george lucas'}
# for k, v in filme.items():
#     print(f'{k}: {v}')
# 
# create = dict()
# create['jogos'] = 'Call Of Duty'
# print(create['jogos'])
#
# dicio = {'nome': 'matheus'}
# print(dicio)
# dicio.update({'nome': 'roberth'})
# dicio.update({'idade': 15, 'sexo': 'masculino'})
# print(dicio)
#
# sex = dicio.setdefault('idade')
# pele = dicio.setdefault('pele', 'preto')
# print(pele)
# print(sex)
# print(dicio)
#
# nome = {'nome': 'roberth'}
# idade = {'idade': 15}
# juncao = {**nome, **idade}
# print(juncao)
#
