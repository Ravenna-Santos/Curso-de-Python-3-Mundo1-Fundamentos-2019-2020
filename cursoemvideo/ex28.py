from random import randint
from time import sleep
computador = randint(0,5)
#print('Pensei no número {}'.format(computador))
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5 tente adivinhar!')
print('-=-' * 20)
jogador = int (input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador :
    print('Parabéns você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no número {}!!!'.format(computador,jogador))
