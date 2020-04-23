n = 0
maior = 0
menor = 0

for i in range(1, 11):
    n = float(input('Número: '))
    if n > maior:
        maior = n
    elif n < menor:
        menor = n

print(f'Maior número: {maior} \n'
      f'Menor número: {menor}')
