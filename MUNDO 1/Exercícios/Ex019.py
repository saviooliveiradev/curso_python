# aula 8
from random import choice

aluno1 = str(input('Nome do primeiro Aluno(A): '))
aluno2 = str(input('Nome do primeiro Aluno(A): '))
aluno3 = str(input('Nome do primeiro Aluno(A): '))
aluno4 = str(input('Nome do primeiro Aluno(A): '))

lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = choice(lista) #eascolha um objeto na lista

print(f'O escolhido foi {sorteio}')