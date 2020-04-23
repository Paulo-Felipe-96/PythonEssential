"""
Loop for

Loop > Estrutura de repetição.

C ou Java

for(int i = 0; i < limitador; i++){
    //execução do loop
}

Python

for item in iteravel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome= 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)
range(valor_inicial, valor_final)

Obs.: O último valor não é incluso.

nome = 'Geek Universisty'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Transformar em lista

# Exemplo 1 (String)
for letra in nome:
    print(letra)

# Exemplo 2 (Lista)
for numero in lista:
    print(numero)

# Exemplo 3 (Range)
for numero in range(1, 10):
    print(numero)

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):  # _ descarte do valor, enumerate retorna indece, valor
    print(letra)

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n}/{qtd} valor:'))
    soma = soma + num

print(f'A soma é {soma}')

nome = 'Geek University'
for letra in nome:
    print(letra, end='')

"""

for _ in range(3):
    for num in range(1, 10 + 1):
        print('\U0001F605' * num)
