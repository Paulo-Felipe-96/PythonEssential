n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))

s1 = n1 - n2
s2 = 0
mp = 1

for i in range(0, s1):

    if i % 2 == 0:
        s2 += i
    if i % 2 == 1:
        mp *= i

print(f'Soma dentro do intervalo: {s2} \n'
      f'Multiplicação dentro do intervalo: {mp}')
