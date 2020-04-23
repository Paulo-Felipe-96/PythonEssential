import math

n = float(input('Digite um número: '))
if n > 0:
    print(f'{n} ao quadrado: {n * n}')
    print(f'Raiz quadrada de {n}: {round(math.sqrt(n), 2)}')
