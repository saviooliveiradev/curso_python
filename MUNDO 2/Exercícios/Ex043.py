# aula 12

peso = float(input('Qual é o seu peso? (Kg): '))
altura = float(input('Qual é a sua altura? (M): '))

imc = peso / (altura ** 2)

print(f'O imc dessa pessoa é de {imc:.1f}')

if imc < 18.5:
    print('Você está ABAIXO do peso normal')
elif imc >= 18.5 and imc < 25:
    print('Você está no na faixa de PESO NORMAL')
elif 25 >= imc < 30:
    print('Você está na faixa SOBREPESO')
elif imc >= 30 and imc < 40:
    print('Você está na faixa OBESIDADE')
else:
    print('Você está na OBESIDADE MÓRBIDA')
