text = """hello, my codename is 002. i am from Brazil 
i live with my mother and i have a dog."""
print(45 * ('-'))
print(text)
print(45 *('-'))
nome = str(input('what is your full name? ')).strip()
print('analyzing your name... ')
gh = nome.upper()
ph = nome.lower()
fh = len(nome) - nome.count(' ')
th = nome.split()
print('your name with capital letters is "{}" '.format(gh))
print('with lowercase is "{}" '.format(ph))
print('your name has a total of {} letters'.format(fh))
print('your first name is {}, and he has {} letters  '.format(th[0], len(th[0])))

