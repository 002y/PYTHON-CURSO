larg = float(input('largura da parede:'))
alt = float(input('altura da parede:'))
m2 = larg * alt
tinta = m2/2
print('sua parede tem uma dimensão de {} x {} e sua área é de {}M².'.format(larg, alt, m2))
print('para pintar toda a parede você precisará de {}l de tinta'.format(tinta))


