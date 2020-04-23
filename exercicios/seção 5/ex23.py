ano = int(input('Informe o ano: '))

if ano % 400 == 0:
    print(f'Ano {ano} é bissexto.')
elif ano % 4 == 0 and ano % 100 != 0:
    print(f'Ano {ano} é bissexto.')
