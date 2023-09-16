d = float(input('Qual a distância da sua viagem? km: '))
if d <= 200:
    p = d * 0.5
else:
    p = d * 0.45
print('O preço da passagem é R$: {:.2f}!'.format(p))
