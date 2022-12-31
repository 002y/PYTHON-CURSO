from datetime import date
print('   \033[1;32;40m CONFEDEREÇÃO NACIONAL DE NATAÇÃO \033[m')
print('='* 42)
nasc = int(input('em qual ano você nasceu?'))
now = date.today().year
y = now - nasc
if y < 9:
    print('o atleta tem {} anos e é \033[0;30;47m MIRIM \033[m'.format(y))
elif y <= 14:
    print('o atleta tem {} anos e é \033[0;30;47m INFANTIL \033[m'.format(y))
elif y <= 19:
    print('o atleta tem {} anos e é \033[0;30;47m JUNIOR \033[m'.format(y))
elif y <= 25:
    print('o atleta tem {} anos e é \033[0;30;47m SÊNIOR \033[m'.format(y))
else:
    print('o atleta tem {} anos e é \033[0;30;47m MASTER \033[m '.format(y))
