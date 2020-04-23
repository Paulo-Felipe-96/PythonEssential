n = 0
qt = 0
qp = 0

while n != 1000:

    n = int(input('Informe um número entre 100 e 999: '))

    if n > 99 and n <= 999:
        qt += 1

    if n % 2 == 0 and n < 1000:
        qp += 1

print(f'Quantidade de números pares lidos: {qp}\n'
      f'Quantidade de valores lidos: {qt}')
