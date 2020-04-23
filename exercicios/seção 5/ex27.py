age = int(input('Informe a idade do nadador: '))

# noinspection PyChainedComparisons
if age >= 5 and age < 8:
    print(f'Infantil A: {age} anos de idade.')
elif age >= 8 and age < 11:
    print(f'Infantil B: {age} anos de idade.')
elif age >= 11 and age < 14:
    print(f'Juvenil A: {age} anos de idade.')
elif age >= 14 and age < 18:
    print(f'Juvenil B: {age} anos de idade.')
else:
    print(f'Sênior: {age} anos de idade.')
