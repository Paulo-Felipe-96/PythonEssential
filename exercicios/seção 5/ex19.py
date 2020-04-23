n = float(input('Informe um número e saiba se divisível por 3 ou 5: '))

if n % 3 == 0 and n % 5 != 0:
    print(f'Número {n} é divisível por 3.')
elif n % 5 == 0 and n % 3 != 0:
    print(f'Número {n} é divisível por 5.')
elif n % 3 != 0 or n % 5 != 0:
    print(f'Número {n} não é divisível por 3 ou 5.')
