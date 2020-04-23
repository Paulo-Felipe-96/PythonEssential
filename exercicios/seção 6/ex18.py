n = int(input('Quantos números? '))
n2 = 0
maior = 0
c = 0
qm = 0

while c < n:
    n2 = int(input('Informe um número: '))

    if n2 > maior:
        maior = n2

    if n2 == maior:
        qm += 1

    c += 1

print(f'Maior: {maior} \n'
      f'Quantas vezes foi lido: {qm}')
