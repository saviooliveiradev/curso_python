# aula 8

import random

aluno1 = str(input('Nome do primeiro Aluno(A): '))
aluno2 = str(input('Nome do primeiro Aluno(A): '))
aluno3 = str(input('Nome do primeiro Aluno(A): '))
aluno4 = str(input('Nome do primeiro Aluno(A): '))

sorteio = random.choice([aluno1, aluno2, aluno3, aluno4]) #Retorna um elemento aleatório da sequência não vazia

print(f'O escolhido foi {sorteio}')