n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))
if n1 > n2:
    print(f'{n1} é maior que {n2} \n'
          f'A diferença entre eles é {n1 - n2}.')
else:
    print(f'{n2} é maior que {n1} \n'
          f'A diferença entre eles é {n2 - n1}.')
