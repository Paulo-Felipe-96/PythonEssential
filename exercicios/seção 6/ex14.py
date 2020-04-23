n = int(input('Digite um número PAR: '))

if n % 2 != 0:
    print(f'{n} não é PAR!')
else:
    for i in range(n, -1, -1):
        if i % 2 == 0:
            print(f'{i}')
