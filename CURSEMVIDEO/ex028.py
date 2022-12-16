import random
from time import sleep
print(' '*1)
print('hello!, I will choose an integer between 0 and 5. Try to guess which.')
n = int(input('what number did i choose? '))
print(' '*1)
lista = [0, 1, 2, 3, 4, 5]
npc = random.choice(lista)
print('loading... please wait ')
sleep(2)
print(' '*1)
print('the number chosen was {}'.format(npc))
if n == npc:
    print('congratulations! you guessed it!')
else:
    print('i won, you couldn\'t guess.')

