op = input('Escolha um operador matemático sendo ele +, -, * ou /: ')
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
r = 0

if op == '+':
    r = n1 + n2
elif op == '-':
    r = n1 - n2
elif op == '*':
    r = n1 * n2
elif op == '/':
    r = n1 / n2
else:
    print('Operador inválido!')

print(f'Resultado da operação {op} é: {r}')
