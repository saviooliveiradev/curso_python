# aula 12

casa = int(input('Valor da casa: R$'))
salario = int(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

prestação = casa / (anos * 12)
mínimo = salario * 30 / 100

if prestação <= mínimo:
    print(f'Para pagar uma casa de R${casa} em {anos} a prestação será de R${prestação:.2f} \n EMPRÉSTIMO APROVADO!!!')
else:
    print(f'Para pagar uma casa de R${casa} em {anos} a prestação será de R${prestação:.2f} \n EMPRÉSTIMO APROVADO!!!')