def voto(nascimento):
    from datetime import date
    atual = date.today().year
    idade = atual - nascimento
    if idade >= 18:
        print(f'{idade} anos, o seu voto é obrigatório')
    elif idade >= 16 or idade >= 65:
        print(f'{idade} anos, o seu voto é opcional')
    else:
        print(f'{idade} anos, você não tem idade para votar')


voto(int(input('ano de nascimento: ')))
