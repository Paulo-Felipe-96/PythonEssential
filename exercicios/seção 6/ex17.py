n = int(input('Digite um número natural: '))
soma = 0

if n < 0:
    pass
else:
    for a in range(0, n + 1):
        soma += a
    print(f'Soma: {soma}')
