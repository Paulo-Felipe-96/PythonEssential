import math

n = 1

while n > 0:
    n = int(input('Informe um número: '))
    print(f'Quadrado: {n * n} \n'
          f'Cubo: {n * n * n} \n'
          f'Raiz quadrada: {round(math.sqrt(n), 2)}')
