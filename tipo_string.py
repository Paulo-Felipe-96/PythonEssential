"""
Tipo string

Em Python, um dado é considerado do tipo String sempre que:

- Estiver entre áspas simples > 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre áspas duplas > "uma string", "234", "a", "True", "42.3"
- Estiver entre áspas simples triplas > '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
- Estiver entre áspas duplas triplas.

nome = 'Geek University'
print(f'{nome}, {type(nome)}')

nome = "Gina's Bar"
print(f'{nome}, {type(nome)}')

nome = 'Angelina \nJolie'
print(f'{nome}, {type(nome)}')

nome = "Angelina \" Jolie"
print(f'{nome}, {type(nome)}')

"""

nome = 'Geek University'
print(nome.upper())
print(nome.lower())
print(nome.split())
print(nome[0:5])  # Slice de string
print(nome[5:15])  # Slice de string

print(nome.split()[0])
print(nome.split()[1])
print(nome[14])

"""
Começe do primeiro, vá até o último elemento e inverta
"""
print(nome[::-1])  # INversão da String Pythônico

print(nome.replace('G', 'P'))
print(nome.replace('G', 'P')[::-1])
print(nome.replace(nome[4], '-'))
print(nome.replace(nome[4], '.*.')[::-1])

texto = 'socorram me subino onibus em marrocos'
print(texto)
print(texto[::-1])

nome = 'ana'  # Palíndromo
print(nome)
print(nome[::-1])
