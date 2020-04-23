sb = float(input('Salário base R$: '))
gt = sb * 0.05
ds = sb * 0.07
sf = sb + gt - ds
print(f'Salário a receber R${sf}')
