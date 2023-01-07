print('{:=^60}'.format('\033[1;32;40m PY STORE \033[m'))
buy = float(input('valor das compras: '))
print('condição do pagamento: ')
print('[1] dinhero a vista ')
print('[2] no cartão a vista ')
print('[3] parcelado no cartão')
pay = int(input('opção de pagamento: '))
if pay==1:
    print('Voce deverá pagar {}R$'.format(buy-(buy*0.10)))
elif pay==2:
    print('Voce deverá pagar {}R$'.format(buy-(buy*0.05)))
elif pay==3:
    np=int(input('Quantas vezes deseja parcelar?'))
    if np<=2:
        print('Voce pagará {}R$ e cada parcela ficará em {}R$'.format(buy, buy/np))
    elif np>=3:
        print('Voce pagará {:.2f}R$ em {} parcelas com juros de 20% e o valor de cada parcela ficará em {:.2f}R$'.format(buy+(buy*0.20), np, buy*1.20/np))
