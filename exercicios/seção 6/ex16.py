n = int(input('Digite um número IMPAR: '))

if n % 2 != 1:
    print(f'{n} não é IMPAR!')
else:
    for i in range(n, 0, -1):
        if i % 2 != 0:
            print(f'{i}')
