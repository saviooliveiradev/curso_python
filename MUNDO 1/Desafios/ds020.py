# aula 8

from random import shuffle

alu_1 = str(input('Digite seu nome: '))
alu_2 = str(input('Digite seu nome: '))
alu_3 = str(input('Digite seu nome: '))
alu_4 = str(input('Digite seu nome: '))

lista = [alu_1, alu_2, alu_3, alu_4]
shuffle(lista)

print(f'A lista nova de alunos é {lista}')