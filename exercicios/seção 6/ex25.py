s = 0

for i in range(1, 1001):
    if i % 3 == 0 or i % 5 == 0:
        s += i

print(f'Soma de todos divisores de 3 ou 5: {s}')
