"""
Loop while

while expressão_booleana:
    execução do loop

O bloco while será repetido enquanto a expressão booleana for verdadeira.
Booleano, a expressão é Verdadeira ou Falsa.

num = 5

num < 5

# Exemplo 1

numero = int(input('Contar até?: '))
contador = 0

while contador <= numero:
    print(contador)
    # contador += 1 - looping infinito

"""

resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou Jéssica? ')