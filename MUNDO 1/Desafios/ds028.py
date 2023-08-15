# aula 10

from random import randrange

aleatorio = randrange(0, 5)
print(aleatorio)

n = int(input('Qual número inteiro entre 0 e 5 a maquina pensou? '))

if aleatorio == n:
    print('Parabéns, você acertou!!!')
else:
    print('Errou, tente de novo!')