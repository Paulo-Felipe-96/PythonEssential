n = int(input('Informe um número: '))
s = 0

for i in range(1, n):
    if i % 11 == 0:
        s += i
        break

print(f'{s} é múltiplo de 11')
