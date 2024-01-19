from random import randrange

aleatorio = randrange(0, 10)
print(aleatorio)
resposta = ''

while resposta != aleatorio: 
    resposta = int(input('Qual número inteiro entre 0 e 10 a maquina pensou? '))
    if resposta != aleatorio:
        print('Errou, tente novamente')
    else:
        print('Parabéns, você acertou!') 
