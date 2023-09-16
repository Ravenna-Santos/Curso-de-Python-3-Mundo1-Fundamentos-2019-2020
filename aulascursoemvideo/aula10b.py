from random import randint
n = int(input("""Estou pensando em um número...
Tente adivinhar!
Ele está entre 1 e 5.
Que o jogo começe! Faça sua aposta: """))
a = randint(1, 5)
if a == n:
    print('Parabéns!!! Eu realmente pensei em {}!'.format(a))
else:
    print('Que pena você errou! Eu pensei em {}'.format(a))
