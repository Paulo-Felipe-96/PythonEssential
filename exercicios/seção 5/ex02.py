import math

n = float(input('Número: '))
if n > 0:
    print(f'Raiz quadrada de {n} é {round(math.sqrt(n), 2)}')
else:
    print('Número inválido.')
