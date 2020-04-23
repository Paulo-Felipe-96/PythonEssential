idade = 1
ci = 0
media = 0

while idade != 0:
    idade = int(input('Informe a idade: '))

    if idade == 0:
        break

    media += idade
    ci += 1

print(f'Média de idades: {media / ci}')
