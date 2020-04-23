cd = int(input('Bem-vindo(a) à lanchonete +sabor!\n'
               '100 - Cachorro quente: R$1.20\n'
               '101 - Bauru simples: R$1.30\n'
               '102 - Bauru com ovo: R$1.50\n'
               '103 - Hamburguer: R$1.20\n'
               '104 - Cheeseburger: R$1.70\n'
               '105 - Suco: R$2.20\n'
               '106 - Refrigerante: R$1.00\n'
               'Informe sua escolha: '))

qt = int(input('Informe a quantidade: '))

if cd == 100:
    print(f'Total R${qt * 1.20}')
elif cd == 101:
    print(f'Total R${qt * 1.30}')
elif cd == 102:
    print(f'Total R${qt * 1.50}')
elif cd == 103:
    print(f'Total R${qt * 1.20}')
elif cd == 104:
    print(f'Total R${qt * 1.70}')
elif cd == 105:
    print(f'Total R${qt * 2.20}')
elif cd == 106:
    print(f'Total R${qt * 1.00}')
