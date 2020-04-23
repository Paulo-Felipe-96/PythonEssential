n = int(input('Digite um número IMPAR: '))

if n % 2 == 0:
    print(f'{n} não é IMPAR!')
else:
    for i in range(0, n + 1):
        if i % 2 != 0:
            print(f'{i}')
