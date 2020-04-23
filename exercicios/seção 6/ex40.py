n = 0
maior = 0
menor = 0

while n >= 0:
    n = int(input('Informe um número: '))
    if n > maior:
        maior = n

    if n < menor and menor > 0:
        menor = n

print(f'Maior número informado: {maior}\n'
      f'Menor número informado: {menor}')
