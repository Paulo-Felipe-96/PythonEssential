n = int(input('Informe um número: '))
s = 0

for i in range(1, n):
    if n % i == 0:
        s += i

print(f'Soma dos divisores de {n} é: {s}')
