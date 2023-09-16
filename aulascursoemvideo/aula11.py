print('\033[7;30mOlá, mundo!\033[m')
a = 3
b = 5
print('\033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))

nome = 'Ravenna'
print('Olá, muito prazer em te conhecer {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá, muito prazer em te conhecer {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))