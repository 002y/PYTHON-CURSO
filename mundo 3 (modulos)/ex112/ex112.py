from ultilidadesCev import moeda, dado

p = dado.leiaDinheiro('Digite um preço: R$')
resum = moeda.resumo(p, 20, 40)
print(f'  aumento: \t{resum[0]} \n  decresc: \t{resum[1]} \n  dobro: \t{resum[2]} \n  metade: \t{resum[3]}')
