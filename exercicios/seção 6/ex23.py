n = int(input('Informe um número: '))

for i in range(1, n):
    if n % i == 0:
        print(f'{i} é divisível')
