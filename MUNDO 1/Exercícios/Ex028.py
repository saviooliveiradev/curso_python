# aula 10

from random import randint
from time import sleep #faz o computador esperar, como dá um pause no programa

computador = randint(0, 5) # faz o computador sortear 

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar')
print('-=-' * 20)

jogador = int(input('Que número eu pensei? ')) # o jogador tenta advinhar

print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}!')
