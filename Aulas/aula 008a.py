'''python tem blibioteca e podemos fazer importações a essas bibliotecas, para incluir uma biblioteca
termos que usar o comando (import), para importar apenas 1 função da biblioteca, segue o comando 
(from doce import pudim), uma biblioteca muito famosa é math = matemática, traz umas funcionalidades
de matemáticas mais avançadas,'''

'''na biblioteca math existe a funcionalidade (ceil), que tem a  função de arredondar o número para cima,
tem o (floor) que faz o arrendondamento para baixo, termos (trunc) que vai eleminar os número da virgula
para frente, tem (pow) que praticamente é potencia, tem a (sqrt) para calcular a raiz quadrada, termos 
a funcionalidade (factorial) que é praticamente fatorar o número'''

from math import sqrt, ceil

num = int(input('Digite um número: '))

raiz = sqrt(num)

print(f'A raiz de {num} é igual a {ceil(raiz)}')