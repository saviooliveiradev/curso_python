# aula 10

distancia = float(input('Qual é a distância da sua viagem? '))

print(f'Você está prestes a começar uma viagem de {distancia}Km')

if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45

print(f'E o preço da sua passagem será de R${preço:.2f}')
