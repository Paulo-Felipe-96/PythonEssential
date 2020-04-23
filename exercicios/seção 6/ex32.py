n = int(input('Quantos lançamentos de dados ? '))

for i in range(1, n + 1):

    d1 = int(input('Dado 1: '))
    d2 = int(input('Dado 2: '))

    if d1 > d2:
        print(f'Dado 1 {d1} maior que Dado 2 {d2}')
    elif d1 < d2:
        print(f'Dado 2 {d2} maior que Dado 1 {d1}')
    else:
        print(f'Dado 1 {d1} e Dado 2 {d2} são iguais')
