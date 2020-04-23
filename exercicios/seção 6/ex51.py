salario = 2000
salarioAtual = 0

for i in range(1, 26):
    salarioAtual = salario * 1.5

print(f'Salário em 1995 R${salario} \n'
      f'Salário em 2020 R${salario + salarioAtual} \n'
      f'Aumento ao ano R${salarioAtual / 25}')
