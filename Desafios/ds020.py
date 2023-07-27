# aula 8

import random

aluno1 = str(input('Nome do primeiro Aluno(A): '))
aluno2 = str(input('Nome do primeiro Aluno(A): '))
aluno3 = str(input('Nome do primeiro Aluno(A): '))
aluno4 = str(input('Nome do primeiro Aluno(A): '))

alunos = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.shuffle(alunos)



print(sorteio)


