a = float(input('Digite um número: '))
b = float(input('Digite um número: '))
c = float(input('Digite um número: '))
if ((a + b) < c) and ((a + c) < b) and ((b + c) < c):
    print('As retas digitadas formam um triângulo!')
else:
    print('As retas não formam um triângulo!')
