import math

n = int(input('Informe um número: '))

if n < 0:
    print('Número inválido.')
else:
    print(f'{round(math.log(n), 2)}')
