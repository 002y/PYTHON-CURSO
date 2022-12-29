from datetime import date
print('   \033[1;32;40m CONFEDEREÇÃO NACIONAL DE NATAÇÃO \033[m')
print('='* 42)
nasc = int(input('em qual ano você nasceu?'))
now = date.today().year
y = now - nasc
print(y)