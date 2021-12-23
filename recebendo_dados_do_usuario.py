"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
- Aspas duplas -> "Pylo"
- Aspas simples -> 'Pylo'
- Aspas simples triplas -> '''Pylo'''

"""
# - Aspas duplas triplas -> """Pylo"""

# Entrada de dados 'antiga'
# print("Qual seu nome ?")
# nome = input()  # Entrada

# Entrada de dados 'moderna'
nome = input('Qual seu nome ?')

# Exemplo print 'antigo' versão 2.x
# print('Seja bem-vindo (a) %s' % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem-vindo(a) {0}' .format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja Bem-Vindo(a) {nome}')

# print("Qual sua Idade ?")
# idade = input()
idade = int(input('Qual sua Idade ?'))
# Processando

# Saída de Dados
# Exemplo print 'antigo' versão 2.x
# print('O(a) %s tem %s anos' % (nome, idade))

# Exemplo print 'moderno' versão 3.x
# print('O {0} tem {1} anos' .format(nome, idade))

# Exemplo print 'mais atual' versão 3.7
print(f'O {nome} tem {idade} anos')

"""
int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro. 
"""
print(f'E {nome} nasceu em {2018 - idade}')
