r = ''
while r != 'Não':
    s = float(input('Digite seu salário R$: '))
    e = float(input('Valor da prestação do empréstimo R$: '))

    if e > s * 0.2:
        print(f'Empréstimo não concedido.')
        r = input('Tentar novamente? (Sim/Não) ')
    else:
        print(f'Empréstimo concedido.')
        r = 'Não'
