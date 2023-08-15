# aula 

salário = float(input('Qual é o salário do funcionário? '))

if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)

print(f'Quem ganhava R${salário:.2f} passsa ganhar R${novo:.2f} agora')