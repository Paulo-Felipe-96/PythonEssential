"""n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
if n1 >= 0 and n2 >= 0:
    print(f'Números válidos')
else:
    print('Ambas notas devem ser iguais ou maiores que 0 (zero)!')
"""
n1 = ''
n2 = ''

while n1 == '' or n2 == '':
    n1 = input('Primeira nota: ')
    n2 = input('Segunda nota: ')

    if n1 == '' or n2 == '':
        print('Os campos não podem ficar vazios.')

n1 = float(n1)
n2 = float(n2)

if n1 < 0 or n2 < 0 or n1 > 10 or n2 > 10:
    print('Notas inválidas. \n'
          'Fim da execução.')
else:
    print(f'Média: {(n1 + n2) / 2}')
