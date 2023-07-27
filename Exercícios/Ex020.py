# aula 8

from random import shuffle

aluno1 = str(input('Nome do primeiro Aluno(A): '))
aluno2 = str(input('Nome do primeiro Aluno(A): '))
aluno3 = str(input('Nome do primeiro Aluno(A): '))
aluno4 = str(input('Nome do primeiro Aluno(A): '))

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)



print('A ordem de apresentação será ')
print(lista)