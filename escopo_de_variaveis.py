"""
Escopo de variáveis:

Dois casos de escopo:

1 - Variáveis globais;
    - Variáveis globais são reconhecidas, ou seja, compreendem todo o programa

2 - Variáveis Locais;
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas,
    ou seja, está limitado ao bloco de declaração.

Para declarar variáveis em Python fazemos:

nome = valor

Python é uma linguagem de tipagem dinânima.

Em Java:
int numero = 42;

Em C:
int numero = 42;
"""

numero = 42  # Global
print(f'Variável {numero} e Tipo {type(numero)}')

numero = 'Geek'  # Global
print(f'Variável {numero} e Tipo {type(numero)}')

numero = 42

if numero > 10:
    novo = numero + 10  # Local
    print(novo)

print(novo)
