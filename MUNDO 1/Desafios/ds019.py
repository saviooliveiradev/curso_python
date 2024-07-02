# aula 8

import random

alu_1 = str(input('Digite seu nome: '))
alu_2 = str(input('Digite seu nome: '))
alu_3 = str(input('Digite seu nome: '))
alu_4 = str(input('Digite seu nome: '))

sorteio = random.choice([alu_1, alu_2, alu_3, alu_4])

print(f'Quem vai apagar o quadro é {sorteio}')