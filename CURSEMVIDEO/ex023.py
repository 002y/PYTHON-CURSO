num = int(input('tell me a number: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('analyzing your number')
print('unity: {} '.format(u))
print('ten: {} '.format(d))
print('hundred: {} '.format(c))
print('thousand: {} '.format(m))