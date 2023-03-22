p = 0
q = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        p += c
        q += 1
        #  ↑
        #MESMA COISA
        #  ↓
        #p = p + c
        #q = q +  1
print(f'a soma dos {q} valores é: {p}')