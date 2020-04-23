a = float(input('Informe sua altura: '))
s = input('Informe seu sexo (M/F): ')
pm = (72.7 * a) - 58
pf = (62.1 * a) - 44.7

if s == 'M':
    print(f'Peso ideal: {round(pm, 2)}')
else:
    print(f'Peso ideal: {round(pf, 2)}')
