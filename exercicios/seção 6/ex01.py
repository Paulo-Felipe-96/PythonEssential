n = int(input('Digite um número maior que 0: '))
c = 1
c2 = 1

if n < 1:
    print('Número inválido.')
else:
    while c < n:
        if c % 3 == 0:
            print(f'{c} é múltiplo de 3.')
            c2 += 1
        if c2 == 6:
            break
        c += 1
