larg=float(input('Largura da parede: '))
alt=float(input('Altura da parede: '))
area=larg*alt
tinta=area/2
print('Sua parede tem dimensão de {} x {} e sua área {} m².\nPara pintar essa parede, você precisará de {}l de tinta'.format(larg, alt, area, tinta))
