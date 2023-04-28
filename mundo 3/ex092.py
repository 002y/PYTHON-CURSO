from datetime import datetime

pessoa = {}
rest = 0
atual = datetime.now().year
pessoa['nome'] = str(input('nome: '))
pessoa['sexo'] = str(input('sexo: [M/F] ')).strip().upper()
pessoa['idade'] = atual - int(input('ano de nascimento: '))
pessoa['CLT'] = int(input('carteira de trabalho: ["0" se não tiver] '))

if pessoa['CLT'] != 0:
    pessoa['ano'] = int(input('ano de contratação: '))

    # if pessoa['ano'] != atual:
    #     anos = int(input('quantos anos de trabalho você tem? '))
    #
    #ano = (atual + pessoa['idade']) - pessoa['ano']
    #
    # if anos == True:
    #     ano += anos

    ano = pessoa['idade']
    pessoa['salário'] = float(input('salário: '))

if pessoa['CLT'] != 0:
    if pessoa['sexo'] == 'M':
        while ano != 65:
            ano += 1
            rest += 1

    if pessoa['sexo'] == 'F':
        while ano != 62:
            ano += 1
            rest += 1

    pessoa['aposentadoria'] = rest

print(pessoa)
print('='*60)
if pessoa['sexo'] == 'M' and rest != 65 and pessoa['CLT'] != 0:
    print(f'olá {pessoa["nome"]}, você tem {pessoa["idade"]} anos, e irá se aposentar daqui {rest} anos')
elif rest > 65:
    print(f'parabéns {pessoa["nome"]}, você já se aposentou')

if pessoa['sexo'] == 'F' and rest != 62 and pessoa['CLT'] != 0:
    print(f'olá {pessoa["nome"]}, você tem {pessoa["idade"]} anos, e irá se aposentar daqui {rest} anos')
elif rest > 62:
    print(f'parabéns {pessoa["nome"]}, você já se aposentou')

if pessoa['CLT'] == 0:
    print("hey men, how's life? ")
