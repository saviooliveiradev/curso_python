# aula 7

largura = float(input('Digite a largura da sua parede em metros: '))
altura = float(input('Digite a altura da sua parede em metros: '))

area = largura * altura

tinta = (area / 2) 

print(f'A sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m².\n Para pintar essa parede, você precisará de {tinta}l de tinta.')