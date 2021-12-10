"""
PEP8 - Python Enhancement Proposal
São propostas de melhorias para linguagem Python

The Zen of Python

import this

A ideia da PEP8 é que possamos escrever codigos Python de forma Pythonica
"""

"""
[1] - Utilize Camel Case para nomes de classes;
"""


class Calculadora:
    pass


class CalculadoraCientifica:
    pass


"""
[2] - Utilize nomes em minusculos, separados por underline para funções ou variáveis  
"""


def soma():
    pass


def soma_dois():
    pass


numero = 4
numero_impar = 5

"""
[3] - Utilize 4 espaços para identação 
OBS: De preferência apertar espaço 4 vezes do que apertar tab, pois o tab varia de computador para computador 
"""

if 'a' in 'banana':
    print('tem')


"""
[4] - Linhas em branco
- Separar funções e definições de classes com duas linhas em branco:
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;
"""

class Errado:
    pass


class Certo:
    pass


"""
[5] - Imports deve sempre ser feitos em linhas separadas; 
"""
# Import Errado
import sys,os

# Import Certo
import sys
import os

# Não ah problemas em utilizar:
from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quisquer comentários ou docstrings e
# antes de  constantes ou variaveis globais.

"""
[6] - Espaços em expressões e instruções 
"""

# Não Faça:

funcao(  algo [ 1 ], { outro : 2 } )

# Faça:

funcao(algo[1], {outro: 2})

# Não faça:

algo (1)

# Faça

algo(1)

# Não faça

dict ['chave'] = lista [indice]

# Faça

dict['chave'] = lista[indice]

# Não faça:

x              = 1
y              = 3
variavel_longa = 5

# Faça

x = 1
y = 3
variavel_longa = 5

"""
[7] - Termine sempre uma instrução com uma nova linha 
"""

import this
