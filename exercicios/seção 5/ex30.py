a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))

if a < b < c and a < c:
    print(f'{a}, {b}, {c}')
elif a < c < b and a < b:
    print(f'{a}, {c}, {b}')
elif b < a < c and b < c:
    print(f'{b}, {a}, {c}')
elif b < c < a and b < a:
    print(f'{b}, {c}, {a}')
elif c < a < b and c < b:
    print(f'{c}, {a}, {b}')
elif c < b < a and c < a:
    print(f'{c}, {b}, {a}')
else:
    print('Números iguais encontrados.')
