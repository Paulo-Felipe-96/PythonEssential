"""
Tipo Float

Tipo real, decimal (casas decimais)

Obs.: O separador de casas decimais na programação é ponto (.)
"""

# Errado do ponto de vista do Float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))

# Certo do ponto de vista Float
valor = 1.44
print(valor)
print(type(valor))

# É possível
valor1, valor2 = 1, 44
print(valor1)
print(valor2)
print(f'Valor 1 {valor1}: {type(valor1)}')
print(f'Valor 2 {valor2}: {type(valor2)}')

# Podemos converser float para um int
"""
Obs.: Ao converter valores float para inteiros, nós perdemos precisão
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j
