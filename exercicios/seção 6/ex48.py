n = int(input('Informe um número: '))

n1 = 0
n2 = 1
sn1 = 0
sn2 = 0

for i in range(1, n + 1):
    n1 = n1 + n2
    n2 = n2 + n1
    if n1 % 2 == 0:
        sn1 += n1
    if n2 % 2 == 0:
        sn2 += n2

print(f'Soma dos números pares da sequência de Fibonacci: \n'
      f'{sn1 + sn2}')
