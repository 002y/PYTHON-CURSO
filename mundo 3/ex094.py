verde = '\033[1;32;40m'
nulo = '\033[m'
pessoas = {}
pessoa = []
idadeMedia = []
mulher = idade = 0

continuar = 'S'
while not continuar == "N":
    pessoas['nome'] = (str(input('nome: ')))
    while True:
        pessoas['sexo'] = (str(input('sexo: [M/F]')).strip().upper())
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! digite apenas M ou F')
    if pessoas['sexo'] == 'F':
        mulher += 1
    pessoas['idade'] = (int(input('idade: ')))
    pessoa.append(pessoas.copy())

    continuar = str(input('quer continuar? ')).upper().strip()
    if continuar == 'S':
        continue
    else:
        while continuar not in 'SN':
            print('ERRO! digite apenas S ou N')
            continuar = str(input('quer continuar? ')).upper().strip()


for c in pessoa:
    idade += c["idade"]

idadeM = idade/len(pessoa)

for c in pessoa:
    if c["idade"] >= idadeM:
        idadeMedia.append(c)

print('=' * 60)
print(f'{verde} DADOS DO GRUPO {nulo}'.center(60, ' '))
print(f' --foram cadastradas {len(pessoa)} pessoas')

if mulher:
    print(f'   --existem {mulher} mulheres na lista')

print(f'   --a média de idade do grupo é de {idadeM:.2f}')
if idadeMedia:
    print(f'   --pessoas com idade acima da média: ')
for c in idadeMedia:
    print(f'     --{c["nome"]} com {c["idade"]} anos')


input('clique em qualquer botão para finalizar ')
