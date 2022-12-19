from datetime import date
from time import sleep
ano = int(input("what year do you want to analyze ? put 0 to analyze the current year: "))
sleep(2)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print ('the year {} is leap '.format(ano))
else:
    print ('year {} is not leap'.format(ano))