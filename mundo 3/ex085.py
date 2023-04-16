val = []
num = []
num1 = []
for c in range(7):
    val.append(int(input(f'digite o {c + 1}° valor: ')))

for v in val:
    if v %2 == 0:
        num.append(v)

    elif v %2 == 1:
        num1.append(v)

print(val)
print(f'números pares: {num}')
print(f'números impares: {num1}')
