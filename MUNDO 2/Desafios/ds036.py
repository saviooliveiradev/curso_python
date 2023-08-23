# aula 12

valor = float(input('Qual o valor da casa? '))
salario = float(input('Quanto é o seu salário? '))
pagar = int(input('Em quantos anos o senhor quer pagar? '))

exceder = salario + (salario * 30 / 100)
pagamento = valor / pagar 

if pagamento >= exceder:
    print('\033[31mCompra Negada!!!\033[m')
else:
    print('\033[32mCompra Aprovada!!!\033[m')
