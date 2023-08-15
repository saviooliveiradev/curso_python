# aula 10

r1 = int(input('Informe  o comprimento da primeira reta: '))
r2 = int(input('Informe  o comprimento da segunda reta: '))
r3 = int(input('Informe  o comprimento da terceira reta: '))

calculo = r2 + r3

if r1 < calculo:
    print('Dá para formar um triângulo')
else:
    print('Não dá para formar um triângulo')