import math
a = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(a))
cosseno = math.cos(math.radians(a))
tangente = math.tan(math.radians(a))
print('O ângulo de {} tem SENO de {:.2f}\nO ângulo de {} tem COSSENO de {:.2f}\nO ângulo de {} tem TANGENTE de {:.2f} '.format(a, seno, a, cosseno, a, tangente))
