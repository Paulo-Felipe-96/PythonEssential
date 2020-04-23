op = input('Bem-vindo, querido usuário(a)! \n'
           'Escolha uma opção\n'
           '1) Soma de dois números\n'
           '2) Diferença entre dois números\n'
           '3) Produto entre dois números\n'
           '4) Divisão entre dois números\n'
           'Digite: ')

if op == '1':
    n1 = float(input('Primeiro número: '))
    n2 = float(input('Segundo número: '))
    print(f'Soma: {n1 + n2}')
elif op == '2':
    n1 = float(input('Primeiro número: '))
    n2 = float(input('Segundo número: '))
    print(f'Diferença: {n1 - n2}')
elif op == '3':
    n1 = float(input('Primeiro número: '))
    n2 = float(input('Segundo número: '))
    print(f'Produto: {n1 * n2}')
elif op == '4':
    n1 = float(input('Primeiro número: '))
    n2 = float(input('Segundo número: '))
    if n1 < 1 or n2 < 2:
        print('Número inválido!')
    else:
        print(f'Divisão: {n1 / n2}')
else:
    print('Opção inválida.')
