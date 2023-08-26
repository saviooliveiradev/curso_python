# aula 12

from random import randint 
from time import sleep

itens = ( 'Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2) # randomizando 

# Escolhendo suas opções 
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual é a sua jogada: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)

# computador jogou PEDRA
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('JOGADOR PERDE')
    else:
        print('Jogada INVÁLIDA!!')

# computador jogou PAPEL
elif computador == 1:
    if jogador == 0:
        print('JOGADOR PERDE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')    
    else:
        print('Jogada INVÁLIDA!!')

 # computador jogou TESOURA
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('JOGADOR PERDE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada INVÁLIDA!!')
