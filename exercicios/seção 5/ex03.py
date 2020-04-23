import math

n = float(input('Informe um número: '))
if n > 0:
    print(f'Raiz quadrada de {n} é {round(math.sqrt(n), 2)}')
else:
    print(f'Número {n} ao quadrado {n * (- n)}')
