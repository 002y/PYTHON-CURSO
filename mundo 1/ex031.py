from time import sleep
dist = float(input('how far will you go?'))
print('calculating wait please...')
sleep(2)
if dist <=180:
    price = dist * 0.50
else:
    price = dist * 0.45
print('the price was {:.2f} real'.format(price))