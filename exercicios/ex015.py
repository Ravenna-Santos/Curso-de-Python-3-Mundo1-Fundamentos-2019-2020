dia=int(input('Quantos dias? '))
km=float(input('Quantos km rodados? '))
pago=dia*60+km*0.15
print('O total a pagar é R${:.2f}!'.format(pago))
