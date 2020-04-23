d = int(input('Intervalo de: '))
a = int(input('Até: '))
si = 0

if d > a:
    print('Intervalo inválido')
else:
    for i in range(d, a + 1):
        if i % 2 != 0:
            si += i

    print(f'Soma dos ímpares de {d} até {a} é {si}')
