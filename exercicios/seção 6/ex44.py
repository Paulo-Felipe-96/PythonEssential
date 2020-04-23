n = int(input('Informe um número: '))

n1 = 0
n2 = 1

for i in range(1, n + 1):
    print(f'Fibonacci: {n1}, {n2}')
    n1 = n1 + n2
    n2 = n2 + n1
    if n1 > n:
        break
