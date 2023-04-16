pessoas = list()
pessoas.append('gustavo')
pessoas.append(40)
galera = list()
galera.append(pessoas[:])
pessoas[0] = 'maria'
pessoas[1] = 22
galera.append(pessoas[:])
print(galera)

user = [['joão', 19], ['ana',33], ['joaquim', 13], ['maria', 45]]
for p in user:
    print(f'{p[0]} tem {p[1]} anos de idade ')

us = user[:]
print(us)
user.pop()
print(user)
