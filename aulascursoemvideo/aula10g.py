a = (float(input('Digite um número: ')))
b = (float(input('Digite um número: ')))
c = (float(input('Digite um número: ')))
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c
print('Maior: {}\nMenor: {}'.format(maior, menor))
