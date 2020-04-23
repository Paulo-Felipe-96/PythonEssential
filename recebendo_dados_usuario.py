"""
Recebendo dados do usário

dir(__builtins__), recursos integrados da linguagem

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie"
- Aspas simples triplas -> '''Angelina Jolie'''
- Aspas duplas triplas
"Paulo"
"""
# Entrada de dados
# print("Qual seu nome?")
# nome = input()

nome = input('Qual seu nome? ')

# Exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem-vindo {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}!')

idade = int(input("Qual sua idade: "))

# Processamento

# Saída
# print('%s tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print('{0} tem {1} anos de idade.'.format(nome, idade))

# Exemplo de print 'mais atual' 3.7

"""
int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro
"""
print(f'{nome} tem {idade} anos de idade e nasceu em {2020 - idade}.')
