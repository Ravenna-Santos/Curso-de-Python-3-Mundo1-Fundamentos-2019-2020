v = float(input('A que velocidade seu carro está? km/h: '))
if v > 80:
    print('Você foi multado! Sua multa custa R$: {:.2f}'.format(7*(v-80)))
