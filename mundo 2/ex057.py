sex = str(input('qual é o seu sexo? [M/F] ')).strip().upper()[0]
while sex not in 'FM':
    print('sexo invalido! por favor insira novamente:')
    sex = str(input('qual é o seu sexo? [M/F] ')).strip().upper()[0]
print('registro feito com sucesso!')
