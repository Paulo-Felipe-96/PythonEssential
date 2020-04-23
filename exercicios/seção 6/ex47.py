op = 0

while op != 5:
    op = int(input('Escolha uma opção: \n'
                   '1 - adição \n'
                   '2 - subtração \n'
                   '3 - multiplicação \n'
                   '4 - divisão \n'
                   '5 - sair \n'))
    if op == 5:
        break

    n1 = float(input('Primeiro número: '))
    n2 = float(input('Segundo número: '))

    if op == 1:
        print(f'Adição: {n1 + n2}')
    elif op == 2:
        print(f'Subtração: {n1 + n2}')
    elif op == 3:
        print(f'Multiplicação: {n1 * n2}')
    elif op == 4:
        print(f'Divisão: {n1 / n2}')

print('Fim da execução.')
