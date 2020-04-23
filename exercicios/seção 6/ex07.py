media = 0
n = 0
s = 0

for i in range(1, 11):
    n = float(input('Número: '))
    if n > 0:
        s += n

media = s / 10

print(f'Média: {media}')
