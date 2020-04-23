ag = int(input('Informe sua idade: '))
tt = int(input('Informe o tempo de trabalho: '))

if ag >= 65:
    print(f'Aposentadoria aprovada, {ag} anos de idade.')
elif tt >= 30:
    print(f'Aposentadoria aprovada, {tt} anos trabalhados.')
elif ag >= 60 and tt >= 25:
    print(f'Aposentadoria aprovada!\n'
          f'{ag} anos de idade\n'
          f'{tt} anos trabalhados.')
else:
    print('Aposentadoria negada por tempo de trabalho ou idade insuficiente.')
