n = int(input('Informe um número: '))
s = 0
c = 0

for i in range(0, n + 1):
    if i % 2 == 0:
        s += i
        c += 1

    if c == 50:
        break

print(f'Soma: {s}\n'
      f'Controle: {c}')
