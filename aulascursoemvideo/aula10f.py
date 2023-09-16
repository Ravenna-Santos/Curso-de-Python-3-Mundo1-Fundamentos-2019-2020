ano = int(input('Digite um ano: '))
if (ano % 400 == 0 and (ano % 4 == 0 or ano % 100 != 0)):
    print('É um ano Bissexto')
else:
    print('Não é um ano Bissexto')
