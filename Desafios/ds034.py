salario = int(input('Digite seu salário: '))

calculo = salario + (salario * 10 / 100)
calculo2 = salario + (salario * 10 / 100)

if salario >= 1250:
    print(f'Seu salário aumentou 10%, R${calculo:.2f}')
else:
    print(f'Seu salário aumentou 15%,  R${calculo2:.2f}')