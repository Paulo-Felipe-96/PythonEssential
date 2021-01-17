"""
Listas em Python funcionam como vetores/matrizes.
São dinâmicos e aceitam tipos diferentes de dados.

Python:

lista = ['paulo', 1, 'Felipe']

Listas em C ou Java não são dinâmicos e possuem tamanho
e tipo de dado fixo, exemplo:

int lista = [5]

lista_1 = [4, 5, 10, 15, 20, 351, 2, 3, 0, 25, 30]
lista_2 = ['P', 'a', 'u', 'l', 'o']
lista_3 = []
lista_4 = list(range(11))
lista_5 = list('Paulo Martins')


Exemplos:

# Ordenando as listas com sort
lista_1.sort()
print(lista_1)

lista_5.sort()
print(lista_5)

# lista_1.append(1, 2)

lista_1.append([125, 135, 145])
print(lista_1)

lista_1.extend([24, 25, 26])
print(lista_1)

# Inserindo novo elemento informando a posição

lista_1.insert(2, 'Novo')
lista_1.extend(lista_2)
print(lista_1)

lista_2 = lista_2 + lista_1
print(lista_2)

# Printando lista inversa

print(lista_1[::-1])

# Invertendo os elementos antes de printar

lista_1.reverse()
print(lista_1)

# Copiando uma lista

lista_6 = lista_2.copy()
print(lista_6)

# Removendo o último elemento

lista_5.pop()
print(lista_5)

# Remover elemento pelo índice
# Se não houver elemento no indice informado, teremos um erro

lista_1.pop(0)
print(lista_1)

# Zerando (limpando) completamente a lista inteira
print(lista_1)
lista_1.clear()
print(lista_1)

# Repetindo elementos numa lista

nova = [1, 2, 3]
nova = nova * 3

# Converter string para lista
# Por padrão, o split separa os elemetos por espaços
curso = 'Programação em Python: Essencial'
print(curso)

print(curso.split())

# Exemplo 2, podemos especificar o delimitador para separar
# os elementos da string

curso = 'Estamos aprendendo programação, certo?'
print(curso.split(','))

lista_6 = ['Programação', 'em', 'Python']

# Junte os elementos atribuindo espaços e transforme em string
curso = ' '.join(lista_6)
print(lista_6)
print(curso)

curso = 'Programação$em$Python$Essencial'
print(curso.split('$'))

# Iterando lista com for
impar, par = [], []
for elemento in lista_1:
    if elemento % 2 == 0:
        par.append(elemento)
    else:
        impar.append(elemento)

print(par)
print(impar)

# Lógica para adição de produtos ao carrinho usando while e exibindo os itens com for
carrinho = []
produto = ''

while produto != 'sair':
    print('Adicione um produto ao carrinho ou pressione sair para finalizar: ')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for item in carrinho:
    print(item)


# É possível criar uma lista com variáveis

n1, n2 = 1, 2
numeros = [1, 2]
numeros_ = [n1, n2]

print(numeros, numeros_)


# Os elementos são acessados pelo index, que começa de 0

cores = ['verde', 'amarelo', 'azul']

print(cores[0])

# Acessando pelo índice negativo

print(cores[-1])  # exibirá o último



cores = ['verde', 'amarelo', 'azul']

for cor in cores:
    print(cor)


cores = ['verde', 'amarelo', 'azul']

# enumerate gera par (chave: valor) indicando o índice do elemento
# indice = enumerate, cor = cores
for indice, cor in enumerate(cores):
    print(indice, cor)

frutas = list(enumerate(cores))
print(frutas)

# Listas aceitam valores repetidos

lista = []
lista.append(42)
lista.append(42)
lista.append('Oi')
lista.append(42)

print(lista)

# Encontrar o índice de um elemento na lista

lista = ['PlayStation 4', 'Xbox One', 'Xiaomi Mi Max 3', 1, 2, 1]

print(lista.index('PlayStation 4'))
print(lista.index('Xiaomi Mi Max 3'))

# Valores fora da lista geram ValueError
try:
    print(lista.index('Xiaomi'))
except ValueError:
    print('Valor não encontrado')
else:
    print(lista)

# Buscando um valor a partir de uma posição definida do index

print(lista.index(1, 2))
print(lista.index(1, -1))

# Buscando um valor entre um range, 1 e 4 (n e y)
print(lista.index(1, 1, 3))

# Revisão de slicing
# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# Parametro inicio, comece do indice 2 e vai até o final [2:]

lista = [1, 2, 'Paulo', 'Martins', 'Magalhães', 'Felipe']

print(lista[1:])

print(lista[:2])  # comece de 0 e vá até 2 (mas o último não é incluído

print(lista[1::2])  # comece de 1, até o final, pulando de 2 em 2

print(lista[::2])  # de 0 até final, de 2 em 2

# Invertendo valores em uma lista

nome = ['Paulo', 'Martins']
print(nome)

nome[0], nome[1] = nome[1], nome[0]
print(nome)

nome.reverse()
print(nome)

# Soma, Máximo, Mínimo, Tamanho lista
lista = list(range(1, 7))
print(lista)

print(f'Soma: {sum(lista)}')
print(f'Valor máximo: {max(lista)}')
print(f'Valor mínimo: {min(lista)}')
print(f'Tamanho: {len(lista)}')

# Transformando lista em tupla
lista = list(range(0, 10))
tupla = tuple(lista)

print(lista, tupla)
print(type(lista), type(tupla))


# Desempacotamento de listas
# Mais elementos do que variáveis para receber, temos Vallue error
# O contrátio também
# elementos > variaveis
# variaveis > elementos

lista = list(range(0, 3))

print(lista)
n1, n2, n3 = lista

print(n1, n2, n3)

try:
    n1, n2, n3, n4 = lista
except ValueError:
    print('Número de variáveis e elementos incompatível')
else:
    print('Deu certo!')

# Shallow e Deep Copy

lista = list(range(0, 3))
lista2 = lista.copy()

print('Deep Copy')
print(lista)
print(lista2)

# Adicionar um valor na lista2 não afeta a primeira lista
# Deep Copy

lista2.append('+1 valor')
print(lista)
print(lista2)

# Adicionar um valor na lista2 afeta a primeira pois ambas apontam para
# o mesmo endereço de memória, pois não são cópias, são representações
# uma da outra
# Shallow Copy
lista = list(range(0, 3))
lista2 = lista

print('Shallow Copy')
print(lista)
print(lista2)

lista2.append('+1 valor')
print(lista)
print(lista2)

"""
