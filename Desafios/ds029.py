# aula 10

radar = int(input('Quantos Km/h o carro passou no radar? '))

multa = 7 * (radar - 80)

if radar >= 80:
    print(f'Ele foi multado, e pagará R${multa}')
else:
    print('Está liberado')