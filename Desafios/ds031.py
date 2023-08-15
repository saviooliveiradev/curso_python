# aula 10

distancia = int(input('Qual a distância da viagem em Km? '))

calculo = 0.50 * distancia
calculo2 = 0.45 * distancia

if distancia <= 200:
    print(F'O valor da viagem ficou R${calculo}')
else:
    print(f'Sua viagem custou R${calculo2}')