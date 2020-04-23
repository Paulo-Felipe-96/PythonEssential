vh = float(input('Valor p/ hora: '))
ht = float(input('Horas trabalhadas: '))
ht *= 22
am = (vh * ht) * 0.10
sl = (vh * ht) + am
print(f'Salário com 10% de aumento R${round(sl, 2)}')
