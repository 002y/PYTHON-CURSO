#contador de números pares
s = 0
con = 0
for c in range(1 , 7):
    n = int(input(f'{c}° número:  '))
    if n % 2 == 0:
        s += n
        con += 1
print(f'você imformou {con} números PARES e a soma foi {s}')
